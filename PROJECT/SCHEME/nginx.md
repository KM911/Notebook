---
file-created: 星期三, 十一月 ,2023
last-modified: 星期日, 十一月 ,2023
---
## 最简配置

这里的配置应该是会影响到功能的配置,上面的环境搭建的配置是为了服务可以启动,可以登陆. 不太会设计到性能和trade off相关的事宜. 


这里添加一个cook book就好了. 
### hello world (nginx版本)

```nginx
worker_processes 1;
events {
    worker_connections 1024;
}
http{
  include mime.types;
  default_type application/octet-stream;
  sendfile on;
  keepalive_timeout 65;
  server {
    listen 80;
    server_name localhost;
    location / {
      root /www/wwwroot/app/public/BLOG ;
      index index.html index.htm;
    }
  }
}
```

## 基础命令 

### location

假设我们的 css文件都是 www/web/css/* .css 这样的形式存储的 我们可以写这样的语句,当 nginx 发现请求的路径中包含 /css 时，它就会去 /www/web/css 下寻找资源 。
```nginx
location /css{
	root /www/web
}
```

不同的资源在浏览器中有不同的处理方法，在一次请求的响应头中有一个叫做
`Content-type`的字段，它告诉浏览器要将该次请求的资源按照该字段的值进行处理。

nginx 中有一行配置是 `include mime.types` 这个mime.types定义了文件扩展名与文件类型的映射关系。
让我们去看看吧 它存放在我们的nginx目录中的conf文件夹下
执行 `vim mime.types`

```nginx
types {
    text/html                                        html htm shtml;
    text/css                                         css;
    text/xml                                         xml;
    image/gif                                        gif;
    image/jpeg                                       jpeg jpg;
    application/javascript                           js;
    application/atom+xml                             atom;
    application/rss+xml                              rss;

    text/mathml                                      mml;
    text/plain                                       txt;
    text/vnd.sun.j2me.app-descriptor                 jad;
    text/vnd.wap.wml                                 wml;
    text/x-component                                 htc;
    ......
```

这里是并不是为了说明文件的类型, 而是让浏览器知道如何处理文件
假如文件的后缀与右边一列的某一个匹配，假如是html，那么浏览器得到的响应头`content-type` 字段的值就是 text/html

浏览器最终会根据这个字段的值 来决定如何显示响应体的内容。
是对该文件进行下载 还是运行 js 或者渲染 html


这是我将mime.types中css那一行改为了 text/html 之后发生的事，浏览器已经无法正确的渲染css了.
![[Pasted image 20231122212046.webp]]

如果你的文件扩展名没有被配置到mime.types,那么它将以默认的文件类型返回给浏览器。`default_type application/octet-stream;` 这表示默认类型为 下载




### proxy_pass 

>[!faq]- http/https分别暴露80和443端口,因为端口占用的问题,我们岂不是只能运行两个web服务了?
> 1.每次访问对应服务都通过其对应端口号访问? 增加url的复杂度,不方便记忆
> 2.使用非443端口可以使用https吗?
> 3.
>


>[!done] 请求转发
>我们可以对请求进行转发,比如请求路径以`/spring`为开头的请求,转发到8080端口,`/node`的请求转发到3000端口,这样你只需要对外暴露部分端口了.

>[!bug]- 端口安全
>有一种说法是,端口暴露在外是不安全的,这句话大部分情况下都是正确的,但是也要考虑实际. 也要知道这里的安全是在指什么. 
>> [!example]- mysql服务运行在3306端口上,你将3306端口暴露在网络上. 
>> 这样肯定是不安全的,因为其他人可以尝试去连接你的数据库,如果你的密码是弱密码,类似于123456,又或者因为其他原因被他人拿到了root密码,他人可以直接对于你的数据库进行操作. 这样肯定是不安全的. 当然了你也可以设置比如不允许远程连接,不过这里的安全是mysql为你提供的了.
>
>> [!example]- springboot项目运行在8080端口上,但是没有对外暴露,nginx会将全部的请求转发到8080上. 
>> 这样的结果,暴露了和没有暴露有区别吗? 如果项目操作操作数据库是直接拼接字符串并且没有做校验,会被[[sql注入]]吗? 这样安全吗? 通过不暴露8080端口可以提高安全性吗? 


```nginx
location /tinypicog{
	proxy_pass localhost:8080;
}

location /proxy {
	proxy_pass localhost:8000;
}
```


举例说明 :
假设用户的客户端发来的请求是 
http://11.22.33.44/api/login
经过我们的nginx之后
会变成 
http://localhost:8080/api/login
```nginx
location /api {
    proxy_pass http://localhost:8080;
}
```

<span style="color:gold">下面的配置是另外一种结果</span>

```nginx
location /api {
    proxy_pass http://localhost:8080/;
}
```
我们服务端最终接收到的请求会变成
http://localhost:8080/login

>[!note] 一句话总结,如果结尾不带`/`,就会将全部的路径进行转发;反之转发匹配的字段后的部分. 





### sendfile 

是否进行缓存 还是直接发送 这里很明显对于大批量请求 还是需要做缓存的 小请求可以就是

开启 sendfile 命令之后，用户请求过来之后，我们的nginx会根据配置文件去到响应的目录中寻找文件，找到之后，是否开启 <span style="color:gold">sendfile</span> 就会对接下来的流程产生影响。

不开启，那么找到文件之后，就会首先读取到nginx的内存中，然后再复制给网络接口，网络接口再返回给用户。

开启之后，nginx就不会去读取需要的文件，而是给我们的网络接口发送一个sendfile()信号，这其中包括着 文件描述符fd 以及socket 等信息，然后让网络接口去读取文件，这样就少了一次
read write 的操作，没错，这就是零拷贝

它的作用就是允许内核直接将数据从文件系统缓存直接发送到网络接口，避免了在用户空间和内核空间之间复制数据的开销。

#### 是不是开启总是有帮助的

根据网上的资料，小文件使用这个方式并不是最佳的，相反，使用传统的读/写反而更好。
你可能会说，传统方式有两次系统调用，但是sendfile只有一次，它虽然只有一次，但是系统调用的过程更加复杂，syscall的执行过程亦有差异。

操作系统对于小文件的读写有优化，在进行读写不会消耗太多CPU以及内存资源。
但是当进行sendfile时，sendfile 自身进行的除了读写以外的内容时所消耗的资源可能就已经相当于一次读写了，甚至更高，如果是大文件，这部分的消耗与大文件的读写差别比较大，可以忽略。

所以它的开启与否与获取的文件的大小有关，如果是大量小文件，不开启可能是一个更加合适的选择。

另外 动态的内容开启这个选项也不合适，调用一次 sendfile 找到的文件会存储在 系统文件缓存中，如果内容是一直在改变的，那么系统文件的缓存就需要一直改变，这也是开销啊是不是。

我曾在写之前想到，什么鬼网站会只有小文件的，那不还是默认开启吗，当然这个想法很快就否定了，因为我不知道什么文件是小文件。

<span style="color:skyblue">"小文件"的定义可能会因环境和上下文的不同而有所不同，但通常，我们可以将几KB到几MB的文件视为小文件。</span>

### URLRewrite配置伪静态





### GZip Br

>[!example]- 开启gzip
>```nginx
> gzip on;
> gzip_min_length  1k;   # 当文件大小大于1k才会开启压缩
> gzip_buffers     4 16k;   # buffer 
> gzip_http_version 1.1;   # 对 http1.1 进行压缩
> gzip_comp_level 5;  # 压缩的程度 1-9 数字越大 压缩程度越高,但是会增大cpu的占用
> gzip_types     text/plain application/javascript application/x-javascript text/javascript text/css application/xml;  # 针对何种格式的文件进行压缩    
> gzip_vary on;
> gzip_proxied   expired no-cache no-store private auth;
> gzip_disable   "MSIE [1-6]\.";
> ```

#### 开启br

br nginx不默认支持,需要我们重新编译nginx. 

```shell
$ cd /usr/local/src/
$ git clone https://github.com/google/ngx_brotli
$ cd ngx_brotli
$ git submodule update --init
```

之后进入我们的 nginx 刚刚解压之后的哪个目录
![[Pasted image 20231113215539.webp]]
```shell
$ ./configure --prefix=/usr/local/nginx  
 --add-module=/usr/local/src/ngx_brotli  --with-http_ssl_module
$ make
```
make 之后如果你报错, 类似于这个
```txt
/usr/bin/ld: 找不到 -lbrotlienc
/usr/bin/ld: 找不到 -lbrotlicommon
collect2: 错误：ld 返回 1
make[1]: *** [objs/nginx] 错误 1
make[1]: 离开目录“/usr/local/nginx-1.24.0”
make: *** [build] 错误 2
nginx编译出现这个错误
```
那不妨执行
```shell
$ yum install -y brotli brotli-devel
```
再执行
```shell
$ ./configure --prefix=/usr/local/nginx  
 --add-module=/usr/local/src/ngx_brotli  --with-http_ssl_module
$ make
```

大概率就不再报错了，然后
```shell
$ cd objs
$ cp nginx /usr/local/nginx/sbin
```

会问你是否覆盖，如果你已经停了nginx服务，什么信息都没有

然后你去nginx.conf文件中配置br
>[!example] 开启br
>```nginx
brotli on;
brotli_static on;
brotli_types text/plain text/css application/javascript application/json image/svg+xml application/xml+rss;

· brotli on; 启用 Brotli 压缩。
· brotli_static on; 启用对静态文件的 Brotli 压缩。
· brotli_types ...; 指定应该进行 Brotli 压缩的 MIME 类型。

怎么知道自己开没开启成功呢？
找一个你已经配置完成的服务，去访问它，比如我的博客网站，就是部署到这个nginx上的。
![[Pasted image 20231113220901.webp]]

可以看到已经开启了。

### 关于监听的端口

#### 关于域名
我前几天搞了一个外国注册商的域名，无法在我国备案，但是这是之后的事情了，我是先使用了这个域名才想起来需要备案的，因为当我访问 80 和 443 的时候，腾讯云把我 ban 了，网上查了一下，除了80，443这俩端口，其他端口不备案也都是可以用的，不过被网警查到，就需要封一天。


监听的端口和 server_name 的组合必须是唯一的。
为了验证我的说法，做一个实验（两台虚拟主机，不同的server_name）。
在我测试的时候，我突然发现，监听的端口是一样的，那么怎么确认是哪一台虚拟主机呢,网上告诉我使用 host (http 1.1) 字段来区别，看来一圈，人傻了，根本没有这个字段，http 2.0 不用这个了已经。

在网上看到了另一个监听相同端口的方法，做一下反代。
宝塔上的那个php项目不过是占用了我的另一个域名以及端口罢了。

```nginx
location /word {
      proxy_pass http://localhost:8080/;
}
```
这还是没达到我们的目的，listen + server_name 必须唯一，就可以监听相同端口了。



>[!bug] 注意
> 上面的<span style="color:skyblue">端口管理</span>部分 提到了后面加不加 / 的区别，可以尝试一下不加 / 能不能显示出测单词网站
> 这个网站占据了 8080 端口。显然是不可以的。
> ![[Pasted image 20231111110539.webp]]



#### 泛解析
在腾讯云解析域名

/* .debudzg.top都打到我的服务器上。

之所以显示不安全，可以点开看看，SSL证书与debudzg.top相关，其他域名用是无效的。
![[Pasted image 20231111112052.webp]]


起码到目前为止，我还没有通过操作对server_name的设置有认识。
暂时的看法时，域名（debudzg.top）跟你的 server_name 没有任何关系，它应该指的是虚拟主机的标识？11.10


### 负载均衡

多台服务器时才这样做
```nginx
upstream serverName {
    test01.com weight=1 ;
    test02.com weight=2 backup;
    test03.com weight=3 down;
}
server {
    location / {
        proxy_pass http://serverName;
    }
}
```
serverName处可以随便起，但是呢，两处serverName需要相同

weight = ‘’代表权重，权重越高，请求就优先被转发到该服务器。


#### 后缀含义

down 停用该虚拟机 ，这个命令比较鸡肋，挂了就挂了呗，有去加标志的时间，找一下bug，或者启用一台新的机器会更好

backup 备用机，当其他服务器宕机的时候，这个服务器才启用，其实也比较鸡肋，其他服务器都宕机了，启用这个也不一定好使。这几台服务器提供的服务肯定都是相同的，因为出bug宕机 没用，流量大宕机，也基本没用，你把好的服务器当备用机？

上面的例子中，test02 服务器是备用机，test03 停用，只有test01能工作，test01 挂了之后，test02才会工作。
#### 轮询

#插曲 发现有好多地方都有轮询这个词

nginx 默认情况下使用轮询方式，逐一转发，适用于无状态请求。
当下使用最多的还是无状态的会话控制，也就是服务端在登录时下发[[Vue的使用#token|token]]，请求时携带token，服务端只做校验（鉴权）。

当然也可以去做有状态的，不过采用轮询的话，就需要在各个服务器之间共享session。




### 静态文件托管


设置了对 jpg、jpeg、gif、png、css、js、ico 和 xml 这些类型的静态文件进行缓存，并且设置了缓存的过期时间为 30 天

```nginx
location ~* \.(jpg|jpeg|gif|png|css|js|ico|xml)$ {
    access_log        off;
    log_not_found     off;
    expires           30d;
}
```

## 高级命令

## nginx 部署项目时的问题

前端发起请求的接口是带/api 的，但是这个/api是我们设置的用于防止CROS报错的
但是后端却将它识别为了路径的一部分，所以就返回了404.

我们的副驾驶还是有点作用的，原来我只需要在proxy_pass http:localhost:8080 后边再加一个/
就可以将/api 去掉了。所以，当一时间做不出来一个东西的时候不如放一放。

### 将 http 变为 https

新申请了个域名，所以将之前做的日记小玩具挂载到了新的域名下，新域名是在外国的平台上申请的，90多嘞这个域名，不过学生零元购，还是很划算的，有一说一，学生身份真的得好好的用。

手动去部署一下，至少可以知道没有可视化平台之后怎么操作，还是很不错的。

#### 遇到的问题

端口占用，这个也是一个小问题，毕竟宝塔那边的php项目，80 443都给占用了。

将免费SSL证书的文件名写错，导致找不到，这个是属于小问题，检查一下就可以知道。

不能启用SSL证书，原因是SSL模块没有在配置中，一个比较好的做法是
找到我们解压过后的那个nginx目录( <span style="color:gold">不是我们nginx的安装目录 </span>)，执行

```shell
$ ./configure --with-http_ssl_module
$ make
```

之后将其中的nginx目录下sbin文件夹的nginx文件替换掉我们 本来nginx文件
说的可能有点绕口，替换掉之后，执行这个nginx文件之后会出现找不到配置文件的错误
这个时候只需要执行

```shell
$ ./nginx -c /usr/local/nginx/conf/nginx.conf
```

帮助它找到我们的配置文件的位置，只需要执行一次。

如果 nginx 报错说端口已经被占用，
如果是因为上次启动的nginx占用了端口，那么执行如下命令，如果是因为其他进程占用，那就考虑更换端口，或杀死占用端口的进程吧

```shell
$ ./nginx -s reload

%% 杀死进程 在 linux中 %%

$ lsof -i:port
$ kill -9 PID

```
##### 在 windows 中杀死进程
现在后台启动一个springboot的项目 占用端口 8000
查询一下这个端口对应的进程PID
```shell
$ netstat -ano |findstr 8000
```

然后执行
```shell
$ taskkill /f /pid PID
```

在上面展示的命令中，所有字母的大小写均与结果无关。我说的是在Windows中
因为windows的文件系统（FAT32 或者 NTFS）它们对于大小写不敏感，所以运行在这些环境中的命令<span style="color:gold">一般</span>也一样。

但是这不代表着linux/unix也是如此，它们的文件系统（ext4 或 XFS）是大小写敏感的

我如果不使用 /f 参数就无法中止我的springboot项目，因为taskkill会发送一个中止信号量给进程，但是它可以选择<span style="color:gold">忽略</span> 加入我们的 /f 参数之后它就不能忽略中止信号了。

我们当然可以拿着我们的进程pid去到我们的任务管理器去搜索关闭它。

##### 进程名称需要大小写

如果你只知道进程的名称，其他的什么都不知道，上面的例子中是已经知道端口号了。
比如我们要关掉我们的笔记软件，它的名字叫 Obsidian
那我们可以使用

```shell
$ tasklist | findstr Obsidian
```

来查询它的一些详细信息，包括它的PID 你查Ob也是可以的，它会输出所有包含Ob的进程信息
但是你搜索ob搜不到。

findstr 用于在文件或者命令输出中搜索“patten” ，将结果打印在命令行之中。
```shell
$ findstr "patten" filename
```

<span style="color:gold">AI说</span> 
![[Pasted image 20231109101102.webp]]

然而
![[Pasted image 20231109101115.webp]]

流程
![[Pasted image 20231109101143.webp]]

最后
![[Pasted image 20231109101416.webp]]

它是懂见风使舵的，所以它的话可信度也是不高的。
用来重新加载，比去杀死进程好多了。



#### 有关 nginx 重载

当我们使用nginx 的重载命令时，本质也是发送一个信号量，当主进程接收到之后，它会首先去读取解析新的配置文件，假如没有错误，就启动新的工作进程，逐渐关闭旧工作进程，旧工作进程还会继续以旧配置文件处理已经接收到的请求。

如果有错误，主进程会拒绝加载。

nginx分为 主进程 与 工作进程

主进程不参与到http请求的处理之中，它负责管理和创建工作进程，以及读取检查配置文件
当然它也会接收来自操作系统或用户的信号，然后执行相应的操作。

### 如何只在网址中输入域名就访问到其他端口的服务？
使用转发！
如下写法仅供参考，记得每行之后加 ；
```nginx
server {
    listen 80;
    server_name localhost;
    location / {
        proxy_pass http:// .....;
    }
}

```

### 加快我们网站的访问速度

在爬虫课上吃了一次压缩文件在网络上传输的亏，知道压缩数据可以加载我们网页的响应速度，所以我们这次也正好可以采用这种方式
就采用 gzip 压缩的方式吧，这个还不知道每一行的具体含义，等弄清楚之后再写。[[PROJECT/SCHEME/nginx#GZip Br|两种压缩方式的配置与解释]]





