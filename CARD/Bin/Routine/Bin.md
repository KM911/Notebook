---
file-created: 2023 12 27
last-modified: 2023 12 30
---




## 为什么要重启 

因为很简单啊,不重启无法重新加载环境变量. 

### linux的环境变量

>[!bug] 我之前使用的zsh, 对于环境变量的修改都是在 `.zshrc`上进行的, 你会 bash不会
>有的shell有自己独立的config, 对于环境变量,我认为最好的方式是将其添加到 /etc/environment 上. 
>


## python envy 

>[!warning] 不要在linux下移除python 
>你会发现,很多linux发行版会自带python/python3.  并且很多版本比较古老, 你想要卸载并重新安装,你会发现你可能进不去桌面了,对于一个新人来说,这无疑是致命的. 

>[!tip] python 也是基础软件的一部分 
>如果你编译过glic你应该还记得,一个C语言的lib库,编译时都需要python的环境 (这里并不是因为"编译"这个行为本身需要,而是有的环境准备脚本是用python写的). 很多桌面环境和基础服务或多或少依赖python , 不然为什么大部分发行版里都携带python呢? 
>

>[!done] envy 来管理你的python环境 
>你应该已经认识到了python的重要性了, 所以为了避免因为python的版本问题或者是不小心对系统的python进行了错误操作,应该使用envy




## hyper thread 

>[!note] 没有那么想当然的事情. 天底下还有什么技术,可以没有任何限制条件和特定场景下有更好的performance.  




## 当计算机性能不够时 我们可以做什么 

### scale 

横向扩展(scale out)和纵向扩展(scale up),或者说水平扩展 和 垂直扩展 

其实是一回事情, 可以建立一个二维直角坐标系. x是数量,y是质量. 

对于服务器来说,横向扩展-- 增加机器数量, 纵向扩展--提高机器性能. 

一般情况下,我们都是购买云服务器使用的,虽然可以购买更多的核心来提升性能(纵向扩展) ,但是纵向/垂直扩展的水平是有极限的--当把全部的CPU核心都给你了,其实就无法再提高性能了,你都买下了一台真实的服务器了-- 其实一般服务器的主板都是可以插好多个CPU的

> [!tip]  核心方式 
> 分布式 : 通过网络让大量机器协同工作

## parallel 


> [!tip]  核心方式 
> 并行编程 : 充分利用多核CPU,而不是一核心有难,多核围观. 

画面渲染和

## golang goroutine schedule  

### GMP Goroutine Processor  Machine 

### Machine 

a core map a machine . 

By the way , you could use 

### processor 

其实你发现了没有,go procs只有12个,也就是和逻辑线程是一致的. 

### Goroutine 




[[并发编程x并行编程]]
[Amdahl](Amdahl.md) 通过提高并行度来提高性能的具体数值. 






### xx是简单的 

网络上常常看见各种低智言论. 这里我就反驳一下. 

写一个操作系统是简单的,xv6的代码不过万,照着抄一个并不困难,在上面修改一些命令也不复杂. 但是这并不意味着现代操作系统十分简单. 
任何一个细小问题都值得研究. 比如调度问题. 


## macos 

我没有mac的电脑,但是考虑到让你在macos使用我决定使用




## chrome parallel download 

past this in search bar : chrome://flags/#enable-parallel-downloading

![](Bin-20240125154755275.webp)




>[!warning] 网络安全问题似乎比我想象地要严重得多
>每时每刻都有人在尝试破解你root账户的密码.
>利用`grep 'Failed' /var/log/secure` 就可以看见哪些ssh登陆失败的日志了  
 >![](基于UDP的稳定连接-20240115234149942.webp)
 >好在我们的服务器上没有重要数据,黑客即使破解了也没有多少损失,如果是公司的服务器被黑了,就会有非常大的损失了. 
 
 

## glibc还是musl

太难受了,说实话. 

>[!others] glibc的地位 
>GNU lib C . C语言的标准库? 其实也不对,因为我们使用的是gcc,可


>[!note] musl 
>其实就是没有历史包袱,所以可以实现得非常小. 


## acill 和 位运算. 

ascll是被精心设计过的. 所以我们只需要做一点点位运算就好了. 

直接给出答案的话就是.

大小写字符串,核心是第6位的值,如果为1说明是小写. 
给定一个任意字符串 [a-Z]
1.小写to大写. == 讲第6为变成0 1-0  32进行 | 96
2.大写to小写 == 讲全部的字符第6位 变成1 和 32进行 | 运算. 
3.交叉转换 == 0变1 1变0 进行 ^


