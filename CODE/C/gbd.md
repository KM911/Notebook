---
file-created: Thursday, November ,2023
last-modified: Saturday, November ,2023
---

````col
```col-md
flexGrow=1
===
> [!note] 定义
>  debug工具


> [!tip] 相关概念
> pdb 
```
```col-md
flexGrow=1
===
> [!info] 别称
> The GNU Project Debugger 

> [!cite]- 参考资料
> [GDB office site](https://www.sourceware.org/gdb/)
```
````
## 没有必要直接只用gdb 

我们应该使用IDE给我们提供的调试功能,而不是自己手动gdb. 这样你会"舒服"很多,"舒服"是很重要的.

我们的IDE的调试功能,其实就是在调用各种 xdb debugger , 加上gdb是最常见的调试器,所以还是有必要学习的 

IDE 提供的功能非常好,将当前函数调用栈中全部的变量都显示出来了,我们不必手动查看这些变量的值.我们可以下一步(next),进入函数(step ),跳转到到下一个断点(continue) ,但是如果我们想要做一些"骚操作" ,可能就需要借助gdb的命令了.   

![[Pasted image 20231025153915.webp]]


## gdb 作用




### 指令 

指令非常多,多到我都不知道没有人知晓全部的命令. 正确的做法是,"管中窥豹". 

| COMMAND      | USEAGE         |
| ------------ | -------------- |
| info threads | 查看全部的线程 |
| t tid        | 切换线程       |
|              |                |


### 调试多线程 

1. 设置多线程锁模式
`set schedule-locking [mode]`
* off 不锁定任何线程,所有线程都可以执行
* on  只有当前线程可以执行 其他线程会暂停
* step 

2. 设置断点 
3. 线程切换 

基于上面的操作, 我们就可以单步执行一个线程,控制最终的执行结果.
