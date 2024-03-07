---
file-created: 2023 11 21
last-modified: 2023 11 26
---

## 使用体验

说实话,作为微软早期的软件,其实使用体验都不是太好.主要是和windows高度绑定,(2017年开始陆陆续续支持linux了)

如果可以我还是希望自己可以使用mysql,或者其他数据库,不过说实话,有太多的命令是我不太好记忆的了.

## 安装 

请牢记,还是使用smss吧,do as rome. 

### 基础概念

dao , database owner 这里其实是mssql的 
master数据库, 其实是主从的master 
## 验证方式

windows验证,利用当前微软用户作为账号.
sql server验证,sql server创建的账号.
混合验证, 两者都需要使用.

### 创建新的用户 

我不是很想表述该怎么办啊 好难受啊 . 这部分的内容太容易出现问题了. 

### 使用其他软件连接sql server

处于 安全考虑 ( 封闭) sql server 的TPC连接和Agent都是关闭的,我们需要开启才可以使用其他软件连接.

SQL Server Configuration Manger 

开启TCP连接,将端口号设置为1433

Client Protocol也需要允许TPC

###  sql notebook 无法连接的问题

其实很简单,你没有创建正确的用户, 使用smss可以创建用户. 

## sql 

主要是每个数据库都有一些关于自己的特殊命令,比如mssql就没有use.

一些实例demo . 我想吐槽 sql server真的一点也不好用不是吗? 



## 创建表

