---
file-created: 2023 11 15
last-modified: 2023 12 01
---

一个专门用于教学的操作系统,代码量相比非常少,但是又足够丰富,可以让你了解计算机结构的全部. 

## 环境搭建

[从零开始使用Vscode调试XV6 - 知乎](https://zhuanlan.zhihu.com/p/501901665)

```bash
sudo apt install -y binutils-riscv64-linux-gnu gcc-riscv64-linux-gnu gdb-multiarch qemu-system-misc opensbi u-boot-qemu qemu-utils
```
## 开始 

```bash
make qemu 
```

恭喜你,现在你就已经进入了xv6了.


退出qemu

### linux 高级操作 

我们不再是简单的`ls cd pwd` 这些了,我们需要使用更加高级的命令,帮助我们来解决问题. 

