---
file-created: 2023 12 02
last-modified: 2023 12 02
---

[[logical operation]]

>[!v] 可以将逻辑运算看作只有一位的位运算? 

##  table of content

按位与（&）：如果两个位都为 1，则结果为 1，否则为 0。
按位或（|）：如果两个位中至少有一个为 1，则结果为 1，否则为 0。
按位异或（^）：如果两个位不同，则结果为 1，否则为 0。
按位取反（~）：每个位都取反。

移动都会用 0 今天填充
左移（<<）：每个位都向左移动指定的位数。
右移（>>）：每个位都向右移动指定的位数。


````col
```col-md
flexGrow=1
===
>[!note] `<<` 


```
```col-md
flexGrow=1
===
>[!note] `>>`
```
````

## Usage 

>[!warning] 是否该使用位运算 
>1. 可读性, 你写的代码, 其他人是否可以看懂? 他们是否了解复杂的位运算
>2. 性能, 位运算比较底层, 相当于人为做了一次优化,是否比常规写法性能好 

>[!missing] 自作聪明 
>对于C语言,很多时候其实编译器已经做了非常多的优化了,你自己做的优化可能会出现三种情况,第一是确实获得了一定的性能提升,但是降低了可读性, 第二种是降低了可读性,性能是一致的,最后还有一种可能,也是最为痛苦的,就是既没有提高性能同时可读性还变差了. 
>

>[!tip] 谨慎的人才有可能获得奖励
>建议将每一个位运算都通过汇编检验. [[Local Compiler Explorer]]

```c
#include <math.h>
#include <stdio.h>
int main() {
  // 1.快速平方 或者开方
  int i = 1;
  int a = i<<10; // 2^10 = 1024
  printf("a = %d\n", a);
  int base = 2;
  int b = pow(base, 10);
  printf("b = %d\n", b);
}

```



快速平方计算

>[!note ] 交换两个数的值
>利用两次异或可以得到原始值的方式. 不过像[[CODE/PYTHON/python]] 提供了交换运算的语法糖. 

```python
a , b = 5, 10 
# 交换 
a = a^b
b = a^b
a = a^b
a , b= b , a
print(a,b)
```



>[!note] 位操作判断奇偶数
只需要判断最后一位是0还是1就可以知道其奇偶性. 
>>[!example]-
> > `````col
> > ````col-md
> > flexGrow=1
> > ===
> > ```python
> > a = 12
> > if a & 1: 
> >     print("奇数")
> > ```
> > ````
> > ````col-md
> > flexGrow=1
> > ===
> > ```python
> > a = 11
> > if a & 1: 
> >     print("奇数")
> > ```
> > ````
> > `````



### 位运算妙解大小写字符转换

>正常解法 , 先判断一个字符是否是大写,如果是就进行转换. 

```python
a = 'a'
A = "A"

print(chr(ord("j")&95))
print(chr(ord("M")&95))
```

![[bitwise operation-20231202193127192.webp|448]]

原理解释一下, 为什么我们的 `A` 是 65 , `a` 是97呢? 并且它们两个相隔32呢? 
其实从二进制角度来看就好理解了 
```txt
64 0b100 0000   
65 0b100 0001 
97 0b110 0001 
```

发现了没有, 大小写的区别就变成了 第6位数字是0还是1的区别了.

