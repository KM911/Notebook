---
file-created: 2023 11 21
last-modified: 2023 11 26
---

## 传输大文件 比如视频会是什么情况呢? 

其实是会变成多个http请求
```
Status Code: 206 Partial Content
Content-Length: 1584893687                                 # 表示剩余的
Content-Range: bytes 47284224-1632177910/1632177911        # 已经请求到的
```

有意思的内容还有很多, 基本上每一请求的size

1114112   = 1024 * 1088 
这里又是为什么 ? 

也有部分请求大小为33kb(31.8 )和66kb(64.8 )的 可以看见还有1.2kb的数据不见了 估计请求头就有这么多了吧

```
HTTP/1.1 206 Partial Content
Server: Fiber_builde_by_km911
Date: Wed, 01 Nov 2023 13:48:02 GMT
Content-Type: video/mp4
Vary: Origin
Access-Control-Allow-Origin: *
Accept-Ranges: bytes
Last-Modified: Sat, 14 Oct 2023 11:08:04 GMT
Content-Range: bytes 16154624-1632177910/1632177911
Content-Length: 1616023287
```


> [!note] transferred data size smallerr than resource size
> In most cases, the resource size is smaller than the transferred size. There are a few possible reasons for this:
> Encoding data: Servers may encode data using methods like gzip and br to reduce its size.