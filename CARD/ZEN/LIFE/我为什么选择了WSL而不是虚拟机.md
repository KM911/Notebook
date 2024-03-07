---
title: 我为什么选择了WSL而不是虚拟机
top: false
mathjax: false
date: 2023-09-09 13:22
tags:
categories:
file-created: 2023 10 29
last-modified: 2023 11 29
---

## 我的需求

最近在将代码部署到服务器,因为工作环境是win出现了很多问题,比如path.IsAbs问题,虽然go可以进行交叉编译,但是当需要使用cgo的时候就有一点点问题,我就想开始使用双系统或者虚拟机.
再次重申一下我的需求
* 可以没有图形化界面 本身生产环境的服务器就是没有GUI的 可以使用CLI环境
* 和win的兼容性比较好 我需要使用QQ和微信等软件 部分软件不提供linux版本 并且我还想玩下游戏放松.
* 相对轻量化 我的笔记本不足以承受这些巨无霸

## 备选方案
### linux双系统
我大一时就开始捣鼓linux双系统了,也算是有一些经验.有一句话可以很好地概括linux.
> linux is free if your time is free.

#### 缺点
* 输入法问题 可以使用搜狗的 但是是不是会出现备选词不见 皮肤失效等问题 (你就不能不打中文吗?😭)
* 因为和win很多操作逻辑不同,导致我时常不是很习惯,需要花费很长一段时间去适应和调整 唯一比较开心的是chrome的使用体验没有太大差比,并且同步了我的数据和插件为Google点赞.
* wine并不能解决所有的问题 甚至我很多时候干脆重启然后使用win了
* 每次切换系统都需要重启 时间花费有点大
* 你会遇到很多奇奇怪怪的问题 比如我之前把python卸载了 然后我就进不去桌面了 (部分桌面组件依赖python) 有非常多的问题在等着你 
* rm太危险了 GUI删除文件相对要直观些 误删除的概率小得多
* 不要把网上看不懂的命令复制 后果自负 

#### 优点

* 完美支持gnu和其他专有软件 之前为了在win上使用make和vim还去安卓了cygwin,反正体验不是很好.
* 调度比win要好,更加省电,不会出现编译代码风扇就起飞的情况.
* 自定义的程度更高 只要你想 感觉都可以修改 比如firefox可以自定义主页css 各种快捷键 

总结:除非你是选择将linux作为你的主力机,不然我不太推荐你装双系统.因为你单一时间内还是只能使用一个系统环境,频繁切换十分不友好.如果你喜欢折腾,愿意花费大量的时间在一些"琐事"上,我还是十分推荐你直接使用linxu,而不是双系统.

### vmware为代表的虚拟机
首先是奇怪的安装体验,本该打开hyperv,但是我打开反而失败了😅.可能老天爷就不想让我使用这个吧.
一开始使用的桌面版,后来换成了服务器版,不知道是不是我电脑的问题,我总感觉使用虚拟机非常卡,特别是将光标聚焦到win或者linux的切换过程,非常折磨人.
然后就会自然而让的想进行虚拟机和win进行交互,比如连接虚拟机中的redis服务器. 更是麻烦.
#### 缺点
* 资源占用有点吓人 电脑不好的可以放弃了 
* 光标切换聚焦的延迟比较高
* 也有很多问题需要你去解决 比如虚拟机无法连接网络 无法识别磁盘 

#### 优点
* 和win的交互性比双系统强,可以做文件共享,端口转发等等操作
* 环境隔离,十分安全,无法启动后,重装一个虚拟机就好了.比重装系统然后配置各种文件 要方便多了

### wsl

其实一开始我不知道wsl,是我要开始使用docker,安装前需要安装wsl,我当时还傻乎乎地以为window可以直接跑linux内核了,后来才知道其实是跑在wsl中,然后wsl创建一个docker环境. 那我为什么不直接使用wsl创建的linux环境呢? 
## WSL是什么?

TODO 介绍 
WSL全称为 windows subsystem for linux,是微软
#### 优势

* 更加轻量化 启动速度快 资源占用少
* 和 windows结合更加紧密

#### 缺点

* 只支持部分liunx发行版. 有的发行版可能还是付费的.  
* 没有环境隔离. 宿主机的文件会被挂载到 `mnt`路径下,你可以删除宿主机的文件. 
### 安装 

启用subsystem

```ps1
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```
启用虚拟机

```ps1
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
设置默认版本为2.如果你不知道wsl1 和 2的区别话,请移步 [比较 WSL 版本 | Microsoft Learn](https://learn.microsoft.com/zh-cn/windows/wsl/compare-versions)
```ps1
wsl --set-default-version 2 
```

重启电脑使上述feature生效.



我们开启了wsl之后,还需要安装liunx发行版才可以使用. 
```ps1
wsl --install -d Ubuntu
```

其实wsl支持非常多的linux发行版,[详情](https://dowww.spencerwoo.com/1-preparations/1-1-installation.html#wsl)

关于我对于wsl的配置可以查看 [[开发环境搭建#wsl]]
