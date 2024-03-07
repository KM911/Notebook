
## python关于global的笑话 

 >[!exp] 可以在函数内部修改外部的list,但是无法修改int. 
> ```python
> a =10
> ls = [0]
> def Test():
>     a = 20
>     ls.append("hello")
> Test()
> print(a,ls)
> ```
> 

 >[!exp] 如果想要修改a的值,必须申明global
> ```python
> a =10
> ls = [0]
> def Test():
>     global a
>     a = 20
>     ls.append("hello")
> Test()
> print(a,ls)
> ```
> 

>[!error] 其实这里很多人会认为是,python会自动将list等引用类型添加上global关键字,其实是错误的.

>[!tip] 因为a和ls都是全局变量,只是因为python无法区分 `a = 20` 究竟是想要将全局a赋值为20,还是想要在函数内部进行申明与赋值,在不使用global关键字的情况下,python选择了后者,所以就有了 shadowing,导致看上去好像无法修改外部的数值类型变量

>[!exp] c语言中就没有这个问题,因为c语言可以区分declaration和 assignment. 
> ```c
int a = 10;
void add() { a++; }
int main() {
  add();
  printf("a = %d", a);
}
> ```
> 我们这里就是在对全局变量a进行赋值,没有任何问题. 

