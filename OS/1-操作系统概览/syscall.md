---
file-created: Sunday, October ,2023
last-modified: Saturday, November ,2023
---
我之前理解的syscall有偏差. 

错误 : syscall会让出CPU的执行权限,交給操作系统. 
正确 : syscall 其实和函数调用没有实质的区别, 只是一个是你的函数,另一个是操作系统的函数. 

syscall 只需要像普通的函数调用一样, 然后修改rip基础的值,也就是进行内核指令区, 然后执行对应的指令就好了,然后就跳转回来,这样的性能开销其实也没有什么哎,因为这个是共享的函数. 

##  xv6的trapframe

跳板 笑死我了非常形象的说法, 它的syscall叫做 ecall,核心内容就是跳转到操作系统内核的指令区. 

