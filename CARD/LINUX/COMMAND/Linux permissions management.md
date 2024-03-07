---
file-created: 2023 12 03
last-modified: 2023 12 05
---

>[!note] 用户管理
>早期计算机系统非常昂贵,通常都是很多人共同使用一台机器,自然就衍生出了多用户的问题. 现在个人计算机非常普及,每个人几乎都有多个电子计算机,用户管理就好像没有那么常见了. 如今的多用户场景更多是公司中需要多人协作的场景下使用. 

>[!example] 查看文件权限  [[file info]] 
>```bash
>touch test.sh
>ls -l test.sh
>```


>[!example] 修改文件权限
>```bash
>chmod 777 test.sh
>ls -l test.sh
>```
>除了使用数字模式外,还可以使用符号模式 



修改权限使用 chmod 

1数字模式 
`chmod 777 file` 自己去想什么意思
r4
w2
x1

2字母模式

`+` 添加 `-` 移除 = 设置 

| a | all |
| ---- | ---- |
| g | group |
| o | other |
| u | user |



>[!warning]- 缺少执行权限不代表不可以执行
>现在有一个 `test.sh` 我们将其的权限设置为`444` 请问,该脚本可以被执行吗? 
>看上去好像是不可以的,因为我们没有执行权限,使用`./test.sh` 确实无法执行,但是,因为其是可读的, 我们利用`bash ./test.sh` 就可以执行了. 我觉得有点好笑, 为了避免这种情况,你应该连读的权限都不提供.




## 更换文件所属和权限

```bash
touch test.sh
sudo chown root test.sh
ls -l test.sh
```




## 用户管理 

| Command | Usage          |
| ------- | -------------- |
| whoami  | 检查当前用户名 |
| adduser | 创建新用户     |
| userdel | 删除用户       |
| su      | 切换用户       |
如果要考就去学习 `adduser`

### 用户组管理 

这里其实就是细分的用户权限不是吗 ? 就是从维护每个当一个人变成了,团队,这样的开销就会小很多. 

| Command  | Usage     |
| -------- | --------- |
| groupadd | 添加组       |
| groupdel | 删除组       |
| groupmod | 将用户添加到某个最 |
| newgrp   | 登陆到其他组    |


## 为什么如此表示

>[!done] 为什么如此表示?
在Linux中，权限777 或者是 `-rwxrwxrwx` 表示文件所有者、同一群组用户、其他用户拥有读（r）、写（w）、执行（x），它们对应的数字分别是4、2、1. 通过或的位运算就可以知道为什么这样表示了.  
```c
int main(){
  int read = 0x4;
  int write = 0x2;
  int execute = 0x1;
  int permission = read | write ;  // 可读可写
  printf("permission = %d\n", permission);
}
```

>[!transfer] 利用宏去实现打开文件时的逻辑策略
>网络请求的协议. 



