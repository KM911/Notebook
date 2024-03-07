
有意义吗? 其实是非常有意义的不是吗? 这样可以简化我们上传文件的管理,这不比使用ftp的客户端要好吗 ? 集成化程度高就意味着可定制化的功能少,不是吗? 

```bash
sudo apt install nfs-kernel-server

```

修改配置文件.

这里对于没有server有一点点问题.

```bash
sudo /etc/init.d/nfs-kernel-server restart
```


### 
```
 sudo apt-get install nfs-kernel-server

```