
## time

[unix - What do 'real', 'user' and 'sys' mean in the output of time(1)? - Stack Overflow](https://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1)


> [!exp]
> ```shell
> time echo hello
> ```

>[!note] real
>程序运行所花费的真实时间. 

>[!done] user 
>程序在 user mode 模式下运行的所花费的CPU时间

 >[!warning] sys 
 >程序在kernel/privileged mode 运行所花费的时间. 

## example

sleep will increase the real and little user or sys

特别注意 : 多线程程序,其user 和 sys计算的是CPU时间,由于多线程程序可能会使用多个CPU,就会出现 user + sys > real 的情况. 