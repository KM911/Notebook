
## 项目的意义 

>[!tip]  灵感来自于redis作者的项目  
>可以帮助你真正了解io多路复用. linux的抽象中, 万物皆文件, 其实io多路复用最常见的场景就是各种server,你有100个客户的请求需要处理.



### 粘包问题 

>[!faq] 粘包
>tcp协议是面向流的协议,向一个连接中发送两次消息. 消息的接收方可能会将两次消息合并作为一个消息处理. 

>[!test]- 粘包复现 
>server端代码
>```go
> func TCPServerStart() {
> 	tcpAddr, err := net.ResolveTCPAddr("tcp", "localhost:8080")
> 	util.Must(err)
> 	listener, err := net.ListenTCP("tcp", tcpAddr)
> 	util.Must(err)
> 	conn, err := listener.Accept()
> 	util.Must(err)
> 	time.Sleep(2 * time.Second)
> 	buffer := make([]byte, 1024)
> 	n, err := conn.Read(buffer)
> 	util.Must(err)
> 	fmt.Println("received:", string(buffer[:n]))
> }
>```
>client端代码
>```go
> func TCPClientStart() {
> 	conn, err := net.Dial("tcp", "localhost:8080")
> 	util.Must(err)
> 	_, err = conn.Write([]byte("Hello, server!"))
> 	util.Must(err)
> 	_, err = conn.Write([]byte("Hello, server!"))
> 	util.Must(err)
> 	time.Sleep(5 * time.Second)
> }
>```
>>[!tip] 1.客户端发送了2个"包"/消息 2. 服务端接受"包"/消息 并不及时 
>运行结果
>>received: Hello, server!Hello, server!


>[!done] 解决方式 
>这不是传输层的问题,应该在应用层协议设计时设置相关字段定义"包"的长度. 

>[!exp] http协议的header中有一个content-length字段用于表示body的长度. 


## 多个TCP连接的管理 

>[!faq] 我们现在有10个tcp连接. 假设用一个 `map[stroing]net.Conn` 来存储, 我们现在需要监听全部的连接, 该采取何种策略? 

### for 遍历 

>[!note] 我们遍历map,如果该conn有消息我们就将其处理 

>[!lab] 
> ```go
>func HandleMessage() {
>	for {
>		for _, conn := range ConnectionPool {
>			n, _ := conn.read(buffer)
>			fmt.Println(string(buffer[:n]))
>		}
>	}
>}
> ```

 首先这是一个单线程程序,当某一个conn阻塞时,其余全部的连接都需要等待. 
 其次,你会发现,这里对于顺序具有强一致性,也就是必须是按照ABC的顺序来收发消息.

综上,你会发现这个代码根本就用不了. 

### 多线程模型 

>[!faq] 我们为每一个fd都创建一个线程,这样就好了不是吗? 

>[!thought] 假如我们有1024个用户,创建1024个线程,每个线程都有独立的栈(查询可得8MB),1024个线程就是8G的内存开销,并且随着用户数量增多,内存占用还会进一步加剧
>```bash
>ulimit -a | grep "stack" 
>```
>于此同时,创建如此多的线程还会增加操作系统调度的负担,进一步拖慢系统的执行. 

>[!tip] 综上, 我们不可能为每一个fd都创建一个线程,

>[!v] 一种可能的优化方式
>协程的资源开销更小,例如goroutine只的栈只有2-8KB,创建同样数量的goroutine只需要2-8MB,几乎不值得一提了. 
>在64位机器上,8G内存,基本上根本就不用担心数量的问题. 

>[!lab] goroutine最大数量
>我测试出来的最大数量是1048576 也就是100万,但是我使用这个方法测试时,就不会报错了,程序可以一直运行下去,除非我手动将其关闭. 
>暂且认为goroutine的最大数量是无限的吧


>[!key] 我们需要让单线程程序可以监听多个fd,多路复用技术就此诞生
>多路复用的前提是操作系统支持,我们常见的select,epoll都是linux的多路复用syscall,至于windows的多路复用技术是什么,我不太了解,但是可以肯定的是,windows一定也实现了多路复用. 


### select [Linux select() - Synchronous I/O Multiplexing](https://phoenixnap.com/kb/linux-select)

```c
#include <sys/select.h>

int select (int nfds, fd_set *readfds, fd_set *writefds,
            fd_set *exceptfds, struct timeval *timeout);
```

实际上,我们说得select其实是pselect, select的返回结果可能是fd或者是超时的错误 ( res == -1)

可以使用pselect,其会一直等待. 


### poll

基本上和select 累世 



### epoll



