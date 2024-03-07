
>[!note] What we should know
>1.lexical scope 
>2.function lexical scope 
>3.function body is not evaluated until the function is called 
>4.function body is evaluateded every time the function is called
>5. A variable binding evaluate its expression when the binding is evaluate , not every time the variable is used. 

>[!faq] what is closure ? 
>A closure is a function that has access to variables in its outer (enclosing) function's scope, even after the outer function has returned



>[!faq] function could be a value ? 



In this case , the `hello_func` == `Hello` . it look like you just give a alias to Hello function. That was easy to under stand. 

you could see function name is special rip regs value , () is a operate that go to rip . 
`````col
````col-md
flexGrow=1
===
```c
void Hello(){
    printf("Hello World!\n");
}
int main() {
    void (*hello_func)() = Hello;
    hello_func();
    Hello();
    return 0;
}

```
````
````col-md
flexGrow=1
===
```go
func Hello() {
	fmt.Println("Hello World")
}
func main() {
	hello_func := Hello
	hello_func()

}

```
````
`````

you could see hello_func as the same Hello 

 c语言的函数指针并不是闭包，JavaScript的函数对象才是闭包



```go
package main 
  
import "fmt"
  
// newCounter function to  
// isolate global variable 
func newCounter() func() int { 
    GFG := 0 
    return func() int { 
      GFG += 1 
      return GFG 
  } 
} 
func main() { 
    // newCounter function is 
    // assigned to a variable 
    counter := newCounter() 
  
    // invoke counter 
    fmt.Println(counter()) 
    // invoke counter 
    fmt.Println(counter()) 
} 

```


还有一个问题没有解决,你的作用是什么? 其实就是为了 屏蔽具体的实现内容,不是吗? 

1.保护变量 

我想知道一个函数的执行次数,并且该函数在不同的执行次数会有不同的执行模式. 


>[!example] helloFunction 执行n次后将会执行不同的逻辑
> 这里的pc和limit都是在FunctionBuilder内部的变量,所以我们无法在外部访问,就可以确保不会被修改,结果一定是正确的,如果利用全局变量就可能出现问题. 
> ```go 
> import "fmt"
> 
> 
> func FunctionBuilder(n int) func() string {
> 	pc := -1
> 	limit := n
> 	return func() string {
> 		pc += 1
> 		switch {
> 		case pc < limit:
> 			return "Hello"
> 		default:
> 			return "World"
> 		}
> 	}
> }
> func main() {
> 	helloFunction := FunctionBuilder(3)
> 	for i := 0; i < 5; i++ {
> 		fmt.Println(helloFunction())
> 	}
> }
> 
> ```


如果从这个角度来看,闭包好像还挺简单的,只是一个trick罢了