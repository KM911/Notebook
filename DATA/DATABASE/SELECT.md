---
file-created: 2023 11 21
last-modified: 2023 11 26
---

*注意：*
        *数据库为 mysql


基本的查询语句，从table 表中查找列名为fieldName 与 fieldName2的列 并 组成一个表输出

```sql
select fieldName1,fieldName2 from table
```

我们首先建立一张课程表

```sql
create table course
(
    id   int                           not null,
    name varchar(255) collate utf8_bin not null
);

```
*运行下方代码，一键创建表以及导入数据。

```sql

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course` (
  `id` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,'大学语文'),(2,'计算机应用基础'),(4,'思想道德修养与法律基础'),(5,'高等数学'),(6,'英语'),(7,'马克思主义基本原理'),(8,'中国近代史纲要'),(9,'计算机系统组成'),(10,'操作系统基础知识'),(11,'系统软件知识'),(12,'形势与政策'),(13,'毛概'),(14,'C++程序设计'),(15,'python程序设计'),(16,'大学美育'),(17,'心理健康'),(18,'职业规划'),(19,'高等代数');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

```


数据如下

| id  | name                   |
| --- | ---------------------- |
| 1   | 大学语文               |
| 2   | 计算机应用基础         |
| 4   | 思想道德修养与法律基础 |
| 5   | 高等数学               |
| 6   | 英语                   |
| 7   | 马克思主义基本原理     |
| 8   | 中国近代史纲要         |
| 9   | 计算机系统组成         |
| 10  | 操作系统基础知识       |
| 11  | 系统软件知识           |
| 12  | 形势与政策             |
| 13  | 毛概                   |
| 14  | C++程序设计            |
| 15  | python程序设计         |
| 16  | 大学美育               |
| 19  | 高等代数               |
| 17  | 心理健康               |
| 18  | 职业规划               |


## 基本查询

示例代码：查询单个字段，多个字段之间使用 ”  英文逗号  ‘ , ’ “ 隔开
```sql
select name from course;
select id from course;
```

注意：

```sql
select id,name from course;
select name,id from course;
```

这两条语句都可以从表中获得相应的数据，最终呈现的结果按 查找 filedName 的顺序排

查询全部字段：
```sql
select * from course
```

### 取别名

也可以为输出之后的表格取别名
```sql

select id '课程编号',name '课程名称' from course;

```

添加别名前

   | id  | name |
   | --- | ---- |
   | 1   | 张三     |

之后

| 课程编号 | 课程名称 |
| -------- | -------- |
| 1        | 张三     |

### 插曲-关于Mybatis的映射

这里有一个问题，我们的 mybatis 在做映射的时候 是将输出结果中的字段与实体类对应呢，还是 原字段名呢？

```java
%% 假如实体类中有如下属性 %%
int userId;
String username;
```

而我们的SQL 语句是

```sql
select id as userId,name as username from course
or
select id userId,name userName from course
```
是否会有错误？

答案是不会的，那么最终的结论就是我们的mybatis还是按 最终生成表 来对应的
```java

@Mapper
public interface SqlMapper {
    @Select("select id as userId,name as userName from course where id = #{id}")
    Course selectAllInfo(int id);

}

@Test
void contextLoads() {
    Course course = sqlMapper.selectAllInfo(1);
    log.info("course:{}", course);
}

```

![[Pasted image 20231012085958.webp]]

### 表达式查询

**<font style="color:green;font-weight:700;font-size:20px">使用student表</font>

我只做基本演示，所以数据少，可酌情添加。

```sql

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` varchar(10) COLLATE utf8_bin NOT NULL,
  `s_major` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `sex` varchar(6) COLLATE utf8_bin NOT NULL,
  `birthday_year` int(11) NOT NULL,
  `current_year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='学生表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'张三','计科','男',2003,2023),(2,'李四','大数据','男',2004,2023),(3,'王五','数学','女',2005,2023),(4,'张一','大数据','女',2003,2023),(4,'王六','数学','女',2001,2023);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;


