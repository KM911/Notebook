
## 效果演示 

>[!exp] 执行sql语句
>```sql
>select * from class;
>```

## 核心原理 

1. mysql可以执行一个sql文件并返回结果. 
2. execute-code 会自动生成该sql文件 

我们需要做的就是理解你的mysql 然后让其执行. 

我的mysql是在wsl, 所以需要将 windows path 换位 wsl path . 


### 环境准备 

请设置如下环境变量 

`SQL_USER` `SQL_PASSWD` `SQL_DB`  


## 狗屎 我现在不理解就是 为什么可以