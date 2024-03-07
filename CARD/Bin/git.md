
#### 理解git
>[!note] 基于change的版本管理. 

理解了这一点其实你就可以理解全部了.
##### github可视化工具
github desktop 这里有一个问题,你的电脑通常情况下会有一个git,但是github desktop会携带一个并且使用它,导致你的部分配置可能不会生效.
#### git的配置
屏蔽掉我们whitespace
```bash
git config diff.ignoreWhitespace true
```
#### 常用命令
##### 创建一个完全新的分支
会保留全部文件. 用于清理历史提交记录.
```bash
git checkout --orphan <branch-name>
```
##### 同步分支修改
两条分支,基于同一个commit创建的,A分支有了一个提交,现在B分支想要获取.


## 一个奇怪的bug

win下clone该仓库,会无法构建. 

需要切换到linux环境下, 使用`git reset --hard` 就可以了 .

```bash
## output 目标文件 
D:\CODE\linux-zh\Documentation\output\teaching
 # rst 目标文件

D:\CODE\linux-zh\Documentation\teaching

```



[[gitignore]]