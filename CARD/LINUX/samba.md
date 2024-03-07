---
file-created: 2023 11 04
last-modified: 2023 11 29
---

所以，为了实现windows和unix系列系统之间能够相互沟通，就产生了samba服务。

Samba服务：是提供基于Linux和Windows的共享文件服务，服务端和客户端都可以是Linux或Windows操作系统。可以基于特定的用户访问，功能比NFS更强大。

[Fetching Title#9tnf](https://www.ywbj.cc/?p=1064)

```bash
sudo apt-get install samba samba-common -y
```
修改配置文件.  `/etc/samba/smb.conf `

```conf
[Ubuntu]                                   # 自定义共享名
comment=this is Linux share directory     # 描述符，是给系统管理员看的
path=/                                    # 共享的路径
public=yes                                # 是否公开，也就是是否能在网上邻居看到该共享
writable=yes                              # 是否可写
```
启动samba
```bash
sudo systemctl restart smbd.service
```




