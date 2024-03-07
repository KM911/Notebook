
## go读写文件 该设置多大的缓冲区呢? 

>[!note] 文件系统读写的最小单位
>操作系统为我们屏蔽了硬件的差异,抽象出了一个兼容层. Windows文件系统中以Cluster作为读写的基本单位,Linux以Block作为基本单位. 

>[!exp]- 查看其大小 
>linux使用 ` stat / | grep "Block"`
>```txt
Size: 4096            Blocks: 8          IO Block: 4096   directory
>```
>windows使用`fsutil fsinfo ntfsinfo C: | grep "Bytes"`
>```txt
Bytes Per Sector  :                512
Bytes Per Physical Sector :        4096
Bytes Per Cluster :                4096
Bytes Per FileRecord Segment    :  1024
>```

根据上面的数据显示,我应该使用4KB大小的缓冲区. 

## 不同缓冲区大小对于文件读写性能影响实验 


>[!tip] go内置了benchmark,这是一个好的工程化实践,我们可以针对性地设计实验进行性能分析

详细代码请查看 GitHub链接 

### 核心函数 


```go
func ReadFile(_src string, _size int) {
	buffer := make([]byte, _size)
	file, err := os.Open(_src)
	if err != nil {
		panic(err)
	}
	for {
		n, err := file.Read(buffer)
		if err != nil {
			break
		}
		_ = buffer[:n]
	}
}
```


### benchmark 

两种场景,分别是小文件 -- 特指只有1-2KB大小. 大文件 100MB以上的文件. 

缓冲区大小分别是 1,2,4,8,16,32 KB / MB,以及100% 50% 25%文件大小. 

```go
func BenchmarkFileRead1KB(b *testing.B) {
	for i := 0; i < b.N; i++ {
		ReadFile(BigFile, KB)
	}
}
func BenchmarkFileRead2KB(b *testing.B) {
	for i := 0; i < b.N; i++ {
		ReadFile(BigFile, 2*KB)
	}
}
```

为了有更好的性能,go还内置了bufio库,本次实验也将其作为实验对象进行benchmark. 

>[!faq] 不妨大胆猜测一下,所谓的bufio就是每次按照block进行读取,减少read/write系统调用的次数. 



## 实验结果展示

你会发现我的结果和go bench有一些差别,因为这里我是使用自己的工具将其优化了. 
主要是将函数执行耗时进行排序,以耗时最少的作为 baseline.

> [!others]- 读取1KB大小的文件
> ```txt
> goos: windows
> goarch: amd64
> pkg: github.com/KM911/demo/benchmark
> cpu: AMD Ryzen 5 5600H with Radeon Graphics
> BenchmarkFileSize                  16275.0ns/op          1.0    0.0ns/op
> BenchmarkBufFileQuarter            16597.0ns/op         1.02    322.0ns/op
> BenchmarkRead4KB                   16603.0ns/op         1.02    328.0ns/op
> BenchmarkReadBufio1KB              16716.0ns/op        1.027    441.0ns/op
> BenchmarkBufFileHalfSi             16830.0ns/op        1.034    555.0ns/op
> BenchmarkBufFileS                  16947.0ns/op        1.041    672.0ns/op
> BenchmarkReadBufio2KB              16984.0ns/op        1.044    709.0ns/op
> BenchmarkRead8KB                   17083.0ns/op         1.05    808.0ns/op
> BenchmarkReadBufio4KB              17180.0ns/op        1.056    905.0ns/op
> BenchmarkFileHalfSize              17310.0ns/op        1.064    1035.0ns/op
> BenchmarkRead2KB                   17597.0ns/op        1.081    1322.0ns/op
> BenchmarkReadBufio8KB              17611.0ns/op        1.082    1336.0ns/op
> BenchmarkRead16KB                  18036.0ns/op        1.108    1761.0ns/op
> BenchmarkRead1KB                   18219.0ns/op        1.119    1944.0ns/op
> BenchmarkReadBufio16KB             18514.0ns/op        1.138    2239.0ns/op
> BenchmarkRead32KB                  19449.0ns/op        1.195    3174.0ns/op
> BenchmarkReadBufio32KB             20340.0ns/op         1.25    4065.0ns/op
> BenchmarkFileQuarterSize           20387.0ns/op        1.253    4112.0ns/op
> BenchmarkReadBufio1MB             134915.0ns/op         8.29    118640.0ns/op
> BenchmarkRead1MB                  136853.0ns/op        8.409    120578.0ns/op
> BenchmarkRead2MB                  182449.0ns/op        11.21    166174.0ns/op
> BenchmarkReadBufio2MB             219710.0ns/op         13.5    203435.0ns/op
> BenchmarkRead4MB                  257632.0ns/op        15.83    241357.0ns/op
> BenchmarkReadBufio4MB             301442.0ns/op       18.522    285167.0ns/op
> BenchmarkRead8MB                  617350.0ns/op       37.932    601075.0ns/op
> BenchmarkReadBufio8MB             908992.0ns/op       55.852    892717.0ns/op
> BenchmarkRead16MB                1377405.0ns/op       84.633    1361130.0ns/op
> BenchmarkReadBufio16MB           2129991.0ns/op      130.875    2113716.0ns/op
> BenchmarkRead32MB                3720603.0ns/op      228.608    3704328.0ns/op
> BenchmarkReadBufio32MB           4450179.0ns/op      273.436    4433904.0ns/op
> ```

