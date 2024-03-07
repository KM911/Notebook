---
date created: Friday, November 24th 2023, 4:58:47 pm
date modified: Saturday, November 25th 2023, 8:57:37 am
file-created: 2023 11 25
last-modified: 2023 12 01
---

## Dynamic/Static Link 

> [!note] C语言有一点非常呆. 

>[!example] 不进行任何的引入,只是将两个目标文件进行链接,同样可以编译成功. 
>
> `````col
> ````col-md
> flexGrow=1
> ===
> ```c
> // main.c
> int main(){
>     Hello();
> }
> 
> ```
> ````
> ````col-md
> flexGrow=1
> ===
> ```c
> ```c
> // any c file
> #include<stdio.h>
> void Hello(){
>     printf("hello wrold");
> }
> ```
> ````
> `````

>[!warning] 缺少了函数声明就缺少了函数定义,就无法获取语法提示. 
>Note that implicit declarations only works in  C89 . 


>[!note] 创建共享库
> ```bash
> -Iinclude -fPIC -shared -o 
> ```


> [!note] 关键编译参数 `-static` 开启静态链接,不再利用 `openat` 和 `mmap` 来读取.
> 



| 操作方式                                       | 文件大小 | Strace |
| ---------------------------------------------- | -------- | ------ |
| `gcc main.o share.o -static -o static`         | 874.7 KB |        |
| `gcc main.o share.o -o dynamic`                | 19.5 KB  |        |
| `gcc main.o share.so -o shared`                | 17.7 KB  |        |
| `gcc main.o share.so -static -o shared-static` | 872.9 KB |        |


>[!note] 采用静态链接的`strace` 内容少很多是因为,不再需要去读取`ld.so.cache` 然后加载其他库.
>我们可以看到只要是使用动态链接的方式,磁盘占用就比较少,因为依赖`libc` 如果你电脑缺少了`libc` 就无法允许. 
>

>[!error]- 错误的分享方式
>我曾经就将我的动态链接的程序分享给其他人,可想而知,这个程序是无法运行.最令人难过地难道不是班级里没有一个人告诉你吗? 




> [!note] 核心指令
> 该指令用于加载`libc.so` ,只要是动态链接的程序都有. 
> `openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3`


动态链接 和 动态链接共享库这里是一件事情还是两件事情, 其实这里是
>[!done] 动态链接的优点
>1.减少编译后文件的体积,因为很多函数的定义都在共享库中. 

> [!faq]- 动态链接就一定共享吗?
>>[!example] `Electron` 
>>因为缺少软件运行所需的动态库, 软件是无法运行的,所以为了确保软件可以运行,大部分的软件都会选择在打包时将自身需要的环境与软件一起分发. 不过也造就了今天 `Electron` 软件会在你的电脑上 安装各个版本的 `vulkan-1.dll` `ffmpeg.dll`
>有办法可以环境今天这种版本乱象吗? 我不知道. 



>[!note] 对于我们自己创建的`.so` 文件,被动态链接后将会有如下的指令
>` `

- [ ] 你不应该修改一个`.so` 文件的位置,这很好理解. 

>[!note] 目前的信息
>1.gcc 在编译的时候,会自动将 `.so`文件视为库文件,将会前往可能的共享库一个个寻找,建议手动声明其绝对路径以减少误判. 
>2.可以利用`.so`的更新来实现更新,这个真的算热更新了,不是吗? 


>[!error]-  当找不到一个`.so` 文件时 `gcc`会尝试遍历全局共享库
>```c
>openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/x86_64/x86_64/share.so", O_RDONLY|O_CLOEXEC) = -1 ENOEN
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/x86_64/share.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No s
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/x86_64/share.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No s
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/share.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such fil
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/x86_64/x86_64/share.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (N
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/x86_64/share.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such
>```

>[!tip] 总结
>动态链接可以减少磁盘占用,提高程序的运行效率(mmap). 坏处就是对于环境存在依赖. 静态与之相反. 
>我们可以将自己编写的函数放到`lib`中,然后利用绝对路径将其应用,可以减少程序的体积. 


>[!faq] 我认为动态共享库只有操作系统和底层软件开发者需要深入了解. 
>普通的软件开发人员很难让自己的多个软件共享一个库并且都被用户所安装,大部分的软件即使使用了动态共享库,也还是放在软件安装目录下供自己使用. 最为典型的就是 `electron`的滥用,大量程序将 `chromium` 打包到他们的程序中,侵占了大量的磁盘空间. 只能说,现在的硬件能力比较好,这要是在以前肯定是会被淘汰的. 