```


不一定查找表中有的列名 
还可以使用表达式，别名也不一定要有 

```sql
select name ,(current_year-student.birthday_year)  from student;
```

结果：

| name | current_year-student.birthday_year |
| ---- | ---------------------------------- |
| 张三     | 20                                   |

使用别名

```sql
select name,(current_year-student.birthday_year) age from student
```

| name | age |
| ---- | --- |
| 张三     | 20    |

#### 新增字段描述

还可以 在 字段的前方插入 一个新的自定义字段 来描述后方的字段

有一说一，我不知道为什么不能使用双引号。

记得添加的字段后方也是有逗号的，字段之间使用 "逗号" 分隔

```sql
select '姓名:' ,name,'年龄:',(current_year-student.birthday_year) age from student
```

结果：

| 姓名: | name | 年龄: | age |
| ----- | ---- | ----- | --- |
| 姓名: | 张三 | 年龄: | 20  |
| 姓名: | 李四 | 年龄: | 19  |
| 姓名: | 王五 | 年龄: | 18  |
| 姓名: | 张一 | 年龄: | 20  |
| 姓名: | 王六 | 年龄: | 22  |

#### 消除重复行

在查找的时候消除 "sex" 重复的行
```sql
select distinct sex from student;
```

那这样应用场景就是 查找一个字段的分类了
那这样我们可以扩展一下，如何知道分类的个数，要求使用SQL语句

```sql
%% 这句虽然在语法上没有错误，但结果是不正确的 %%
select distinct count(sex) from student

%% 正确的应该使用这个 %%
select count(distinct sex) from student

%% 应该还可以这样 嵌套的写一下%%

select count( sex ) "分类个数" from (select distinct sex from student) as test;

%% 记得为后面的那个sql语句写一个别名,不然报Error %%
%%' Every derived table must have its own alias' %%
```

## 条件查询

条件查询需要使用我们的 <font style="color:pink">where</font> 关键字

### 简单的条件查询

语法
```sql
select filedName from Table where "条件"
```

条件谓词：
    用的多的不写了，比如大于小于这些
    

"  <>  "  
```sql
select name from course where id <> 18
```
这条语句的含义为：
                            查询 id 不为 18 的所有 行


查询 id 位于 5 与 10 之间的 行
```sql
select name from course where id BETWEEN 5 AND 10;
```
一共6个

| name |
| ---- |
|高等数学|
|英语|
|马克思主义基本原理|
|中国近代史纲要|
|计算机系统组成|
|操作系统基础知识|


当然也可以使用  <font style="color:gold">  NOT  </font> 关键字修饰

含义就相反了
```sql
select name from course where id NOT BETWEEN 5 AND 10;
```

| name                   |
| ---------------------- |
| 大学语文               |
| 计算机应用基础         |
| 思想道德修养与法律基础 |
| 系统软件知识           |
| 形势与政策             |
| 毛概                   |
| C++程序设计            |
| python程序设计         |
| 大学美育               |
| 心理健康               |
| 职业规划               |
| 高等代数               |


### 使用表达式作为条件查询

```sql
%% 查询所有学生年龄 %%
select (current_year-birthday_year) as age from student;

%% 查询年龄大于20的学生 %%
select name from student where (current_year-birthday_year)>20;
```

#### 表达式+谓词 做条件

查询年龄在 2 0到 22 之间的  包括 20 和 22

```sql
select name from student where (current_year-birthday_year) between 20 and 22
```


#### 多重条件查询

查询 年龄在 20 与 22 之间 的 男生
```sql

select name from student where sex='男' and (current_year-birthday_year) between 20 and 22
```

查询专业为大数据或者数学专业的女生

下面这种写法正确吗？
```sql

select name from student where sex='女' and s_major='数学' or s_major='大数据'

```

应该加 括号 才能 正确回答问题
```sql

%% 正确的应该是： %%
select name from student where sex='女' and (s_major='数学' or s_major='大数据');

```


### 结合 不重复关键字 的例子

*新建一张学生选课的表

```sql
create table sc
(
    student_id char(8),
    course_id char(5),
    Grader SMALLINT comment '成绩',
    primary key (student_id,course_id)
)
```

*导入数据：

```sql