对于小文件读写的结果并不让人感到意外,开辟一个非常大缓冲区去读一个小文件不仅浪费了内存还由于需要申请大量的内存导致速度感人. 

1KB和16KB的差距并不显著,都在可以接受的范围内只有10%左右的差距,差距可以忽略.  

值得注意的是,bufio只有当你的缓冲区小于block时可以带来性能提升,其余的时候都是负面收益. 所以不要想当然地认为使用了bufio性能就一定好. 

>[!others]- 读取100MB的文件
> ```txt
> goos: windows
> goarch: amd64
> pkg: github.com/KM911/demo/benchmark
> cpu: AMD Ryzen 5 5600H with Radeon Graphics
> BenchmarkReadBufio1MB           13231525.0ns/op          1.0    0.0ns/op
> BenchmarkRead1MB                13254417.0ns/op        1.002    22892.0ns/op
> BenchmarkReadBufio2MB           13692429.0ns/op        1.035    460904.0ns/op
> BenchmarkRead2MB                13703544.0ns/op        1.036    472019.0ns/op
> BenchmarkRead4MB                13932077.0ns/op        1.053    700552.0ns/op
> BenchmarkReadBufio4MB           14077248.0ns/op        1.064    845723.0ns/op
> BenchmarkReadBufio8MB           16097806.0ns/op        1.217    2866281.0ns/op
> BenchmarkRead8MB                16115280.0ns/op        1.218    2883755.0ns/op
> BenchmarkReadBufio32KB          17874616.0ns/op        1.351    4643091.0ns/op
> BenchmarkRead32KB               17995909.0ns/op         1.36    4764384.0ns/op
> BenchmarkReadBufio16MB          19868725.0ns/op        1.502    6637200.0ns/op
> BenchmarkRead16MB               19960625.0ns/op        1.509    6729100.0ns/op
> BenchmarkFileQuarterSize        21406129.0ns/op        1.618    8174604.0ns/op
> BenchmarkBufFileQuarter         21494687.0ns/op        1.625    8263162.0ns/op
> BenchmarkReadBufio32MB          22207569.0ns/op        1.678    8976044.0ns/op
> BenchmarkRead32MB               22576478.0ns/op        1.706    9344953.0ns/op
> BenchmarkReadBufio16KB          22917932.0ns/op        1.732    9686407.0ns/op
> BenchmarkRead16KB               23179257.0ns/op        1.752    9947732.0ns/op
> BenchmarkFileHalfSize           24599869.0ns/op        1.859    11368344.0ns/op
> BenchmarkBufFileHalfSi          24711621.0ns/op        1.868    11480096.0ns/op
> BenchmarkFileSize               29328449.0ns/op        2.217    16096924.0ns/op
> BenchmarkBufFileS               29419713.0ns/op        2.223    16188188.0ns/op
> BenchmarkRead8KB                32119684.0ns/op        2.428    18888159.0ns/op
> BenchmarkReadBufio8KB           32601111.0ns/op        2.464    19369586.0ns/op
> BenchmarkReadBufio4KB           49854575.0ns/op        3.768    36623050.0ns/op
> BenchmarkRead4KB                50008214.0ns/op        3.779    36776689.0ns/op
> BenchmarkReadBufio2KB           51449764.0ns/op        3.888    38218239.0ns/op
> BenchmarkReadBufio1KB           51981355.0ns/op        3.929    38749830.0ns/op
> BenchmarkRead2KB                75542057.0ns/op        5.709    62310532.0ns/op
> BenchmarkRead1KB               129211050.0ns/op        9.765    115979525.0ns/op
> ```


