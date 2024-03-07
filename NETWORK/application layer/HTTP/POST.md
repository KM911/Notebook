---
file-created: 2023 11 01
last-modified: 2023 11 29
---
from表单提交 

```html
<form action='http://localhost:3000/file' method='post'>
      <input type='text' name='username'/>
      <input type='password' name='password'/>
      <input type='submit' value='登录'/> 
 </form>
```

提交的内容是存放到body中的, 其中值得注意的是请求头的`Content-Type v [application/x-www-form-urlencoded]`

内容还是存放在body里
```bash
ctx.body username=123&password=123
```

解析的方式是 ` ctx.FormValue("username")`

from表单提交文件

```html
<form action="http://localhost:3000/file" enctype="multipart/form-data" method="post">
  <input type="file" name="name"/>
  <input type="submit" value="提交">
</form>
```

`Content-Type v [multipart/form-data; boundary=----WebKitFormBoundaryrX3sLbkQZSibBZqs]`
Content-Length:
Accept-Ranges: bytes
Content-Disposition: attachment; filename=main.go
Vary: Origin
Last-Modified: Tue, 31 Oct 2023 12:23:18 GMT
If-Modified-Since: Tue, 31 Oct 2023 12:23:18 GMT

解析方式是 `file, _ := ctx.FormFile("name")`

内容变成了二进制数据,我们尝试写入一下. 写入错误了,我们会发现文件头部存在额外信息.

```txt
-----WebKitFormBoundaryz5CJ1BuMwHVI5Jfj                                                 Content-Disposition: form-data; name="name"; filename="æœªå¡«å†™éƒ¨åˆ†(1).doc"          Content-Type: application/msword  
```

这里的Content-Type是浏览器自动设置的 , 不是我设置的, 
## 文件续传 


## 分片上传
为什么不能使用文件名,因为文件名可以重复,一个可以唯一表示文件, 文件hash

spark-md5 增量计算

web worker


## 分片组合

what is byte range 这个就是文件


nginx会限制单个http请求的大小,之前做项目的时候其实也遇到了. 

