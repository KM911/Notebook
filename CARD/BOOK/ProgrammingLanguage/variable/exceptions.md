
>[!faq] 如果代码的执行出现了异常,该如何表示呢? 



C语言中就没有专门为 `exception` 创建一类专门的变量 和 其相关的语法. 而是使用基本类型来实现类似的功能. 

比如 打开文件时如果文件文件不存在返回NULL. 

```c
    const char* filename = "main.c";
    FILE* fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Error: Could not open file %s\n", filename);
        exit(1);
    }
```

python则是内置了很多 异常类型
## 错误处理 python 为例 

### raise exception

> [!exp] 数组越界 
> 这是一种可能的实现 : 每次用索引获取数组的值前都进行判断是否越界了. 
> ```python
> def List(n):
>   __inner_list__ = [ i for i in range(n) ]
> 
>   def get(index): 
>     if index >= len(__inner_list__):
>       raise IndexError("Index out of range")
>     return __inner_list__[index]
>   return get
> 
> ls = List(10)
> print(ls(10))
> print("hello world")
> ```

>[!note] 程序在执行 ls(10)时抛出了异常,程序直接终止了,导致最后的`hello world` 没有被输出 
 
### handle exception

>[!others] 有了异常 就 肯定有异常处理 不然直接退出程序 为什么不使用exit呢? 

> [!exp] 数组越界(错误处理版)
> ```python
> def List(n):
>     __inner_list__ = [i for i in range(n)]
> 
>     def get(index):
>         if index >= len(__inner_list__):
>             raise IndexError("Index out of range")
>         return __inner_list__[index]
>     return get
> 
> 
> ls = List(10)
> try:
>     print(ls(10))
> except IndexError as e:
>     print(e)
> 
> print("hello world")
> ```
> 

>[!note] 使用了`try` 成功捕获异常,程序不会终止,可以继续运行 







>[!note] 不要指望错误处理可以解决一切问题
>很多时候你的错误处理只是为了不让程序中途退出. 

