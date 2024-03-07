 
## Installation

>[!tip] [Install Docker Engine | Docker Docs](https://docs.docker.com/engine/install/)
>没有比官方更好的安装教程了  


>[!faq] windows也可以安装docker吗? 
>这个问题看你如何理解和定义. 
>毫无疑问,在docker的官网上, 清清楚楚地写着 "Install on Windows" ,你说docker不能在docker上安装显得你有些无理取闹. 但是你在 "System Requirement"中会发现你需要安装"Wsl"或者是开启"hypr-v".  
如果你知道它们是什么的话,如何按照这种方式的安装与运行,那我可以说,linux支持一切软件.使用wine你可以运行很多带有UI的windows程序,使用qemu+kvm,有什么程序是你无法安装并允许的呢?

>[!key] docker强依赖于Linux的内核.
>需要这些syscall ,chroot,cgroup,namespace, windows上没有这些对应的syscall,是不可能运行docker的.
>现在运行的docker 除开 docker desktop和部分的命令行, 其核心的容器化部分都依赖于hypr-v虚拟出的linux内核. 从这个角度看,我们说windows不支持docker或许也是正确的. 
>


>[!note] 安装docker 
>其实了解了上面的这一点后,安装docker就显得非常简单了,windows需要额外做一步虚拟化的操作,linux利用包管理就好了. 

>[!tip] 不同linux的包管理
>以我现在在用的manjaor(基于arch linux的发行版)为例,我只需要执行
>```bash
>sudo pacman -S docker
>```
>就可以将docker 安装成功了. 
>其余的发行版大体上都是类似的,如果官方源找不到docker,可以使用其他私有源或者从源码进行编译. 


>[!lab] 测试安装结果
> ```bash
> docker run hello-world
> ```
> 



## linux不同发行版

linux不同发行版的软件是不兼容的,例如rpm和deb的软件结构就完全不一样

从移植性的角度来看,这不是什么好的事情. 

