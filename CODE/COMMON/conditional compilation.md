
>[!faq] 背景
>跨平台: 相同的功能在不同的平台比如win和linux上可能需要使用不同的代码,我们该如何在不损失效率的前提下进行开发.



## 这里应该给出一个非常好的实践的例子 而不是讲这些空洞的内容 不是吗 

## 条件
* debug
* release
完全相同的逻辑结构,前者会输出提示信息,后者不会.

* linxu
* windows
部分算法在不同操作系统中需要不同的实现方式,或者是需要调用不同syscall,这里就需要我们分别编写两端代码了.
但是其实大部分的都是比较重复性的工作不是吗 ?


## go
一共有两种方法实现条件编译

````col
在文件的首行添加注释,然后编译的时 go build -tags
//go:build condition
//

类似于xxx_test.go,编写xxx_windows.go,xxx_linxu.go
编译器会自动选择当前操作系统后缀的文件进行编译并忽略其他后缀的文件.
````

### 例子

````col
```go
// hello_linux.go
func Hello(){ print("hello,linux.")}
```

```go
// hello_windows.go
func Hello(){ print("hello,windows.")}
```


```go
// main.go
func main(){ Hello() }
```
````

这样就可以在不同的操作系统中有不同的功能了,就是有一点点繁琐,一次需要创建多个文件.


## C/C++

C/C++的条件编译其实是条件宏,也就是满足条件就会有这个宏. 
相比之下,C的条件编译就更加灵活,可以在一个文件中添加多个条件.

这个功能是编译器提供的,所以编译器也会提供一些特别的宏. 

```c

```