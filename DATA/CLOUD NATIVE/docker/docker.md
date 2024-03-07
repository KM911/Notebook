
>[!note] Background 



## Do What ? 
1. time machine 
git已经可以做到将代码恢复到某个时刻,但是确无法恢复当时的环境. 可能新版本的python并不兼容当时的代码了,又或者是github的仓库已经不见了... 
docker可以让你乘坐时光机,回到那个时候. 
2. 

## 一些错误的处理方式 

1. 镜像应该是一个最简环境而不是一个完整系统. 
2. 不应该在镜像里进行构建,而是应该将构建的结果打包到镜像里.
3. alpine是目前最小的base image,但是请时刻牢记静态链接. 


何时使用 ubuntu这种,只有当你需要动态链接库时,例如 
```txt
 >ldd a.out
linux-vdso.so.1 (0x00007ffec80f8000)
libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fdaf5fd6000)
libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 
(0x00007fdaf5fbb000)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fdaf5dc9000)
libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fdaf5c7a000)
/lib64/ld-linux-x86-64.so.2 (0x00007fdaf61d0000)
```


## docker 的三要素 

image container 


