
## /bin/sh: ./main: not found

>[!faq] 问题原因 
>其实是报错信息 程序无法执行 异常抛出的结果让我有些不太好接受就是说. 

>[!others] alpine为了减少体积,采用的是musl进行静态编译,所以没有glic组件,缺少例如ld.so等导致无法进行动态链接

>[!done] 解决方式 
>进行 [Static Link](Static_Link.md) 并检查是否是 ELF格式

>[!warning] go语言中如果使用cgo的部分也应该进行静态编译,不然默认会使用动态链接glibc
>使用
>

```c
go-hell0: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, Go BuildID=83JaOF168cFwEoj
FfJOG/qLAG4OqF3I8rv8ZUVgUe/OPzNw0mN6xflivnVjS0J/_jzUNfakBUgtV4uUJ6f_, not stripped
```

```c
a.out: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, BuildID[sha1]=9c9f84bb1c
9efa621f112cee19f2ab6692804e81, for GNU/Linux 3.2.0, not stripped
```


>[!others] 参考资料
>[Promacanthus](https://promacanthus.netlify.app/experience/golang/01-%E7%BC%96%E8%AF%91%E7%9A%84%E5%9D%91/)

