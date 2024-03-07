

## Aggregate

翻译是聚合 其实是有道理的 

将多个 聚集到一起 然后合成一个 , 所以你会发现都是操作列表的函数 .

最常用的聚合函数 count,sum,avg,max,min


## 列名重命名 
old_col_name as new_col_name


## 限制数据 

top 5 
## 条件查询

但是这里其实有非常多的条件,这个是最为复杂的. 
where condition


## 升序/降序


## 模糊查询

where key like pattern

`%` 匹配任意数量的字符。
`_` 匹配一个字符。
`[charlist] `匹配 charlist 中的任意一个字符。
`[^charlist ]` 不匹配 charlist 中的任何一个字符。

常见例子 : 



## 分组查询 

>[!example] 分组查询的意义 
>比如统计男生和女生的数量;统计不同岗位的平局薪资;统计不同年龄阶段的收入水平... 


> [!faq] 分组后可以显示什么数据? 
> 依赖条件 和 聚合函数处理后的结果


> [!faq] 我们可以利用where对数据进行初步过滤,如何对分组后的数据进行过滤呢?

>[!example] 比如说某类商品数量太少了,我们希望其分组的结果中不要出现. 
>使用 group by ptype having count(pid) > 5; 只统计有5种以上的商品类型.

## 连接查询 

>[!note] 定义 : 一次查询多张表. 

### 笛卡儿积 

from table1,table2 来实现. 会进行笛卡儿积的操作,其中相同的列名会组合成为新的列. 

>[!faq] 笛卡儿积存在大量的冗余信息,这很不理想. 通常情况下,我们的进行连接查询的表格是存在或多或少的关联的,可以利用这些关联信息来消除冗余吗? 

>[!faq]- 如果没有任何相关信息呢?
>不妨做一个假设.
>结论,如果不使用right 和 left 
>join的效果和where完全一致

>[!abstract] 解决方案
>1.你可以添加足够多的where条件来实现
>2.利用join

### 内外连接 

>[!exp] 有时,多表直接可能存在一些不存在对应关系的行,我们该采取何种态度? 

>[!fix] 
> 1.直接将其移除
> 2.将缺失信息填充为NULL. 

其中将其直接移除可以理解为内连接,外连接将会根据一定规则进行补全. 
### 左右连接 

> 当我们谈及左右连接时,意味着一定是外连接,因为内连接讨论左右没有任何意义. 



因为是两张表,所以根据那一张表来决定是否将其丢弃就非常关键,引申出了这个概念. 

你可以通过交换两张表的位置来实现左右一致的效果,所以我认为左右连接的意义不太. 


## 子查询 

> [!exp] 如何查询员工薪资低于平均水平的员工信息呢? 

> [!error] 错误理解
> ```sql
> select *  from empl where salary < avg(salary); 
> ```
> 这里的错误是因为没有深刻理解 "聚合"的含义,内容必须是列表,如何将聚合函数内部的`salary`替换为列表呢? 


>[!done] 
>这里不能将 avg 作用于 subquery.
>```sql
>select * from empl where salary < (select avg(salary) from empl);
>```

编写子查询应该按照从里向外一层层的递进关系来编写.
