
## 致命错误：stdatomic.h：没有那个文件或目录

>[!tip] 原因 
>gcc 版本问题 gcc4.8 

>[!done] 解决方式 
>将gcc升级即可
```bash
sudo yum install centos-release-scl
sudo yum install devtoolset-9-gcc*
scl enable devtoolset-9 bash
```




