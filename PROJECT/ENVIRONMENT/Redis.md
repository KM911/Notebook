---
title: redis
mathjax: false
date: 2023-04-28 18:31:04
tags:
categories:
---

## redis安装

像这样的常用服务端软件,一般的包管理工具都会提供.其实不必太担心.

```
yum -y install redis
```

错误的,如今已经2024年了,你应该需要学会使用docker来安装各种软件了,redis:alpine 只有50MB,其资源占用可以忽略不记,我只能说完美. 

如果不考虑相关的配置,你可以非常快速地启动你的项目. 




## 启动redis

```shell
redis-server config
```

这里我们编写一个就是systemctl

```
[Unit]
Description=Redis
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/bin/redis-server /etc/redis/redis.conf
ExecReload=/usr/local/bin/redis-server -s reload
ExecStop=/usr/local/bin/redis-server -s stop
PrivateTmp=true

[Install]
WantedBy=multi-user.target
                                       
```

```
[vagrant@xf-dev ~]sudo vim /usr/lib/systemd/system/redis.service
[Unit]
Description=The redis-server Process Manager
After=syslog.target network.target

[Service]
Type=forking
PIDFile=/var/run/redis_6379.pid
ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/etc/redis.conf
ExecReload=/bin/kill -USR2 $MAINPID
ExecStop=/bin/kill -SIGINT $MAINPID

[Install]
WantedBy=multi-user.target
```



## 最简配置

```
requirepass 123456
bind 0.0.0.0
daemonize yes
databases 1

dbfilename database.rdb
dir /root/redis/data
rdbcompression yes
logfile /root/redis/log
```


### redis 持久化

redis将自己的数据复制一份保存到磁盘中,下次启动会自动加载 

- ### RDB 

- ### AOF持久化
#### AOF
AOF 持久化策略就是 将Redis服务器执行的每一条写命令都记录到一个文本文件中，这个文本文件就是一个追加文件（ append only file ）

AOF有三种持久化策略，也就是刷盘策略。可以根据不同的场景使用不同的刷盘策略。

然而随着时间的推移，AOF文件也会越来越大，因为它记录了所有的写命令。这样会导致AOF文件占用过多的磁盘空间，以及恢复数据的时间过长。为了解决这个问题，Redis提供了AOF重写机制，来压缩和优化AOF文件。

这里插一嘴
#### Redis 是单线程吗

常说的单线程是指 「接收客户端请求->解析请求 ->进行数据读写等操作->发送数据给客户端」
这个过程是单线程的，由主线程来完成

怎么感觉和 Node. js 单线程的解释 十分类似

但是这个Redis 程序并不是单线程的，它还是会启动后台进程来处理一些事情的
就比如 关闭文件和 <span style="color:gold"> AOF 扫盘</span>





- 混合持久化

平常使用AOF进行持久化 




### 内存回收机制  内存淘汰机制

当我们的内存使用到达上限了,我们就需要进行回收.这里是决定如何进行回收的地方.

* LUR Least Used Resently
* LFU  Least Frequent Used



![image-20230430094151976](http://81.68.91.70/pg/image/KMFuvZRwoNKj.webp)

![image-20230430094012193](http://81.68.91.70/pg/image/KMx0R6VrF4mZ.png)