但是大文件读写的结果让我感到意外. 根据上面文件系统最小单位的分析,使用4kb还是16MB的缓冲区读取的blcok数量是一致的,不应该有非常大的性能差距. 是什么原因导致的使用较小的缓冲区的性能较差的呢? 

其实也很简单,看看go的read函数具体实现就好了. 

简单跳转一下,就可以看到这个.

go语言的Read实现中,每次进行读操作时都会给文件上锁,这解释了为什么大文件读取时用较小的缓冲区来读取会有非常差的性能. 
```go
func (fd *FD) Read(buf []byte) (int, error) {
	if err := fd.readLock(); err != nil {
		return 0, err
	}
	defer fd.readUnlock()
	...
}
``` 


操作系统的read/write并不提供任何的并发保护机制.换而言之,并发读写文件并不安全. 

>[!exp]- 并发读写文件 C语言
> ```c
> #include <unistd.h>
> #include <stdlib.h>
> #include <stdio.h>
> #include <errno.h>
> #include <fcntl.h>
> #include <string.h>
> #include <sys/file.h>
> #include <wait.h>
> 
> #define COUNT 100
> #define NUM 64
> #define FILEPATH "./count.txt"
> 
> int Open(const char *path, int oflag)
> {
>     int fd;
>     fd = open(path, oflag);
>     if (fd < 0) {
>         perror("open()");
>         exit(1);
>     }
>     return fd;
> }
> 
> 
> int do_child(const char *path)
> {
>     int fd;
>     int ret, count;
>     char buf[NUM];
>     fd = Open(path, O_RDWR);
>     /*    */
>     ret = read(fd, buf, NUM);
>     if (ret < 0) {
>         perror("read()");
>         exit(1);
>     }
>     buf[ret] = '\0';
>     count = atoi(buf);
>     count++;
>     sprintf(buf, "%d", count);
>     lseek(fd, 0, SEEK_SET);
>     ret = write(fd, buf, strlen(buf));
>     close(fd);
>     exit(0);
> }
> void init_Count(){
>     int fd;
>     fd = remove(FILEPATH);
>     if (fd < 0) {
>         perror("remove()");
>         exit(1);
>     }
>     fd = open(FILEPATH, O_RDWR|O_CREAT, 0666);
>     if (fd < 0) {
>         perror("open()");
>         exit(1);
>     }
>     write(fd, "0\0", 2);
>     close(fd);
> }
> 
> int main()
> {   
>     init_Count();
>     pid_t pid;
>     int count;
> 
>     for (count=0;count<COUNT;count++) {
>         pid = fork();
>         if (pid < 0) {
>             perror("fork()");
>             exit(1);
>         }
> 
>         if (pid == 0) {
>             do_child(FILEPATH);
>         }
>     }
> 
>     for (count=0;count<COUNT;count++) {
>         wait(NULL);
>     }
>     // 最后读取该文件查看结果
>     int fd;
>     fd = Open(FILEPATH, O_RDONLY);
>     char buf[NUM];
>     int ret;
>     ret = read(fd, buf, NUM);
>     if (ret < 0) {
>         perror("read()");
>         exit(1);
>     }
>     buf[ret] = '\0';
>     printf("count = %s\n", buf);
>     return 0;
> }
> 
> ```

