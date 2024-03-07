---
file-created: 2023 11 25
last-modified: 2023 12 02
---


>[!faq] verbose code 
>Sometimes, we may need to write a lot verbose code , like exchange value of two variables. Even you could use `Ctrl C+V` , it still is very verbose. We need some thing to help us do the same thing.

>[!tip] Function
>In math , function is a special mapping , a special input and return a output. 

>[!tip] In programming 
> function is a set of operation. 
> In Some case , you could treat it as copy/paste code.  

>[!example] Cpp
>```cpp
>void Swap(int &a, int &b) {
  int temp = a;
  a = b;
  b = temp;
}
int main( ){
  int a = 1, b = 2;
  Swap(a, b);
  printf("a = %d, b = %d\n", a, b);
}
>```


## Why Function is reusable ? 

>[!note] encapsulate 
>Instead of repeatedly writing the same code, you can encapsulate that code into a function and call it whenever you need to perform the task

>[!faq] Why function is reusable ? 
>Maybe it just copy/paste . Just like you write verbose code . 

>[!tip]  Interesting discoveries
>Your thoughtful analysis has led to some interesting discoveries, including the concept of inline functions. Inline functions act as code replacements, seamlessly integrating the function's code into the location where it's called. Now, let's delve into the common function call process.

>[!note] line and common function
>common function 


>[!exp] Code Example
>```c
>void hello(char* msg){printf("%s",msg);}
>int main(){
>    hello("hello");
>    hello(" world");
>}
>```



## hello world 调用过程

让我们查看一个最简单的C语言的函数调用过程.
```c
int main(){
    
}
```



![[Pasted image 20231027093027.webp]]




gdb 调试的时候,寄存器中的值都是物理地址,现在我们是真正的上帝视角了 哈哈哈. 错误的,还是虚拟地址,其实就算是虚拟地址,也不太全部是虚拟的, 理解又错了. 哎 .

恩，是这样的，编译器可以确定我们所需的段描述符，以及段内偏移，具体物理地址由OS处理。

具体这个指令放在哪，要由这个相对地址+内核基地址算出来。
内核基地址是内核放置的物理初始地址。

其他地址。我默默的看看intel386手册再来讨论吧。我不理解这些概念。。


物理地址
0x00000000 到 0x0fffffff
对应虚拟地址
0xf0000000 到 0xffffffff

还是有不少收获的, 更好地理解了我们的函数调用过程, 希望对我们以后可以有更多的帮助,这个
