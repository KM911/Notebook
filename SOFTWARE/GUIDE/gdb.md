
我们还是需要知道一些gdb的命令,这样来帮助我们调试.特别是可以看到更多的其他的信息. 

## 查看全部的寄存器信息

i386:x86-64

一共有24个寄存器信息, 
其中rip寄存器的感觉就是pc一样地存储,告诉你运行到了哪里. 

16 General Purpose Registers rax -t15 
2 Status Registers  rip eflags 
6 Code Segment Registers  cs ss ds es fs gs

## 没看见了 

16 SSE Registers
8 FPU/MMX Registers

```c
rax            0x1                 1
rbx            0x0                 0
rcx            0x1                 1
rdx            0xb814a0            12063904
rsi            0x0                 0
rdi            0x0                 0
rbp            0x5ffee0            0x5ffee0
rsp            0x5ffe70            0x5ffe70
r8             0xb820a0            12066976
r9             0x7ff86ee94f40      140704989400896
r10            0xb80000            12058624
r11            0x5ffc58            6290520
r12            0x0                 0
r13            0x0                 0
r14            0x0                 0
r15            0x0                 0
rip            0x7ff7aa681340      0x7ff7aa681340 <__tmainCRTStartup+492>
eflags         0x202               [ IF ]
cs             0x33                51
ss             0x2b                43
ds             0x2b                43
es             0x2b                43
fs             0x53                83
gs             0x2b                43

```

```c
rax            0x1                 1
rbx            0x0                 0
rcx            0x1                 1
rdx            0xb814a0            12063904
rsi            0x0                 0
rdi            0x0                 0
rbp            0x5ffe60            0x5ffe60
rsp            0x5ffe30            0x5ffe30
r8             0xb820a0            12066976
r9             0x7ff86ee94f40      140704989400896
r10            0xb80000            12058624
r11            0x5ffc58            6290520
r12            0x0                 0
r13            0x0                 0
r14            0x0                 0
r15            0x0                 0
rip            0x7ff7aa681648      0x7ff7aa681648 <main+20>
eflags         0x202               [ IF ]
cs             0x33                51
ss             0x2b                43
ds             0x2b                43
es             0x2b                43
fs             0x53                83
gs             0x2b                43
```