DROP TABLE IF EXISTS `sc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sc` (
  `student_id` char(8) NOT NULL,
  `course_id` char(5) NOT NULL,
  `Grade` smallint(6) DEFAULT NULL COMMENT '成绩',
  PRIMARY KEY (`student_id`,`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sc`
--

LOCK TABLES `sc` WRITE;
/*!40000 ALTER TABLE `sc` DISABLE KEYS */;
INSERT INTO `sc` VALUES ('1','2',91),('1','3',67),('1','4',45),('1','5',59),('2','2',78),('2','3',79),('2','4',98),('2','5',61),('2','6',56);
/*!40000 ALTER TABLE `sc` ENABLE KEYS */;
UNLOCK TABLES;

```

添加如下数据 
student_id 就是 学生表 中 学生 的 id  course_id 同理

| student_id | course_id | Grade |
| ---------- | --------- | ----- |
|1|2|91|
|1|3|67|
|1|4|45|
|1|5|59|
|2|2|78|
|2|3|79|
|2|4|98|
|2|5|61|
|2|6|56|


语义显而易见
```sql
select student_id from sc where Grade < 60
```

结果：

| student_id |
| ---------- |
| 1          |
| 1          |
| 2          |

但是同一个学生id会输出很多，假如我们只需要知道谁挂课了，不需要知道有多少门挂了，加一个 distinct 就好

```sql
select distinct student_id from sc where Grade < 60
```


### 结合排序关键字


后端返回的数据是按照 一个非主键排序 的表，这样就省去了在上层或者前端对字符串进行操作

SQL就能做的事情。

查询不及格的学生情况，并且把分数 升序排列
```sql

select student_id,Grade from sc where Grade<60  order by Grade ;

```

降序排列使用关键字   <font style="color:gold">desc</font>

```sql

select student_id,Grade from sc where Grade<60  order by Grade desc ;

```

## 聚集函数 

其实就是 <font style="color:gold">count(*)</font> 这些

| 函数                            |
| ------------------------------- |
| max ( [distinct or all]<列名> ) |
| sum                             |
| avg                             |
| min                                |



用法同 <font style="color:gold">count(*)</font>  ，但是值得注意的是 sum 和 avg  一个计算综合一个计算平均值，这两个作用的列必须是数值型。

ok，疑问， max 和 min 作用的 列 是否也必须是数值型

文心一言 的回答 （关键部分）

```text

对于一些数据库系统（例如 MySQL），如果你对非数值型的列使用 MAX() 函数，该函数会尝试将所有值转换为数值类型，然后返回最大的那个数值。但是，这可能会导致一些意想不到的结果，比如，对于字符串类型的列，它会尝试将字符串转换为数字，而如果字符串不能转换为数字，那么可能会产生错误或者返回一个不确定的结果。

在其他数据库系统（例如 PostgreSQL）中，如果对非数值型的列使用 MAX() 函数，这可能会导致错误。

```

copilot 的回答

```text

MAX() 是 SQL 中的聚合函数，用于返回一组值中的最大值。它可以用于数值和非数值数据类型。当用于非数值数据类型时，MAX() 函数将返回按字母顺序排列的最后一个字符串。例如，如果您在一组字符串上使用 MAX()，它将返回按字母顺序排列的最后一个字符串。但是，当用于非数值数据类型时，MAX() 函数的结果可能没有实际意义或用途。

```

我没试过，先打   ？ ∠ 

## 分组查询

关键字是  <font style="color:gold">group by</font>  列名


统计 各个课程 的人 选课的 人数

```sql

select course_id, count(student_id) from sc group by course_id;

```

<font style="color:gold">group by</font>  后面还可以 接 having  

having 和 where 后面都接 条件，但是区别就在于 having 作用的对象是分组，而 where 作用的对象是 表 和 视图

where 不可以 使用 聚集函数做 条件

```sql

select student_id '学生id 不加limit' from sc;

select student_id '学生id 加 limit' from sc limit 5;

```

| 学生id 不加limit | 学生id 加 limit |
| ------ | ------ |
| 1      | 1       |
| 1      |      1  |
| 1      |     1   |
| 1      |     1   |
| 2      |       2 |
| 2      |        |
| 2      |        |
| 2      |        |
| 2      |        |


根据 学生id分组 然后求课程成绩平均值 ，按平均分从高到低排序

```sql

select student_id,avg(Grade) from sc group by student_id order by avg(Grade) desc; 

```

然后我们写一个逆天一点的语句，主要是数据库中的数据太少


这其中的数字都可以更改的，展示的只是例子

```sql

%% 只输出第一个 %%

select student_id,avg(Grade) from sc group by student_id order by avg(Grade) desc limit 1 ;

%% 输出一个，但是忽略第一个 %%

select student_id,avg(Grade) from sc group by student_id order by avg(Grade) desc limit 1 offset 1;

```


## 连接查询
### 自然连接查询

先说一下树上的概念：
    把结果表目标列中重复的属性列去掉的等值连接查询则为自然连接查询
所以我们先看看什么是等值连接查询
#### 等值连接查询

```sql
%% 先运行这一句改变一下 student 表 %%
alter table student add column student_id int(11) not null;
```

```sql
select student.*,sc.* from student,sc where student.student_id = sc.student_id;
```

如果报条件总是错的不要担心，就当IDE发癫吧。、

可以知道，结果表中有 两列的student_id ，没错，我们的自然连接就是去掉这两行相同的列

<font style="color:gold">下面是自然连接的内容</font>

```sql

select student.student_id,name,s_major,sex,birthday_year,current_year,course_id,Grade from student,sc where student.student_id = sc.student_id;

```

跟定义说 的和 书上的例子 大同，无异。


### 复合条件连接查询

定义是：
            使用一条SQL就可以同时完成选择和连接查询，这是where子句是由连接谓词和选择为此组成的复合条件。where 子句中有多个条件的连接查询，称为 。。。。。

我们懂 条件查询，复合就是复杂。 至于连接，简单理解为两个表联合着查，一般用来做逻辑外键。
建议直接运行例子。 
```sql
select student.student_id,name from student,sc where student.student_id = sc.student_id and course_id = 2 and Grade > 30;
```


### 自身连接查询

连接查询，不仅可以在两个不同的表中，也可以是一个表与自己进行连接。

这个看书吧

### 外连接查询

左外连接就是会将左边的表中的所有 查询的列（满不满足条件都输出）输出到结果表中，右外连接同理。

我的表的设计是有缺陷的。
#### 左外连接
直接上例子
```sql
%% 普通连接 %%
select student.student_id,name,sex,birthday_year,current_year,course_id,Grade from student,sc where student.student_id = sc.student_id;

%% 左外连接 %%
select student.student_id,name,sex,birthday_year,current_year,course_id,Grade from student left join sc on student.student_id = sc.student_id
```

#### 右外连接

```sql
%% 必须运行下面的insert，不然结果看不出来外连接的灵魂 %%
%% 主要是我设计的表太差了，不过能反映效果即可 %%

insert into sc values(8,1,61);

select student.student_id,name,sex,birthday_year,current_year,course_id from student right join sc on student.student_id = sc.student_id
```



## 嵌套查询


先给一个简单的例子给兄弟们了解一下是神马玩意。

```sql
select name from student where student_id in(select student_id from sc where course_id = 2);
```
咱们理解一下这个句子，从课程表中找出选择了课程2的学生学号，然后根据学号再从学生表中找名字。


我们完全可以写成连接查询
```sql
select name from student,sc where sc.course_id=2 and student.student_id=sc.student_id;
```

ok  说完了，其余的无非就是介绍几个谓词  O.0 ?      0_O!

## 集合查询

select 语句的查询结果是元组的集合，所以对多个 select 语句的结果可进行集合操作，集合操作主要包括 并（union） 交（intersect） 差（except）

参加集合操作的各查询结果的 <font style="color:red">列数</font> 必须相同，对映项的数据类型也必须相同

说实话，至今没用过这样的查询，可能是水平太差，自己做的东西也不需要这样的。

既然如此，看概念的话，也是可以多个表的，
要查询的字段应该是两个表中共有的字段，因为要求 列 必须相同

```sql
select * from student where s_major='大数据' union select * from student where ( current_year- birthday_year ) >18;
```

