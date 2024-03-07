---
file-created: 2023 11 15
last-modified: 2023 11 26
---

## 大数据的三架马车 

大数据三驾马车是指分布式数据处理MapReduce、分布式数据存储GFS（Google文件系统）以及列式存储数据库BigTable这三者的结合，它们共同构成了强大的大数据处理平台。


海量数据处理 
海量数据存储
海量数据查询 

? 海量数据收集 

其实就是单机 无法解决问题了, 我们需要开始分布式集群来解决. 


### 何为大数据

>[!tip] 
> 现在我终于可以定义了 : 针对大量/海量数据整个生命周期的一系列技术解决方案. 
> 
> 关键词 : 数据挖掘 数据存储 数据计算 数据传输 数据分析 数据治理 
> 
> 所以你写爬虫的,可以说是从事数据挖掘/数据采集行业的, 你作为数据库内核开发,也可以说自己是数据存储的,你是一个文职人员用excel/r/python处理数据,也可以说自己是数据分析... 
> 
> 你看几乎只要是个人,无论你对于计算机了解的有多少,和"数据"有一点关系,都可以是大数据相关人员. 


不过对于计算机技术而言, 通常情况下我们还是将下面的内容视为大数据技术. 

数据计算 

mapreduce 

spark flink hardoop 这样的 

## Data Storage 

Database : [[PROJECT/ENVIRONMENT/MySql|MySql]] [[Redis]] 


## Data Computer



### What is big data? 

大数据不是某一个具体的事物,而是一系列针对海量数据的处理分析使用的技术.它是一系列技术的集合,也可以是一些技术解决方案,一些分布式的数据库具有极高的性能,就是一个大数据技术,但是和传统的数据库技术其实没有区别.

如果我们细化一下大数据核心的功能.
* 数据存储
* 数据计算
* 数据传输
### 大数据下的明星产品

#### 数据存储
[Apache Hadoop HDFS](https://hadoop.apache.org/)  看名字就知道 这是一个文件系统

Hadoop 是一些列软件

[Apache Hbase](https://hbase.apache.org/) Nosql kv形式的 

[Apach Kudu]()

#### 数据计算
[Apache Hadoop MapReduce]()

[Apache Hive]() SQL的分布式计算框架

[Apache Spark]() 基于内存的计算 

[Apache Flink]() 流计算

#### 数据传输

[Apache Kafka]() 消息中间件

[Apache Pulsar]() 分布式消息系统



#### Hadoop 

Hadoop 整体解决方案 
* HDFS 存储
* MapReduce 计算
* YARN 资源调度


