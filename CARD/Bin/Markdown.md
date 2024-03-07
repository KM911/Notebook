---
file-created: 2023 11 23
last-modified: 2023 11 30
---

## Markdown规范

如果问我是否存在一种大家普遍认可的Markdown规范,我认为 [Github](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)  的Markdown规范是最被广泛接收的. 

但是坏消息是,就如同C语言的编译器实现一样,各个编辑器都声称支持markdown,但是具体的细节语法不太一致,最后的渲染结果也不保证. 

所以从这个角度来看说,就不存在统一的markdown的语法规范. 所以我喜欢自己写一个语法笔记用于测试其渲染效果.

## 基本语法


| 元素 | 语法 |
| :--: | ---- |
| 标题 | #  ## 数目表示 几级标题 |
| 超链接  | `[显示的内容](链接)` |
| 代码 | `code` 利用两个 ` 多行代码就是 三个 |
| 分割线 | `---`  — 或者 `***` |
| 高亮 | `==高亮==` ==高亮== |
| 加粗 | `**加粗**`  **加粗的字体** |
| 加粗斜体 | `***加起来***`   ***加粗斜体*** |
| 任务清单 | `- [ ]` -[ ] `- [X]` |
| 删除线 | `~~删除的内容~~`~~被删除了~~ |
| 图片 | `![image](图片位置)` |
| 无序列表 | 利用没有人用的符号 比如 `+ *` |
| 斜体 | `*倾斜*`*倾斜的字体* |
| 引用 | `>`  有的引用是 tab 笑死我了 |
| 有序列表 | 1. 2.  数字. 部分软件支持自动计数 |


## 高级语法

*脚注*
格式的内容和typora是一致的.


比如你需要说明 linux[^GUN/linux] 

脚注不会实时预览有点麻烦



[^GUN/linux]: 虽然我们日常喜欢只讨论



### 插入html

利用这个你可以比较方便的去修改字体的颜色 <span class='c3'>color</span>，当然了前提是你已经编写好了足够方便的css文件.



### 数学符号

[符号表](https://www.cnblogs.com/ywsun/p/14271547.html)




# 测试样式 一级标题

## 二级标题

### 三级标题

#### 四级标题

## 字体效果渲染

* 1
* 2

*斜体*

**加粗**



| 表   | 格   |
| ---- | ---- |
| 测   | cs   |



![B站图床测试](https://i0.hdslb.com/bfs/album/311120bb5abbf9afc1a351068a24e6753ab08c2e.png)



[链接测试_我的博客](https://km911.github.io/BLOG)



数学公式

$\int_a^b  sin(x) + \frac{1}{2}$



````yaml
代码的高亮测试
# KaTeX
katex:
  enable: false
  per_page: false
  hide_scrollbar: true
````



* typora表情 :cry: 
* emoje 😂



## 测试mermaid

[[Mermaid]]