---
file-created: 2023 11 23
last-modified: 2023 11 29
---

[1.5.1 容器技术 | 深入架构原理与实践](https://www.thebyte.com.cn/architecture/container.html)

1. [[chroot]]
2. cgroups + namespace
3. docker
4. oci




chroot 被认为是最早的容器化技术之一，chroot 可以重定向进程及其子进程的 root 目录到文件系统上的新位置，也就是说使用它可以分离每个进程的文件访问权限，使得该进程无法接触到外面的文件，因此这个被隔离出来的新环境也得到了一个非常形象的命名，叫做 Chroot Jail（监狱）。

这便是容器最重要的特性 -- 进程隔离。




不过由于 container 这一命名在内核中具有许多不同的含义，为了避免代码命名的混乱，后来就将 Process Container 更名为了 Control Groups，简称：cgroups。


至 2013 年，Linux 虚拟化技术已基本成型，通过 cgroups、namespace 以及安全防护机制，大体上解决了容器核心技术“运行环境隔离”。



至此，容器技术体系已经解决了最核心的两个问题 “如何运行软件和如何发布软件”，云计算开始进入容器阶段。


OCI 其核心产出是：

OCI Runtime Spec（容器运行时规范）
OCI Image Spec（镜像格式规范）
OCI Distribution Spec（镜像分发规范）。