>[!exp]- 为了保证安全,我们需要给文件上锁. 
> ```c
> // 
> #include <unistd.h>
> #include <stdlib.h>
> #include <stdio.h>
> #include <errno.h>
> #include <fcntl.h>
> #include <string.h>
> #include <sys/file.h>
> #include <wait.h>
> 
> #define COUNT 100
> #define NUM 64
> #define FILEPATH "./count.txt"
> 
> int Open(const char *path, int oflag)
> {
>     int fd;
>     fd = open(path, oflag);
>     if (fd < 0) {
>         perror("open()");
>         exit(1);
>     }
>     return fd;
> }
> 
> 
> int do_child(const char *path)
> {
>     int fd;
>     int ret, count;
>     char buf[NUM];
>     int lock;
>     fd = Open(path, O_RDWR);
>     
>     ret = flock(fd, LOCK_EX);
>     if (ret < 0) {
>         perror("flock()");
>         exit(1);
>     }
>     /*    */
>     ret = read(fd, buf, NUM);
>     if (ret < 0) {
>         perror("read()");
>         exit(1);
>     }
>     buf[ret] = '\0';
>     count = atoi(buf);
>     ++count;
>     sprintf(buf, "%d", count);
>     lseek(fd, 0, SEEK_SET);
>     ret = write(fd, buf, strlen(buf));
>     
>     // free lock
>     ret = flock(fd, LOCK_UN);
>     if (ret < 0) {
>         perror("flock()");
>         exit(1);
>     }
>     close(fd);
> 
>     exit(0);
> }
> void init_Count(){
>     int fd;
>         fd = remove(FILEPATH);
>     if (fd < 0) {
>         perror("remove()");
>         exit(1);
>     }
>     fd = open(FILEPATH, O_CREAT, 0666);
>     if (fd < 0) {
>         perror("open()");
>         exit(1);
>     }
>     char buf[NUM];
>     buf[0] = '0';
>     buf[1] = '\0';
>     ssize_t w=  write(fd, buf, 2);
>     if (w < 0) {
>         perror("write()");
>         exit(1);
>     }
>     close(fd);
> }
> 
> 
> int main()
> {   
>     init_Count();
> 
>     pid_t pid;
>     int count;
>     for (count=0;count<COUNT;count++) {
>         pid = fork();
>         if (pid < 0) {
>             perror("fork()");
>             exit(1);
>         }
> 
>         if (pid == 0) {
>             do_child(FILEPATH);
>         }
>     }
> 
>     for (count=0;count<COUNT;count++) {
>         wait(NULL);
>     }
>     // 最后读取该文件查看内容
>     int fd = Open(FILEPATH, O_RDWR);
>     char buf[NUM];
>     int ret;
>     ret = read(fd, buf, NUM);
>     if (ret < 0) {
>         perror("read()");
>         exit(1);
>     }
>     buf[ret] = '\0';
>     printf("count = %s\n", buf);
>     return 0;
> }
> 
> ```

go因为协程随处可见,出于安全考虑,在read/write的实现中都添加了锁来进行保护. 相对应地在正常情况下读写性能就会稍弱一些. 我本人暂时还不知道go中如何实现无锁文件读写,希望你可以不吝赐教,我对此表示感谢.

## 总结 

1. 对于小文件读写,大部分方式性能差距并不明显,只要你不是无脑开辟一大块缓冲区.
2. go的read/write实现都有文件锁,所以是并发安全的,你可以在goroutine中愉快玩耍. 同时请注意, 既然已经有锁了,就没有必要再使用mutex或者其他机制保证并发安全了,这样只会导致你的goroutine可能不如单线程程序. 
3. 已知read/write会自动上锁,所以针对大文件读写应该尽量采用较大的缓冲区比较为合理,可以减少锁的使用.个人认为 缓冲区大小和文件大小保持两个数量级的差别比较合理.
4. bufio只有在你需要频繁小尺度地读取文件时可以提高性能(主要是减少锁的开销),不然它的性能很可能不如普通的io. 


