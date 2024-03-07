


当你使用python进入交互时, 你会发现你不会退出python, python还是会继续给出信息.

win会发送一个`interpret` 信号,如果没有被接受处理,就会将程序关闭. 

下面这个程序将会接受一切的信号,你将无法使用CTRL + C的方式将其关闭. 可以通过任务管理器将其关闭,或者是将终端关闭. 
```go
func main() {
	for {
		//interrupt
		c := make(chan os.Signal)
		signal.Notify(c)
		fmt.Println("start..")
		s := <-c
		fmt.Println("End...", s)
	}
}
```

假如你不希望自己的程序被CTRL+C直接关闭,可以使用如下方法.

```go
func DisableInterpret() {
	//	如果有ctrl + c 信号，就会触发
	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt, os.Kill)
	for {
		<-c
	}
}
func main(){
    go DisableInterpret()
    // Your process
}
```

对于大部分程序,你可以将 CTRL＋Ｃ视作强制关闭.  下面是一个死循环被CTRL + C终止的例子.

```c
#include<stdio.h>
int main(){
  for(;;){}
}
```
### 信号

在win上, CTRL+C会发送 `interpret` 中断, 如果没有被处理就会将该程序关闭. 

我们尝试利用PID向目标程序发送信号. 

我不能理解的地方在于,每一次中断信号来了,都会执行`thread exit` 和 `thread create` 这个模型也太捞了吧.

>[!test] taskkill 和 kill
>win使用 `taskkill` 杀死程序 关闭chrome
>```powershell
>taskkill /F /IM chrome.exe 
>```


