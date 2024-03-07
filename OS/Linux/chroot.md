
>[!faq] 



>[!desc] chroot
>chroot is an operation on Unix and Unix-like operating systems that changes the apparent root directory for the current running process and its children

## [[Read Eval Print Loop]]

>[!note] 一种状态机 
>读取用户输入,执行,打印输出结果,并循环. 

>[!example]- go语言实现
> ```go
> func main() {
> 	for{
> 		print("please tell me your name : ")
> 		var input string
> 		_, err := fmt.Scan(&input)
> 		if err != nil {
> 			fmt.Println("scan",err)
> 			return
> 		}
> 		println("hello",input,"!")
> 	}
> }
> ```

>[!note]- 效果如下
>不过如果你输入内容存在空格就会有一些显示问题. 


![[Pasted image 20231123103735.webp]]

## 模拟shell

>[!note] 我们上面的程序已经有一些shell的影子了,我们现在尝试进一步优化上述代码,使其更加接近shell. 
>我们打算实现以下几个命令 : ls pwd touch exit rm




## stdin stdout stderr

> [!note] [[everything is file]]  
> Linux做了一个抽象,任何程序的输出,都是向一个名为 `stdout` 的文件中写入内容. 

> [!note]- 重定向
> command > file 将stdout重定向到file, "w"模式
> command >> file "a"模式 
> command 2> file 将 stderr重定向到file, "w"
> command 2>> file "a"
> command &>> file 将stdout和stderr都定向到file中,"a"


### read user input

>[!note] scanf的本质其实就是重stdin中读取内容. 

> [!v] 实现了目录级别的资源隔离,有什么意义?
> 因为根目录已经被修改了,所以程序的执行就变得完全不一样了. 
> 还有网络请求会怎么样呢? 
> 我们可以创建软连接来实现复用已有的liunx环境吗?
## cgroup

>[!note] 我们利用chroot已经修改了当前的程序的执行环境


