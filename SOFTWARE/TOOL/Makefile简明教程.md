---
file-created: Thursday, November ,2023
last-modified: Saturday, November ,2023
---


## 前置知识

* 基本的命令行知识,了解过 `shell cmd`
* 最简单的编译命令,例如`gcc go build`.
* 简单了解C语言编译过程. [[何为编译]]

## 适用场景(c语言)

首先我们知道,`#include`是直接将其他的文件内容拷贝过来,这样直接编译该文件相当于,首先将other.c文件的内容拷贝过来,然后将整个项目文件编译,这样是很花费时间的,如果可以只编译修改了的文件,然后将其进行链接,实现增量编译,就可以提高编译速度.

重点: 增量编译 

```c
#include<other.c>
iny main(){
// do something 
}
```


## 适用场景(go)


我们假设你现在有一个 `go `的项目. 你想发布一个精简版需要以下命令. (编译优化和对exe文件进行压缩)

```
go build -ldflags="-s -w" && upx -9 *.exe
```

你有的时候还需要对文件进行调试

```
go build && app.exe 
```

如果想运行测试脚本

```
go test -v ./test
```

又或者是一个 `benchmark`

```
go test -bench=. -benchmem  ./benchmark
```

你会发现你需要重复键入大量的命名,而且很多的参数挺麻烦的,这个时候有没有一种工具可以帮助你管理这些命令呢?这个时候就需要我们的 `Makefile`

因为go本书就支持增量编译了,相对现代化一些的编译器基本上都支持增量编译的,可以理解为内置了一个Makefile的模板.对于go,虽然我们不能通过makefile实现增量编译,但是我们还是可以化简我们的命令,提高项目开发的效率.

这里的重点变成了 : 化简命令 



## Makefile

`makefile`的基本语法如下

```
[target]:
	[command]
```

```
build :
	go build -ldflags="-s -w"
```

`target` 是你需要的目标 ,例如当我执行命令 `make build` , makefile就会检查该目标是否达成,如果没有达成,就会执行下面的命令,达成目标.

`target`可以是一个文件名,这样就会检查文件是否存在,如果不存在就可以执行命令对其进行构建.

这里有一个问题? 如果我们只是希望执行命名,而不是检查文件,我们可以提前声明. `.PHONY` 表示这些目标都是没有完成,也就是一定会执行下面的命令,并且不用担心文件名和命令重名的情况.

```makefile
.PHONY: run build realse
```



## 高级用法

### 依赖目标

有的时候我们的目标依赖于其他的目标,这个时候就可以这样做了

```
[target]: [require]
	[command]
```

### list

这里其实是为了交叉编译 不然每次都是需要我们进行修改 感觉其实挺麻烦的 



## 基本的功能 我其实都还没有使用


1. 如果没有指定命令 `make` 默认执行第1条命令
2. 容错,如果某一条指令出现了错误 make将会终止 为了避免这种情况,请在指令前面添加 `-` 
3. 


## Win如何使用make

很不幸,make是linux的专属,因为是GNU项目下的,额这个问题其实就和如何在win上使用gcc一样,使用 mgw就好了.

这里导致的问题就在于, 会创建一个环境,你的如果想要使用绝对路径就会出问题,所以就不要使用了哦.



## 本人实践

我个人摸索出来来的比较好的方式. 


获取当前文件夹的名称 一般情况下都是作为我们最后的project name了不是吗 

```Makefile
pwd = $(shell pwd)   # /cygdrive/d/CODE/cpp/make_demo
project = $(notdir $(pwd)) # make_demo
```

简单替换非常繁琐的命令.
```make
release:
    go build -ldflags="-s -w" && upx -9 *.exe 
```

主要我也没有用c写过大的项目,所以其实无法真的很好体会到增量编译的好处.


这里列表 获取参数


思考一下 如果你将include全部的其他文件,本质其实就是将其复制粘贴到一起,就没有必要使用我们的 makefile
了,所以

目前我们的是main函数内部进行函数申明 然后 其他文件中进行定义 


基本上可以满足基本的C语言项目的开发了.

```makefile
pwd = $(shell pwd)
project = $(notdir $(pwd))
SRCS := $(wildcard *.c)
folders := $(wildcard */)
SRCS += $(foreach dir,$(folders),$(wildcard $(dir)*.c))
OBJS := $(patsubst %.c,%.o,$(SRCS))


CC = gcc
CFLAGS = -Wall -g


# 通用的C语言模板

run:$(project)
	./$(project)
$(project):all

all: $(OBJS)
	$(CC) $(CFLAGS)  $(OBJS) -L .  -o $(project)

build:
	$(CC) main.c -o $(project)

clean:
	-rm *.exe
	-rm *.o
	-rm *.out


# 测试我们的参数

pwd:
	@echo $(pwd)

project:
	@echo $(project)

src:
	@echo $(SRCS)

obj:
	@echo $(OBJS)

argv:
	@echo $@
folder:
	@echo $(folders)
```

我其实并不知道这里有多少命令 