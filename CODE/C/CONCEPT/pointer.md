---
file-created: Saturday, November ,2023
last-modified: Saturday, November ,2023
---

>[!note] address  == pointer   , it is 4byte in 32bit platform and 8byte in 64platform.  


>[!warning] 小心指针
我们太年轻以至于我们甚至都不知道自己身处危险之中. 
>>[!example]
> ```c
> #include<stdio.h>
> int main(){
>   int a =10;
>   int b = 20;
>   int c = 30;
>   // 看上去是在修改b的值，实际上是修改了其他变量的值
>   *(&b + 1) = 999; 
>   printf("a = %d \t &a = %p\n", a, &a);
>   printf("b = %d \t &b = %p\n", b, &b);
>   printf("c = %d \t &c = %p\n", c, &c);
> }
> ```


>[!fail]  上面这段代码的结果会因为编译器不同产生差异.
> 这件事情是很可怕的,通过对一个变量进行操作,我就可以修改其他变量的值. 


>[!note] 尽管操作系统有一定的安全机制,但我尝试修改内核部分的代码时,通常会引发`segment fault` ,但是如果我的指针恰好落到了某个关键变量的地址上,导致程序崩溃也不是没有可能. 

>[!note] 如果你以后要写C语言,将其作为你的"终身伴侣",请时刻小心. 

> [!warning] 如果你随意起来,就可以写出各种"妖魔鬼怪",静态语法检查只能检查语法错误,无法检查地址错误.
>>[!example]
> ```c
> #include<stdio.h>
> #include<unistd.h>
> #include<malloc.h>
> int main() {
>   char *p =  malloc(10);
>   p = "hello world";
>   printf("p = %s\n", p);
> }
> ```

> [!note] 本来你只申请了10bit的空间用于存储字符数组,结果你一不小心将长度更长字符串拷贝. 这里存在各种安全隐患. 

## 理解指针

>[!faq] 数据是如何存储在计算机上的? 
>其实存储要回答两个问题,1是数据如何存 ,2是存在哪里 



我们不妨大胆假设, 这里将 `1000-1003` 这一块内存空间用于存储 a的值. 
```c
int a = 10 ; 
```

其实有的时候不需要知道是因为我们可以利用 `rsp` `rbp`的值通过一定的计算获取其地址,并不需要"显式"的存储其地址. 