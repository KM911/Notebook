---
file-created: 2023 12 01
last-modified: 2023 12 01
---

## 插件教程

[Extension_Kanban](Extension_Kanban.md)

>[!note] 目前使用的第三方插件
>- [ ]  Auto Link Title 复制链接会自动将网站title复制
>- [ ]  [[Callout Manage]]  管理callout
>- [ ]  Custom Frame 内嵌网页
>- [ ]  Clear Unused Image 会将没有使用的文件都删除 所以小心
>- [ ]  CustomJS 和 Dataview 这两个需要配合联动使用 前者提供js支持,后者提供dataview的api供你进行文档内的查询. 
>- [ ]  emoji Toolbar 文件夹也有表情了
>- [ ]  Keyboard Analyse 用于可视化查询快捷键,帮助你学习和记忆快捷键
>- [ ]    [[Execute Code]] Run code in code block. 
>- [ ]    templater templat 增强

>[!others]- 废弃的/不常用的
>Advance Table 官方新的版本支持表格编辑了.
### 内嵌网页

> [!done] feature 
> 1.在笔记内部实现一边看视频一边记笔记的体验.
> 2.保留cookie,完整用户体验.
> 3. 
> 

## 官方插件

### 日记插件

>[!info] 提供的功能
> 1. 复制模板
> 2. 填写时间

### 模板插件

官方的不足以满足我们的要求,还是需要使用插件进行增强. 


## 为obsidian提供更多函数支持 

>[!note] 前提
>1. execute-code 让我们可以在笔记总执行代码
>2. 利用python进行字符串处理,修改笔记内容 

### 规范 

>[!note] 代码格式 
>```python
import os
os.system("python "+@vault_path+"/RESOURCE/CODE/function/test_argv.py "+@vault_path+"/"+@note_path)
>```

>[!note] 代码存放位置 : /RESOURCE/CODE/function/xxx.py

>[!note] 参数解析 
> sys.argv[1] = 当前文件绝对路径


