---
file-created: 2023 11 15
last-modified: 2023 11 30
---

#### rust tool box

下面这些都是由rust编写的 CLI 工具. ( 如果你还不知道什么是rust的话,可以查看这个 []())

如果你是一个经验丰富的程序员,你应该试试看,因为它们或许有你喜欢的地方;如果你是一个新人,不是很了解shell和 linux ,你更加应该使用它们.

这些用rust重写的命令行工具,一般情况下这些工具都有下面的优点. 
* 更好的性能,比如硬件加速功能.
* 更美观,ASNI 输出结果带有颜色.
* 更有友好的使用方式和错误提示  
* 更简洁,没有历史遗留包袱.

缺点 
* 更多的资源占用,利用空间换时间的优化方式,输出ASNI带来的额外开销等等,不过基本可以忽略不计.
* 语法的不兼容,比如 nushell 采用了 ; 而不是 && ,有一定的迁移成本.
* 更高的学习成本,比如nu
* 
* 
![[Pasted image 20231007103113.webp]]

#### nu-shell
##### 推荐理由 

1. 美观,长得好看非常重要.
2. 友好,错误提示更加丰富.
3. 可扩展性. 
##### 安装环境

配置文件在 $env.APPDATA/nushell下

我们配置一些工具需要在config.nu下添加source xxx.nu的文件还是比较简单的 


[Starship](https://starship.rs/guide/#%F0%9F%9A%80-installation)
[GitHub - ajeetdsouza/zoxide: A smarter cd command. Supports all major shells.](https://github.com/ajeetdsouza/zoxide)
#### rust命令行工具速览

| 命令      | 替换目标 | 特色                | cargo源码安装 | 推荐指数   |
| --------- | -------- | ------------------- | ------------- | ---------- |
| fd        | find     | 高性能 命令友好     | fd-find       | 🌟🌟🌟🌟   |
| rg        | grep     | 高性能              | ripgrep       | 🌟🌟🌟🌟🌟 |
| z         | cd       | 记录路径            | zoxide        | 🌟🌟🌟🌟🌟 |
| gping     | ping     | 绘制图表            | gping         | 🌟🌟🌟     |
| grex      | 无       | 生成正则表达式      | grex          | 🌟🌟🌟🌟   |
| nu        | bash     | 现代化shell         | nu            | 🌟🌟🌟🌟🌟 |
| dust      | du       | 树状结构输出        | du-dust       | 🌟🌟       |
| hx        | vim      | 易于上手 更加现代化 | helix         | 🌟🌟🌟🌟🌟 |
| hyperfine | 无       | 命令行benchmark     | hyperfine     | 🌟🌟🌟🌟🌟 |
| starship  | 无       | 友好                | starship      | 🌟🌟🌟🌟🌟 |
| btm       | top      | 友好                | bottom        | 🌟🌟       |
| bat       | cat      | 代码高亮            | bat           | 🌟🌟🌟🌟🌟 |
| tokei     | 无       | 代码数量统计        | tokei         | 🌟🌟🌟🌟   |
| broot     |          |                     |               |            |
| zellij    | tmux     |                     | zellij        |            |

可以使用如下的脚本进行安装.
```bash

```