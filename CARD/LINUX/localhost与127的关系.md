
>[!done] localhost是domain , 127.0.0.1 是 IP, 所以localhost需要进行DNS解析,本机的hosts文件默认将localhost解析为127.0.0.1,同理你可以通过修改hosts文件将其解析到其他的服务器,比如百度的服务器

>[!example] 修改hosts
>我们通过 nslookup查看baidu的ip
>```bash
>nslookup www.baidu.com
>```
> windows : `C:\Windows\System32\drivers\hosts` 
> linux : `/etc/hosts`

>[!note] 127.0.0.1 == 当前电脑

 >[!v] ::1 表示的含义是什么? 
 

