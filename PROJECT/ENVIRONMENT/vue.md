---
file-created: 2023 11 04
last-modified: 2023 11 29
---

## 利用脚手架初始化项目

```bash
npm init vue@latest
```


组件库 [Installation | Element Plus](https://element-plus.gitee.io/en-US/guide/installation.html#using-package-manager)
路由管理 [Installation | Vue Router](https://router.vuejs.org/installation.html)
状态管理 [Introduction | Pinia](https://pinia.vuejs.org/introduction.html)

## vite 

```bash
vite --open 
```
将会启动一个web server,这个web server会提供vue的编译后的结果,其实只是没有写到磁盘上,缓存到内存罢了,不可能真的不用编译,因为操作内存相对速度还是比较快的. 

### request has been blocked by CORS policy

当我们第一次使用axios时,假设请求百度做一个测试.
```js
  axios.get("https://www.baidu.com").then(res => {
    console.log(res)
  }).catch(err => {
    console.log(err)
  })
```

然后你就可以收获到如下的报错.  
>[!error] Access to XMLHttpRequest at 'https://www.baidu.com/' from origin 'http://localhost:5173' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.

其实报错信息非常明确了, <span class="r">request has been blocked by CORS policy </span> 我们直接去了解一下什么[[CORS]].

### 解决方案

1. 修改`server`的` AllowOrigins: "*"` 

这样就是告诉浏览器,我这个请求可以被任何域名请求, 既然你都这么说了,浏览器也不好说什么. 

2. 使用vite proxy

既然浏览器会进行[[CORS]]检查,那么我们就用代理服务器去请求就好了. 所谓`代理`就是请别人用自己的身份替自己做事. 

>[! important]- 开发/部署环境一致性问题
>开发时,我们会利用vite启动一个server,端口为3000,如果你某个接口的url是 "http://localhost:3000/server/xxx" 等到部署完成后,用户的浏览器还是会请求该路径,你觉得可以请求成功吗?
>
>正确的做法是: 将请求接口使用相对路径,比如 "/server/hello" , 这样用户浏览器的请求就可以被正确接收了.

```js
  server: {
    port: 3000,
    proxy: {
      "/server": {
      // localhost:3000/server/test -->   http://server_host:4000/server/teest
        target: "http://server_host:4000/server", 
        changeOrigin:true, 
      },
    },
  },
```

>[!error]- 奇怪
>目前如果将target设置为 `localhost`将会出现问题,但是`127.0.0.1`就不会,有待深入考证. 
#### 理解vite proxy做了什么


针对浏览器跨域问题,现在我可以给出一个更好的答案了. 

>[!note] 浏览器提供的一种安全机制. 
> 假设你的网站是aaa.com,你的网站有很多图片视频等资源 url为 aaa.com/resources 
> 其他人直接将你的图片链接复制,放到了自己的网站中,假设是 bbb.com . 浏览器认为这样是不合理的,因为直接其他域名下的内容是否侵犯了他人不说,如果这个其他域名的文件是一个病毒或者是可能损害计算机的内容,就应该阻止该请求, 当然了还是存在了CDN哎. 

你可以将上面的代理理解为下面的`express`项目代码.

```js
app.use("/server",function(req,res){
  let RootUrl = "http://127.0.0.1:4000"+req.baseUrl
  console.log(RootUrl);
  axios.get(RootUrl).then((axios_res)=>{
    res.send(axios_res.data)
  }).catch((err)=>{
    console.log("request error")
    console.log(err);
  })
})
```
## 防盗链是什么 ? 

我们已经知道了浏览器发送请求和我们利用`socket`发送请求没有任何区别. 如果非要说区别,那就是浏览器会自动添加一些信息标明身份, 比如`User-Agent`. 如果一张图片可以被浏览器访问,肯定也可以被其他的程序访问. 



