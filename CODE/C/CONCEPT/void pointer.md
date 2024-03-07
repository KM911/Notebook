---
file-created: Saturday, November ,2023
last-modified: Saturday, November ,2023
---

````col
```col-md
flexGrow=1
===
> [!note] 定义
>  a pointer which has no associate any data type with it 


> [!tip] 相关概念
> [[pointer]]
```
```col-md
flexGrow=1
===
> [!cite]- 参考资料


> [!error]
> java中也有空指针,但是意义完全不一样了,java的指针操作可以忽略不计,更多的时候是找不到对象报的错
```
````

换言之, 因为没有和任何数据类型绑定 , 它可以是任何类型,或者被 typecasted into any data type

下面的代码完全可以正常运行,并且输出 `hello world` , 因为 P只是一个单纯的指针, 和其他任何数据类型的指针都是一样的,都是 32/64位. 
```c
int main(){
  void * p;
  p = "hello world";
  printf("%s",p);
}
```

所以当我们看到一个void pointer的时候,其实可以表示任何数据类型,或者或你可以用其

```c

```
## Not allowed

You can not dereference a void point . 

这很好理解, 因为`void pointer`没有和任何数据类型 `associate` 所以你也没有办法根据地址解析其值,因为它可能是 `int` 也可能是 `char*` . 不过只要你手动说明它的类型不就好了? 

```c    
int a = 10;
void *p = &a; 
a = *p + 2;   // not allowed
a = *(int*)p + 2;  // allowed
```
这里我们说明p是一个`int*`的指针,其实就是告诉CPU从p的位置取4个byte的数据然后加2. 

## pointer of void pointer 

第一次看见是在`int pthread_join(pthread_t __th, void **__thread_return)` , 我没有理解为什么参数是二级指针,太难看了. 

其实解释的话,就是说