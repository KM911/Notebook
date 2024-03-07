---
file-created: 2023 11 25
last-modified: 2023 11 29
---
Content-Type: application/x-www-form-urlencoded

这里我记得让我头疼了好久 让我拿过死了. 

不过当前确实是没有仔细去研究 还是有非常多的内容的不是. 

### 响应标头
#### Strict-Transport-Security

告诉浏览器只能通过https访问，不能通过http访问

当服务器返回这个响应头时，浏览器会记住该设置，即使下次用户使用http访问，浏览器也会自动使用https进行发送。

哈哈，如果第一次使用域名访问网站的时候是http呢，会不会让你访问？
它是做一个重定向，重定向使用https，感觉好骚啊，我下面有图有真相，我有三个浏览器。

![[Pasted image 20231120222936.webp]]

#### Content-encoding
资源所采用的压缩方式 [[PROJECT/SCHEME/nginx#GZip Br|Gzip and br]]


#### Cache-control 
用来标识该资源的过期时间

如果需要缓存，那么`Cache-control` 的值中一定会包含 max-age:value
value的单位为秒。意思就是在这个时间段内，请求不会发送给服务器，而是直接从内存中读取。

#### ETag

ETag 在nginx之中是默认打开的，如果想关掉，那么就` etag off; `写在Server外面。

服务器根据资源内容或者版本号生成的唯一的字符串。 事实上，只要你可以实现用一串字符 '标识资源当前的状态' ,那么这一串字符就可以作为ETag。

进行 [[网络优化#Local Storage|协商缓存]] 的时候才会使用到ETag



[[Header#If_None_Match|If-None-Match]] 的值并不一定与服务器响应的ETag相同，可能会在ETag值的基础上加W/,假如If-None-Match的值是携带W/(ETag) 的话，那表明只需要两个资源在语义上是相同的就好了(弱校验)。


表面上是这样的，那么什么时候会出现从磁盘（内存）中读取，什么时候不会呢？
![[Pasted image 20231121082819.webp]]
浏览器会响应给我们字段标识内容的缓存时间。
Expires 是http 1.0时候的header，同时使用 会被 Cache-Control(http 1.1)覆盖，主要作用还是兼容旧客户端。

##### 关于ETag的值
nginx 不支持自定义ETag值的算法.
###### nginx实现ETag源码

```c
    etag->value.len = ngx_sprintf(
                                etag->value.data, "\"%xT-%xO\"",
                                r->headers_out.last_modified_time,
                                r->headers_out.content_length_n
                                )
                      - etag->value.data;

    r->headers_out.etag = etag;
```
可以看到，在 nginx 中，ETag的值是根据最后修改时间和内容长度来计算ETag值的。
###### 自定义ETag的值
```python
import hashlib
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def index():

    content = "hello world"
    etag = hash(content) #我直接使用hash值，只要保证此刻状态即可

    response = Response(content, 200)
    response.headers['Etag'] = etag

    response.headers['Cache-Control'] = 'max-age=60'

    if_none_match = request.headers.get('If-None-Match')
    if if_none_match == etag:
        response.status_code = 304

    return response


app.run(debug=True)

```


#### 通过Last-modified判断资源是否更改

<span style="color:gold">可行！</span>

那为什么要多出一个ETag字段出来呢，Last-modified的时间精度为秒，也就是说在1s内完成操作退出一气呵成，Last-modified的值就不会改变。
    这简直刷新认知，感觉跟胡说的一样，当然也有一定道理。

>[!note]
>我觉得能够修改文件的时间 并不能成为我们不使用Last-modified来判断是否更新缓存的理由  网站上的资源都是在服务器上的，闲的没事干了去写脚本修改文件时间，让用户缓存都失效，毫无利益可言，感觉不会有人做这样的事情。

但是，刚去尝试了一下，使用vim打开文件，胡写一串然后删除，最后无法使用q退出
![[Pasted image 20231122102731.webp]]
使用ls -l 查看最后修改时间，时间是改变的。
事实上，只要发生了写，删除操作，这就会引起最后修改时间的改变。操作系统不管你的内容。

这才是拿来回答为什么会多用ETag的原因我觉得，因为仅仅通过判断修改时间的不同就重传，浪费了。

缺点：
1. 是的，照这种方法下去，nginx算法下的ETag的值也会改变，真小丑。
2. 甚至，根据stackoverflow老哥们的看法，如果在1秒内做多次修改，它的ETag值都不会变......
3. 而且两个文件，假如文件大小一样，最后修改时间也一样，内容不同，ETag的值也是相同的。


但是一想，尽然有这么多的问题，那为什么不用更能反映精确度的 资源内容的hash值呢？ (apche http服务器就是用这种)

可能是计算哈希值的开销比较大吧，你要根据内容计算哈希值，又读取，又计算。
不如直接根据大小和最后更改时间来计算一个，省点服务器开销。

我们的nginx并不支持我们自定义ETag的值


自定义ETag的值，不过通过Server值也看的出来，这并不是我们正常的http服务器，浏览器依然在下次的请求之中携带了 If_None_Match 请求头。

![[Pasted image 20231122144241.webp]]


<span style="color:red">这只是目前的看法，请速度批评指正</span>






这里有[ETag介绍](https://www.fastly.com/blog/etags-what-they-are-and-how-to-use-them)  [RFC文档](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3)

浏览器在看见响应中的ETag时，会在下次请求中携带if_None_Match。这是http协议的一部分，所以这应该能够解释浏览器为什么认得ETag吧。








#### Content-encoding
这个说的是该资源采用的压缩方式 gzip br。

#### Date
表示 服务器返回该响应的时间，使用的 格林威治时间，我们是北京时间，所以我们减少8小时，时间就和这个字段的值对应了。

Last-Modified 表示资源的最后一次更改时间。
Server 表示服务器所使用的软件或者版本

#### Vary 

Vary的值 是一个请求标头的字段，也就是说，只有Accept-Encoding相同的请求才可以使用服务器已经缓存的数据。
有的浏览器就不支持br压缩，但是你上次请求缓存了一个经过br压缩的副本，你给它返回br压缩的内容会出问题，这只是举个例子，说明主要功能。
![[Pasted image 20231121091345.webp]]

nginx配置文件中可以在此处开启Vary，这个打开之后的效果就是上图的Vary效果。
![[Pasted image 20231121092357.webp]]

#### Alt-Svc

Alt-Svc:h3=":443"; ma=86400
表示我们还有一个备用服务，在443端口，使用的是http3协议，这个信息在接下来的一天内有效。

http3 使用QUIC协议作为传输层协议，21年被定位标准，但目前还没有普及


### 请求标头
我感觉这里有多好字段啊。


这四个请求头是http 2.0的产物，是用来代替请求行 (http 1.1) 的
![[Pasted image 20231121095502.webp]]

#### Accept
这个也是非常好理解的，表示浏览器接收什么类型的文件
如果是*/* 那表示接收任意类型的资源。
假如服务器不能返回这个字段值之中的响应，那么就会返回406 Not Acceptable

##### Accept-Encoding:

>browser could decoding type 

>default: gzip, deflate, br


##### Accept-Language
表示客户端优先接受什么类型语言的响应
![[Pasted image 20231121104246.webp]]
表示优先接收中国中文，其次接受任何中文，q=0.9 可以理解为偏好程度。
假如有多种语言，就可以根据q值返回优先程度较高的。
#### 浏览器自动添加的请求头
sec开头的都说是由谷歌浏览器添加的
![[Pasted image 20231121104735.webp]]

User-Agent 包含了发起请求的客户端信息。
##### Origin

主要用于实现跨源资源共享（CORS）,它告诉服务器请求是从哪个源发起的。
如果服务器允许跨域，那么就会响应一个 Access-Control-Allow-Origin 头，值通常和Origin匹配，也可以直接是一个通配符* ，表示任何源的请求都可以请求资源。
由浏览器控制，不由js控制。
##### Referer

由浏览器控制，不由js控制。
告诉服务器这个请求从哪个页面来的。
##### If_None_Match

进行协商缓存的时候，会携带该请求头，它的值一般与 [[Header#ETag|ETag]] 相同
服务器会拿该字段的值与服务器重新计算出来的ETag值比较，如果相同，返回304，否则就将新的资源返回，状态码200。





### 跨域资源共享响应头

表示在请求中可以使用哪些头部，如果为空，表示的是不允许[[Header#添加自定义字段|自定义头部]] 被使用
Access-Control-Allow-Headers: 

表示在请求中可以使用哪些方法
Access-Control-Allow-Methods: Get,post

表示允许哪些源访问资源
Access-Control-Allow-Origin: https://debudzg.top



### 添加自定义字段
我们也可以添加我们想添加的任何字段，不过浏览器解析不了我们的字段是啥意思，等自己解析的时候就有点用了。(可能吧)

在nginx的虚拟服务器之中，也就是Server之中使用
            add_header name  "value" ;
eg：
![[Pasted image 20231121093606.webp]]
效果：
![[Pasted image 20231121093644.webp]]


### 修改文件最后修改时间代码
下面是windows中修改文件时间的代码
修改文件时间的C语言代码
```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <utime.h>
#include <time.h>
#include <assert.h>
#include <string.h>

int modify_file_time(const char *path, char *date)
{

    int num_array[6]; // 假设我们最多有 10 个数字
    int count = 0;

    char *token = strtok(date, "[,]"); // 使用 '[', ',' 和 ']' 作为分隔符
    while (token != NULL)
    {
        num_array[count++] = atoi(token); // 将字符串转换为整数并存储在数组中
        token = strtok(NULL, "[,]");      // 继续分割字符串
    }

    struct utimbuf new_times;

    struct tm new_time;
    new_time.tm_year = num_array[0] - 1900; // 年份，从 1900 年开始
    new_time.tm_mon = num_array[1];         // 月份，从 0 开始
    new_time.tm_mday = num_array[2];        // 日期，从 1 开始
    new_time.tm_hour = num_array[3];
    new_time.tm_min = num_array[4];
    new_time.tm_sec = num_array[5];

    new_times.actime = mktime(&new_time);
    new_times.modtime = mktime(&new_time);
    if (utime(path, &new_times) < 0)
    {
        perror(path);
        return -1;
    }

    return 0;
}

int main(int argc, char *argv[])
{

    assert(argc == 3);

    int flag = modify_file_time(argv[1], argv[2]);

    if (flag == 0)
    {
        printf("文件时间修改成功\n");
    }
    else
    {
        printf("文件时间修改失败\n");
    }
    return 0;
}

```

编译后传递 filename  "[年，月，日，时，分，秒]"

![[Pasted image 20231121214028.webp]]





