
>[!book] 线程可以理解为一个轻量级进程,是操作系统调度的最小单位.现在我们就借助linux来看看,linux是如果实现进程和线程的.


## 只有"进程"

告诉你一个不幸的消息,如果非要严格定义的话,其实Linux中没有"线程",只有"进程". 不过这样其实也不对,应该说,Linux中只有 `task`,进程和线程都是利用`task`来表示的.

>[!info] 计算机世界没有魔法. 操作系统可以管理进程,也就是操作系统必须要"认识"进程,换句话说,就是进程在操作系统这个软件中,肯定对应一个变量也好,一个结构体也好,肯定存在一个值和其对应,管理进程,其实就是在修改这个对应的值. 

task_struct + exec  + stack  

可以简单看看我们的task_struct,代码来自 [linux sched.h v0.0.1](https://elixir.bootlin.com/linux/0.01/source/include/linux/sched.h)

```c

struct  task_struct  {
/* these are hardcoded - don't touch */
	long state;	/* -1 unrunnable, 0 runnable, >0 stopped */
	long counter;
	long priority;
	long signal;
	fn_ptr sig_restorer;
	fn_ptr sig_fn[32];
/* various fields */
	int exit_code; 
	unsigned long end_code,end_data,brk,start_stack;
	long pid,father,pgrp,session,leader;
	unsigned short uid,euid,suid;
	unsigned short gid,egid,sgid;
	long alarm;
	long utime,stime,cutime,cstime,start_time;
	unsigned short used_math;
/* file system info */
	int tty;		/* -1 if no tty, so it must be signed */
	unsigned short umask;
	struct m_inode * pwd;
	struct m_inode * root;
	unsigned long close_on_exec;
	struct file * filp[NR_OPEN];
/* ldt for this task 0 - zero 1 - cs 2 - ds&ss */
	struct desc_struct ldt[3];
/* tss for this task */
	struct tss_struct tss;
};
```


这里还解释了为什么我们需要`int main` 因为在linux上,exit_code被定义为`int` 用于返回程序的错误信息.  

相关知识点:[[错误处理]]

这里看出,一个进程由下面task_struct 和 stack 组成. 

```c
union task_union {
	struct task_struct task;
	char stack[PAGE_SIZE];
};
```

这里是加载程序读取的内容,读取代码段 `a_text` ,初始化数据 `a_data` ,未初始化数据`a_bss` . 
```c
struct exec {
  unsigned long a_magic;	/* Use macros N_MAGIC, etc for access */
  unsigned a_text;		/* length of text, in bytes */
  unsigned a_data;		/* length of data, in bytes */
  unsigned a_bss;		/* length of uninitialized data area for file, in bytes */
  unsigned a_syms;		/* length of symbol table data in file, in bytes */
  unsigned a_entry;		/* start address */
  unsigned a_trsize;		/* length of relocation info for text, in bytes */
  unsigned a_drsize;		/* length of relocation info for data, in bytes */
};
```


>[!tip] 我们可以不考虑进程,只讲线程. 
>这是合理并且真实有效的 

