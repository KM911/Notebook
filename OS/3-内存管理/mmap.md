>[!note] Memory mapped files 将文件映射到我们的内存中.

## 为什么可以实现?

从逻辑来看,我们的内存和磁盘都是一系列字节序列.两者没有什么区别,如果可以将内存中的部分区域视为磁盘,读写内存可比读写磁盘的速度要快多了. 
这样不就可以提高性能的性能了吗?

## mmap的作用

1. 简化文件读写操作. 
2. 共享内存.
3. 提高IO性能. 

### 简化文件读写操作 

这里需要你对于C语言的文件读写比较熟悉,如果不是的话, 可以查看一下[[file]].
常见的文件操作. 我们将文件中的某一段数据读取出来,将这段数据写到文件的某个位置,假设是末尾吧. 

```c
void FileOperation(){

}
```



如果使用mmap的话,操作就变得简单得多得多了.










错误理解 : 将内存的一部分视为磁盘,提高IO性能.
正确理解 : 直接将磁盘视为内存的一部分,不必从磁盘读取到内存中,然后在交给程序. 

#### 实现导致的差异

除开C语言的实现是和操作系统最接近的,其余的多多少少有些细节的差异.
比如go的 [mmap](https://pkg.go.dev/golang.org/x/exp/mmap) 官方实现就只提供了read,无法write,并且API很少.不过性能还是不错的,特别是在频繁读取的场景下. 

![[Pasted image 20231016211829.webp]]

benchmark测试代码.

```go
func BenchmarkMmap(b *testing.B) {
	b.ReportAllocs()
	buff := make([]byte, 4096)
	at, _ := mmap.Open(FileName)

	//这里难道不是我需要的时候直接读取部分
	for i := 0; i < b.N; i++ {
		//多次读取
		for i := 0; i < loops; i++ {
			at.ReadAt(buff, int64(i*4096))
			at.Close()
		}
	}
}

func BenchmarkFileIO(b *testing.B) {
	b.ReportAllocs()
	content := make([]byte, 4096)
	file, err := os.Open(FileName)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	for i := 0; i < b.N; i++ {
		for i := 0; i < loops; i++ {
			file.Read(content)
		}
	}
}

```

```bash
goos: windows
goarch: amd64
pkg: hello
cpu: AMD Ryzen 5 5600H with Radeon Graphics
BenchmarkMmap
BenchmarkMmap-12          102843             11478 ns/op            8000 B/op 500 allocs/op
BenchmarkFileIO
BenchmarkFileIO-12          1279            940113 ns/op               3 B/op 0 allocs/op
```

即使是在window上的性能差距已经很多了,但是到了linux上,差距更是离谱,下面是我在wsl跑的,物理机应该会更加好看一些.
```bash
goos: linux
goarch: amd64
pkg: hello
cpu: AMD Ryzen 5 5600H with Radeon Graphics
BenchmarkMmap-12           92520             12572 ns/op            8000 B/op     
  500 allocs/op
BenchmarkFileIO-12            27          40510725 ns/op               4 B/op     
    0 allocs/op
```


如果你想要高性能就该使用mmap来读取文件中的数据. 


让我们试试看c的版本吧. 最原汁原味的mmap还是只能看我们的C呢. 

C语言如何做benchmark呢? 直接time ./a.out  存在一定的误差 不过其实也不多,只要你执行的内容是一致的,时间差距不会太大.

这里我推荐一个rust的命令行工具.


对于很多API是非常失望的,什么意思呢?
比如读文件,会给文件上锁,其实说实话,这里还是没有"高性能",我觉得就是在极端条件下做这些事情才是对的.
![[Pasted image 20231016204055.webp]]


我这里没有理解的地方在于,如果你需要进行读取,并且这里是缺页的,肯定还是会发生内核态到用户态切换的,所以说其实mmap好像其实也没有提高性能.













### 其他作用

因为mmap其实是将磁盘映射到内存,也就是说只要两个线程/进程加载的是同一片区域,就可以实现"共享内存"

```c
void ChangeMemoryWithFork(){
  int SharedMemory = 100;
  if (fork() == 0) {
    SharedMemory = 200;
  }else{
    sleep(1);
  } 
  printf("Parent process: %d\n", SharedMemory);
}

void SharedMemoryWithFork(){
  int * SharedMemory = mmap(NULL,4096,PROT_READ|PROT_WRITE,MAP_ANONYMOUS|MAP_SHARED,-1,0);
  *SharedMemory = 100;
  if (fork() == 0) {
    *SharedMemory = 200;
  }else{
   sleep(1);
  }
  printf("Parent process: %d\n", *SharedMemory);
  munmap(SharedMemory,4096);
}
```

其中的 sleep主要了是为了确保我们的child thread可以




mmap可以提高性能的原因主要有以下几个：


减少用户态到内核态的切换：传统的I/O操作需要通过系统调用来读取或写入文件，这会导致用户态到内核态的切换。而mmap可以将文件映射到用户空间，从而避免了用户态到内核态的切换，提高了性能。
减少数据的拷贝次数：传统的I/O操作需要将数据从文件系统复制到内核空间的缓冲区，然后再从内核空间的缓冲区复制到用户空间的缓冲区。而mmap可以直接将文件映射到用户空间，从而避免了数据在内核空间和用户空间之间的拷贝，提高了性能。
提高了数据访问的效率：mmap可以将文件映射到用户空间，从而可以直接通过指针来访问文件数据，提高了数据访问的效率。
具体来说，mmap可以提高I/O性能的表现如下：

读取文件时，mmap可以直接将文件映射到用户空间，从而避免了用户态到内核态的切换，提高了读取文件的效率。
写入文件时，mmap可以直接将数据写入用户空间，从而避免了数据在内核空间和用户空间之间的拷贝，提高了写入文件的效率。
共享内存时，mmap可以将文件映射到多个进程的地址空间，从而提高了进程间通信的效率。
mmap是一种比较通用的I/O优化技术，适用于多种场景。在实际应用中，可以根据具体的场景来选择是否使用mmap。



可以做一个测试 不过这里就需要C语言了,我可以看看go是不是又mmap的功能

我怀疑这里其实是假的 它和我们普通的文件操作其实好像没有什么本质的区别 我找不到其中的性能差异呀 就是说 我们还是CPP工作一年多的人其实也还是什么都不会






### mmap 共享内存

```c
void SharedMemoryFork(){
  int SharedMemory = 100;
  if (fork() == 0) {
    SharedMemory = 200;
  }else{
    sleep(1);
  } 
  printf("Parent process: %d\n", SharedMemory);
}

void SharedMemoryForkMmap(){
  int * SharedMemory = mmap(NULL,4096,PROT_READ|PROT_WRITE,MAP_ANONYMOUS|MAP_SHARED,-1,0);
  *SharedMemory = 100;
  if (fork() == 0) {
    *SharedMemory = 200;
  }else{
   sleep(1);
  }
  printf("Parent process: %d\n", *SharedMemory);
  munmap(SharedMemory,4096);
}

```
