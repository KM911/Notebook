---
file-created: 2023 11 15
last-modified: 2023 11 29
---

[https://www.cloudflare.com/learning/dns/what-is-dns/](https://www.cloudflare.com/learning/dns/what-is-dns/)

>[!abstract]
>The Domain Name System (DNS) is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names to IP addresses so browsers can load Internet resources.

> 不是给人用的协议,是给其他IP协议提供适用地. 

我几乎从来没有想过这个问题

| Domain         | IP              |
| -------------- | --------------- |
| www.google.com | xxx.xxx.xxx.123 |
| www.xxx.edu    | xxx.xxx.xxx.111 |
|                |                 |


load blance 



> 分层的,基于
UDP 53端口

1. DNS的查询方式
递归和迭代两种方式. 


## DSN域名结构 
层次树状结构. 

顶级域名 
.com .edu .gov .int
国家域名 
.cn .us 

这里反而需要倒着来看. 

一共全球13个根服务器, 避免一个挂了,但是没有任何的作用. 

但是其实我们基本上就是在叶子节点就好了. 

robot.cs.edu.cn
从叶子到根

DHCP. 
local name server , 自动配置和手动配置. 
ISP是什么
手动设置DNS,default gateway , 

local name server 
1. cache 
2. 递归查询 . 向下查询. cn --> edu --> ustc 
3. 迭代查询.  LNS 向各个DNS请求. 

### DSN协议报文格式 

这里看RFC就好了不是吗? 

新增一个域 , 


## DNS作用 

从 域名 到IP的解析


## process 

1. check local name server ? 
2. check local hosts files

[[hosts]]