## Where are you going ? 

![](Bin-20240109220213568.webp)

>[!exp] If you do not know which job you want to do , it does not matter which subject you major . 



## 图标库的使用

两种方式 : 第一种是将每个图标的svg/png保存下来
2.使用图标框架,这样你就可以直接@xx使用了. 

前者的好处是方便修改参数,体积较小.比较麻烦 

>[!tip] 总结
>我使用手动下载,因为我的项目一般也比较小. 



## regex

说实话,这个网站真的惊艳到我了.并非其UI或者内容的丰富程度,而是这种交互式的学习过程一直是我追求的.

大部分的学习材料,要么只是单纯地表述真实,缺少"实际"案例.

>[!warning] regex的标准挺多的
>使用 grep --help 可以看到
  -E, --extended-regexp     <模式> 是扩展正则表达式
  -F, --fixed-strings       <模式> 是字符串
  -G, --basic-regexp        <模式> 是基本正则表达式
  -P, --perl-regexp         <模式> 是 Perl 正则表达式



## 脚本写多了不好 

>[!note] 容易忘记一个事情
>我们的server类程序是需要一直运行的,你不能因为一个网络请求超时就让程序退出,这在脚本中非常常见. 
>如何处理错误就成为了一个非常重要的问题


## Why you should not use link envokey 

一个非常简单的道理,提供了更少的信息,不方便理解和debug.

>[!faq] 是否会创建无用的中间变量,导致内存被浪费了呢? 
>





## 懒惰求值 

>[!v] 表达可能存在问题 
>一个函数的执行逻辑可以变化吗 ? 

js是简单的



## Meta-knowledge

>[!exp] 你尝尝会听到如下类似的话语 
>1.文科好的人,语文一般比较好
>2.数学好的人,一般物理会比较好. 
>3.如果你会C语言,python几天就学会了. 
>... 

>[!note] 我们不讨论其是否是100%正确,但是至少在一定程度上具有普适性. 

>[!tip] meta knowledge(元知识) 或者 atomic knowledge (原子知识) 
>>[!transfer] 就如同各种化合物都是由元素周期表中的元素组成的. 
>>高级的,复杂的知识都是由基础知识拼凑组合起来的.  

>[!note]- 118种元素，其中94种元素天然存在于地球上,其余24种则为合成元素
>有限的元素通过各种组合,形成了数以万亿的各种化合物. 烷烃只有C H 两种元素,组合出了海量的烷烃类化合物. 大部分化合物都是由几种常见的元素组成的. 还记得被高中化学的同分异构体吗? 哈哈哈 

>[!tip] 结构化笔记 和 神经网络 
> 
> 




## 视频剪辑通用手法 

1. 不同元素切换 : 转场 推荐使用模糊 最简单并且有效

转场 : 模糊 放大 吸入 
特效 : 路线


视频编码格式

AV1 
HEVC
H265 
H264 
还有非基于RBG的这样可以进一步来减少视频的

你可以理解其中的原理吗? 我感觉其实是不可以的呢?
但是肉眼可见的使用AV1编码速度非常慢,感觉都有10x的差别. 


## Code style (go)

更多的提示信息.

✔️`func createCmd(command string) (cmd *exec.Cmd) `

❌`func createCmd(command string) *exec.Cmd`


## go build 没有窗口 

-H=windowsgui就可以没有窗口了
```
go build -ldflags "-s -w -H=windowsgui" 
```



## Github Programming Language Color Table

>[!tip] Obsidian Graph Tree

| RGB       | Example |
| --------- | ------- |
| `#E05252` |         |
|           |         |
|           |         |


>[!tip] 填充该颜色表格
>
| Language | RGB | Example |
| ---- | ---- | ---- |
| C |  | <div style="color:#f34b7d" >C</div> |
| C++ | `#f34b7d` | <div style="color:#f34b7d" >C++</div> |
| python | `#3572A5` | <div style="color:#f34b7d" >C++</div> |
| java | `#b07219	` | <div style="color:#b07219" >java</div> |
| go | `#00ADD8` | <div style="color:#f34b7d" >C++</div> |
| rust | `#dea584` | <div style="color:#f34b7d" >C++</div> |
| R |  | <div style="color:#f34b7d" >C++</div> |
| javascript | #f1e05a | <div style="color:#f34b7d" >C++</div> |
| vue | #2c3e50 | <div style="color:#f34b7d" >C++</div> |
| HTML | #e34c26 | <div style="color:#e34c26" >HTML</div> |
|  |  |  |
|  |  |  |


