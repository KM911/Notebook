---
file-created: 2023 11 15
last-modified: 2023 11 29
---

>[!faq] 需要一个环境 

首先，你的开发机器会变得干净很多。你需要个 mysql ，要安装吧。需要个 redis， 也要安装吧，对应的依赖，也要安装吧。如果有一天想卸载呢？你猜猜哪些依赖可以删了，哪些依赖还不能删呢？如果电脑重启了，进程要重新启动吧。要设置自启动么？启动速度又会慢。要搞编译了，想腾些内存？要关进程吧，各个进程的开关命令要记吧。配置不小心搞坏了，影响了系统的其它文件？Emmm，小则重启，大则重装...总之，装的东西越多，维护起来就越心累。但是有了 Docker 就省事多了，永远只需要维护两个东西：镜像列表，和容器列表...大部分开发的环境依赖还是很重的，运行环境，中间件，各种服务。而且有了 Docker，还有更神奇的魔法：docker run -v "${PWD}":"/script" --rm python:3.8 python /script/main.py 对，我的本地不安装 python，也能运行 python 代码了！时至今日，使用容器作为代码调试环境也是非常实用的。尤其是做三方库，测试版本兼容性的时候，比起本地维护多个运行版本，多个镜像，岂不是要方便许多。另外，之前我自己想在本地装一套 WordPress 做测试，于是 Apache、PHP、MySQL 折腾了一整套，但开发机不是 Linux，所以很多安装方式都要自己查，所以绕了很多弯路，安装了一堆东西，修改了一堆配置，好不容易搭起来，但半个月后，当我想删的时候，并记不起来，我当时到底都做了些什么...现在，有了 Docker ，只需要一个命令：docker run -p 80:80 wordpress拯救人生啊！！！这也是我想说的第二个点，尝鲜测试，变得简单了太多！最后做个广告，Methodot，您的一站式云原生在线开发协作平台，深度整合云原生技术，如果想看看 Docker 对于开发者的意义，不如来这个网站。在线编码，组件集成，一键部署，全都是以容器技术作为基础的，而作为用户的你，全都是所见即所得！而最终的意义是什么呢？编码之外，都是工具，而非负担传送门：Methodot 官方网站


## 基于docker做集群化的部署 

你认可吗? 利用docker可以跑多个mysql 他们有完全不同的配置没有问题吧 
利用docker你可以学习真正的分布式. 

你所做的一切都是为了提高你的开发效率,而不是没有意义的事情不是吗 ? 
## Install


[Install Docker Engine on CentOS | Docker Docs](https://docs.docker.com/engine/install/centos/)

change source 

[轻量应用服务器 安装 Docker 并配置镜像加速源-最佳实践-文档中心-腾讯云](https://cloud.tencent.com/document/product/1207/45596)

重启以生效
```bash
sudo systemctl restart docker
```
[创建最简单的镜像 - Containerization and Automation](https://containerization-automation.readthedocs.io/zh-cn/latest/docker/basic/hello-world/)
## some knowlage you should know 

image
container







