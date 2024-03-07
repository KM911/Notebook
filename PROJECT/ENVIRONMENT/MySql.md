---
title: mysql环境搭建
date: 2023-03-12 14:17:43
tags:
categories:
file-created: 2023 11 21
last-modified: 2023 11 28
---

## MySql 环境搭建

我不想花费很多的精力在这种事情上了 这是运维的事情 我们的重点应该是对于数据库的性能负责就是.

不过确实吧, 我花了一年的时间都没有找那么几天的时间去把mysql相关的重要指令,比如创建新用户,给新用户设置权限,设置是否运行远程登陆,这些都没有做,我只能说你的水平就是只有这么点了,自己部署都不能做得很好. 

## 安装 

如果是你自己使用,那么我推荐你使用[[宝塔面板]].  

如果是公司里,我认为一般的运维人员,应该也没有大公司的人专业. 

## 用户管理篇

### 创建用户并给予权限

假如我要创建 `usernam = km911 password = asdfasdf` 的一个账号 , 并且还需要说明允许登陆的ip为任意ip.  语句一定要加   分号

```sql
%% 如果ip的位置为 “%” 则表示为任意ip %%
%% 当然也可以不做指定，那就表示为任意的IP %%

create user 'username'@'ip' identified by 'password';
```

```sql
create user 'km911'@'%' identified by 'asdfasdf';
```

给予其管理员权限. 

```sql
grant all privileges on *.* to 'km911'@'%' with grant option; 
```

只有查询无法写的权限.  这确实是一种常见的策略,避免新人误操作把库给删除了
其实胡乱更新破坏力也挺大的，
备份还得搞一搞。


<font style="color:gold">*.*  表示对所有的文件都具有查询的权限，或者说数据库，毕竟有些数据不该查</font>

```sql
grant select on *.* to 'km911'@'%' identified by 'password';
flush privileges
```
### 无法用密码登录

```sql
ALTER USER 'root'@'%' IDENTIFIED BY '@Dzg15484' PASSWORD EXPIRE NEVER; #修改加密规则
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '@Dzg15484'; #修改密码
FLUSH PRIVILEGES; #刷新数据
```
### 修改密码

像这类操作不用多少都应该是管理员来操作的

```sql
%% 这里写出完整的步骤 %%
use mysql
update user set password = password（'passwd'）where user = 'username'
flush privileges
```

### 删除用户

某人离职了，干掉账号
```sql
use mysql
delete from user where user = 'username' and host = 'ip'
flush privileges
```

<font style="color:gold">注意：创建用户或者修改用户密码之后，我们需要执行指令 </font> `` flush privileges 

### 撤销权限

撤销更新的权限 
```sql
revoke update on *.* from username@localhost
```

撤销所有权限
```sql
revoke all on *.* from username@localhost
```

### 开启远程连接

在创建用户的时候其实我们就发现了其中的一个字段就是让我们指明允许登陆的ip. 所谓的开启远程连接,就是修改用户的Host. 

```sql
update user set host = '%' where user = 'km911';
```

### vscode连接问题

vscode 会采用socket 进行连接我们的mysql, 对于localhost,就无法连接成功,我这里还没有尝试去连接我们的服务器. 


## Mysql 版本问题

mysql 6.0 以后驱动版本改变了,记得更新驱动程序,并且部分字段设置也有修改,等日后遇到了我们再来设置. 

### 密码问题

mysql 8 采用了 新的加密方式 
这里需要我们设置一下. 


mysql_native_password mysql 8
修改加密方式为早期版本的. 

```sql
alter user km911@'%' identified with  mysql_native_password by '123456';
```

或者在创建用户时就指明密码的加密方式 . 
```sql
create user 'km911'@'%' identified  with mysql_native_password by 'asdfasdf'
```

Actually for mysql community server 5.7, the default root password is randomly generated when you install. Check your /var/log/mysqld.log for a line talking about a "temporary password". Saves hours of messing around. 

## 意义

说实话，我对mysql的理解只在最最基础的层面，连接，通过可视化工具 写两句SQL建个数据库，建俩表，然后就CRUD 就上了。

没有在IDEA 中去创建用户什么的试过，也没有使用除了root用户以外的用户登陆过数据库，这个问题感觉很大，会有人在工作中使用 root 用户登录数据库来进行CRUD操作的吗，不知道，没工作过。

不知道，一个人的前途不应该是直勾勾的，又不是非开发的工作不可，当然也不是非计算机不可。



