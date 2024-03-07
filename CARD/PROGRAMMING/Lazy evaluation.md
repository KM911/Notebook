---
file-created: 2023 11 15
last-modified: 2023 11 29
---


或许 惰性函数 惰性求值 都是一个东西. 

[惰性求值 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E6%83%B0%E6%80%A7%E6%B1%82%E5%80%BC)

>[!abstract] 核心
>不直接进行 "计算",而是在需要时计算. 
>在运行时根据条件,生成不同类型的函数,从而实现兼容性和性能的提升. 


````col
```col-md
flexGrow=1
===
>[!done] 好处
>确实可以提高程序的运行销量 
```
```col-md
flexGrow=1
===
>[!error] 坏处
>带来的开发时间增加和函数破碎化. 
```
````



>[!example] js实现 在函数内部修改该函数的内容
> ```js
> let flag = 10
> function OS() {
>   console.log("OS check")
>   if (flag==10){
>     OS = function () {
>       return "Windows"
>     }
>     return "Windows"
>   }else{
>     OS = function () {
>       return "Mflagc"
>     }
>     return "Mflagc"
>   }
> }
> 
> console.log(OS())
> console.log(OS())
> ```



我们直接重写我们的OS函数了,只有在第一次执行的时候会进行条件判断,后续都不会进行该操作了. 

## 通用性实现

函数的名字其实只是为了说明call的对象,你只要修改call的对象就好了. 有的编程语言无法直接修改该函数的类型/内容,但是可以利用其返回一个函数指针就好了. 



## python实现

利用lambda返回一个匿名函数.  虽然无法在一个函数内部去修改自己,不过如果这样的化就可以了. 
```python
import os 

def Hello():
    if os.path.exists("review"):
      return lambda : print("Hello, review!")
    else:
       return lambda : print("Hello, world!")
    
  
if __name__ == "__main__":
    ls = Hello()
    ls()
    ls()

```

## go语言实现 

```go
func OS() func() {
	if runtime.GOOS != "windows" {
		return func() {
			println("Windows")
		}
	} else {
		return func() {
			println("Linux")
		}
	}
}

func main() {
	os := OS()
	os()
	os()
}

```
 
 >[!exp] C语言实现 函数指针
> ```c
> void Win(){
>   printf("Windows\n");
> }
> 
> void Linux(){
>   printf("Linux\n");
> }
> 
> // 返回一个函数指针
> void (*getOS())(){
>   int a = 1;
>   if(a == 1){
>     return Win;
>   }else{
>     return Linux;
>   }
> }
> 
> int main(){
>   void (*os)() = getOS();
>   os();
>   os();
>   return 0;
> }
> ```


>[!tip] 好处 
>因为我们只需要执行一次就可以确定当前的执行环境,可以避免重复进行if判断,提高程序的执行效率. 

>[!transfer] 如果一个函数要求在执行n次后改变其执行内容,又该如何操作呢? 

>[!example] python实现(2次后改变函数的执行内容)
>```python
>execute_pc = 0
>
> def ExecuteA():
>   print('ExecuteA')
>   global execute_pc , exe
>   execute_pc +=1
>   if execute_pc >=2 :
>     exe = ExecuteB
> def ExecuteB():
>   print('ExecuteB')
> exe = ExecuteA
> exe()
exe()
exe()
>```


