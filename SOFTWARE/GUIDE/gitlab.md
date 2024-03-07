
## 安装

没有什么教程是比[官方文档](https://about.gitlab.com/install/)还要好的了. 根据你的发行版选择对应的教程. 下面以Ubuntu 20为例. 

我们还是使用docker来进行安装,理由. 

```bash
# install dependence
sudo apt-get update 

# add gitlab package repository and install it
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash

sudo apt-get install -y gitlab-ce

```

Unless you provided a custom password during installation, a password will be randomly generated and stored for 24 hours in /etc/gitlab/initial_root_password. Use this password with username root to login.
密码是随机的并且只会保存24h，如果你不尽早去/etc/gitlab/initial_root_password 记住密码然后搭配你的用户名登录gitlab，你就完蛋了



奇怪的卡死 
```
ruby_block[wait for logrotate service socket] action run
```

这里需要你执行启动,我只能说 
```
sudo /opt/gitlab/embedded/bin/runsvdir-start
```

gitlab默认使用80端口,所以会出现部分端口冲突的问题


### 获取root密码

如果没有在安装时设置,就需要查看文件. 
```bash
sudo cat /etc/gitlab/initial_root_password
```
### 创建用户

### CI/CD 的搭建 


##### runner 安装

```bash
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash
```

这里的版本太低会出现问题,最好是15.10以上的版本. 
```bash
sudo apt-get install gitlab-runner=15.11.0
```

#### gitlab runner 安装

