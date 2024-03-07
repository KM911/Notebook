
>[!note] github 推出的CI/CD服务. 

## 开始使用

>[!note] GitHub Action 采用[[Configuration Files#Yaml|Yaml]]文件作为配置文件. 

>[!note] 在你的git项目中创建环境. 
>touch /.github/workflows/xx.yml

>[!faq] 配置文件中需要写什么? 
>其实就是回答这几个问题. 
>1.Action 名称
>2.Action 什么时候触发执行
>3.Action 具体做什么 

>[!tip] 对应到yaml文件中
>1. name: your_action_name
>2. on: 具体执行策略
>3. jobs: 执行的操作 

>[!note] 我们其实已经介绍了核心 concept
>现在让我们深入了解它们. 


### on 

>[!example] 
>```yaml
> on:
>   push:
>     branches:
>       - master
>   pull_request:
>     branches:
>       - master    
>```

>[!note] push 和 pull_request说明在什么操作下触发Action
>branches,说明考虑的分支. 
>

>[!note] 可选的动作有 : push pull_request 




### jobs




## 案例讲解

- [x] [[Github Action#创建go的环境]]
- [x] [[Github Action#hexo 的案例]]
- [ ] 部署到服务器

## 创建go的环境

```yml
# workflow 的名称
name: Go
# 触发的条件
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  # build 任务
  build:
  	# 选择机器环境 基本上都是Ubuntu了 哈哈哈
    runs-on: ubuntu-latest
    
    steps:
  	# 小任务的名称
    - name: pull code on ubuntu
      # uses 就是使用一些特殊的指令
      # checkout 就是 git pull
      uses: actions/checkout@v3

    - name: Set up Go
      # a action for set up go 
      uses: actions/setup-go@v3
      # with argvs 
      with:
        go-version: 1.19

    - name: Build
	  # run command 
	  run: go build -v ./...

    - name: Test
      run: go test -v ./...

```

### 创建GITHUB_TOKEN

一些比较特殊的项目比如GitHub action中进行静态网页的部署工作,需要将build好的代码放到一个新的分支

```

```

很多教程都讲错了,说是ssh的token,关键是我一开始也觉得有道理,把pub_key添加后,发现还是无效,哎.

settings 中的token 只会显示一会哦,需要保存下来.

将其添加到仓库中就好了.



## hexo 的案例 

这里似乎有问题 如果使用ubuntu的版本过劳 会一次处在 queue的状态 

![image-20230427173146985](http://81.68.91.70/pg/image/KMiNnv7G0T4C.png)

```yaml
name: HEXO

on: push

jobs:
  build:
    runs-on: ubuntu-18.04

steps:
- uses: actions/checkout@v2
 
# Cache node modules to speed up build
- name: Cache node modules
  uses: actions/cache@v2
  env:
    cache-name: cache-node-modules
  with:
    # npm cache files are stored in `~/.npm` on Linux/macOS
    path: ~/.npm
    key: ${{ runner.os }}-build-${{ env.cache-name }}-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-build-${{ env.cache-name }}-
      ${{ runner.os }}-build-
      ${{ runner.os }}-
 
- name: Install Dependencies
  run: npm install
 
- name: Build
  run: npm run build 
         
- name: publish and push
  uses: peaceiris/actions-gh-pages@v3
  with:
    github_token: ${{ secrets.TEST_TOKEN }}
    publish_dir: ./public
```









## 静态页面部署

对于静态页面部署 可以说是没有任何的难度了 

只需要你创建仓库 然后导入就好了 像GitHub pages 和 vercel 都会自动的为你部署文件

## 动态页面部署

我们其实是可以利用api 实现动态页面的 但是有一些限制 就是你不能修改路由 

项目的结构 必须 和 网站的结构一致 （当然了 现在的我还没有接触过vue 和 react 这样的框架 很多话可能都是错误的）

## API 部署

首先我们要明白一件事情 我们的vercel.app是运行在一个只读的文件系统上的 所以我们不能进行存储的相关功能 但是其实还是的 可以保存到本地然后push上去就好了 (vercel好像有100GB的存储空间 真的用不完) 

Vercel 会自动创建一个server 我们只需要按照它的格式书写api就好了

`api/index.js`  

两种书写方式 ES6 和 commonjs

```js
// index.js commonjs
module.exports = async (req, res) => {
    // 其实这个也是ES6的语法 为什么会不兼容? 
  const { id, theme } = req.query; 
  const data = await getBilibiliInfo(id);
  data.theme = theme;
  res.setHeader('Content-Type', 'image/svg+xml');
  res.setHeader('Cache-Control', `public, max-age=${6000}`);
  return res.send(renderBilibiliCard(data));
};

```

为了实现本地的测试 我们可以创建一个 `app.js` 不然的话只能部署到vercel后才可以查看

```js
const express = require('express');
const app = express();

const index = require("./api/index")
app.use("/api",index) // get请求会交给我们的index 处理
app.listen(3000)
```

**ES6的写法** 

```js
// index.js ES6
export default async (req, res) => {
    res.end("hello world")
}
```

同样的我们创建一个`app.js`用于本地测试

```js
// app.js
import express from 'express';
let app = express();
import index from './api/index.js';
app.use("/api", index);
app.listen(3000);
```

引入其他模块

```js
// render.js 
function render(text) {
    return text + "调用了render方法";
}
export default render;
```

```js
// 在index.js 里写下
import render from "../render.js"
export default async (req, res) => {
    res.end(render("hello world"))
}
```


 
# 项目参考

[GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats)
