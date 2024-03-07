
## file modes

"r"：以只读方式打开文件，文件必须存在。
"w"：以只写方式打开文件，如果文件存在则长度清为0，即该文件内容会消失。如果文件不存在则建立该文件。
"a"：以追加的方式打开文件，如果文件不存在，那么创建该文件，如果文件存在，写入的数据将追加到文件的末尾。
"r+"：以读/写方式打开文件，文件必须存在。
"w+"：以读/写方式打开文件，如果文件存在则长度清为0，即该文件内容会消失。如果文件不存在则建立该文件。
"a+"：以读/追加方式打开文件，如果文件不存在，那么创建该文件，如果文件存在，写入的数据将追加到文件的末尾。


## 常见API

```c
// cache指针 单次读取的大小int为4,char为1 读取次数 文件描述符
size_t fread (void *__restrict __ptr, size_t __size,size_t __n, FILE *__restrict __stream)
```


## 例子
### 读操作

```c
const char *FILE_NAME = "test.txt";
void CommonFileOperation(){
  FILE * fd = fopen(FILE_NAME , "r+");
  if(fd == NULL){
    printf("open file failed\n");
    return;
  }
  fseek(fd, 10, SEEK_SET);
  char buf[10];
  fread(buf, 1, 10, fd);
  printf("read data is %s\n", buf);

  fseek(fd, 0, SEEK_END);
  int len = ftell(fd);
  printf("file len is %d\n", len);
  
  fseek(fd, 0, SEEK_SET);
  fwrite(buf, 1, 10, fd);
  fclose(fd);
}
```


### 判断是否是文件,还是文件夹

需要借助库 sys/star, 并且这个库在win上无法使用.
```c
int IsFile(const char * __file_name){
  int fd = open(__file_name, O_RDWR);
  if(fd == -1){
    printf("open file failed\n");
    return -1;
  }
  struct stat st;
  stat(__file_name, &st);
  if(S_ISREG(st.st_mode)){
    printf("this is a file\n");
    close(fd);
    return 1;
  }else{
    printf("this is a folder\n");
    close(fd);
    return 0;
  }
} 
```

更加合理的函数应该是这样的. 每次都通过文件名判断也太呆了,因为后续肯定还涉及到对文件的后续操作. 所以还是将函数的职责保持小点比较好.

```c
int IsFile(const int fd){
  struct stat st;
  fstat(fd, &st);
  if(S_ISREG(st.st_mode)){
    return 1;
  }else{
    return 0;
  }
}
```


### 简化繁琐操作

我个人比较懒惰,所以喜欢把很多重复的代码记录下来.

#### 检测文件打开失败

同时利用宏提供更加具体得到报错信息. 
```c
FILE* OpenAndCheck(const char* __file_name,const char* __modes){
  FILE * fd = fopen(__file_name , __modes);
  if(fd == NULL){
    printf("open %s failed\nat %s lines : %d \n",__file_name,__FILE__,__LINE__);
    _exit(1);
  }
  return fd;
}
```

#### 获取文件大小

利用sys/star库.

```c
int FileSize(FILE* __file ){
  int fd = fileno(__file);
  struct stat st;
  fstat(fd, &st);
  return st.st_size;
}

```

因此，再回到“int fd”这个问题，这里的fd其实就是file_struct结构体内那个存放指针数组的下标！！！ 通过下标就可以控制拿到的文件


### FILE 结构体解析

