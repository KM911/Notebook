
| 常用命令 | 作用 |
| ---- | ---- |
| docker run -it image | 进入一个镜像 |
| docker build -t name:version .  | 根据当前路径的Dokcerfile 构建image |
|  |  |




| flag | useage |
| ---- | ---- |
| -it |  |
| -p outer : inner |  |
| -rm | auto clean container |
| -d | background  |


多镜像构建环节, 



## A类地址 

最初用于将网络分层的,我们并不需要了解其作用,只是你看到下面的ip时应该要知道这是内网ip. 

A类地址：10.0.0.0～10.255.255.255

B类地址：172.16.0.0～172.31.255.255

C类地址：192.168.0.0～192.168.255.255 常见的路由器分配的ip地址