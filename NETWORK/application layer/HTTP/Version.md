---
file-created: 2023 11 15
last-modified: 2023 11 26
---

> [!abstract] HTTP History
> HTTP 0.9
> HTTP 1.0
> HTTP 1.1

[[计算机大厦不是一天建成的]]


更加深刻理解了 HTTP是基于字节流的协议,我真的太感谢了,果然还是需要去学习这些内容可以让你对于其有更加深入的了解不是吗? 

现在对于你来说,实现http协议这件事情,感觉好像没有那么复杂了. 


>[!note] nc localhost 3000 
GET /hello

>[!note] res
> HTTP/1.1 200 OK
> Server: Fiber_builde_by_km911
> Date: Sun, 26 Nov 2023 09:51:59 GMT
> Content-Type: text/plain; charset=utf-8
> Content-Length: 18
> Vary: Origin
> Access-Control-Allow-Origin:
> Connection: close
> 
>Hello, World 👋!



![ ](https://cdn.xiaolincoding.com/gh/xiaolincoder/ImageHost/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/%E9%94%AE%E5%85%A5%E7%BD%91%E5%9D%80%E8%BF%87%E7%A8%8B/4.jpg)



## MTU是1500,我们的TCP可以写更多的内容吗? 

其实是可以的,你直接开写就好了

自作聪明的你啊, 比如说


直接将大文件写入是快的. 

