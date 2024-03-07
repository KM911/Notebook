---
file-created: 2023 10 29
last-modified: 2023 11 26
---

不要翻译成数据冒险,哪怕是数据竞争我都觉得好不少. 
>[!note] 因为并发导致共享资源存在安全问题


查看如下算法. 多线程取钱, 如果 `BankMoney` 余额不足,就应该失败. 理论上, `BankMoney`的值肯定是大于零;因为两次取钱的金额总和大于`BankMoney`,所以两次取钱操作肯定有一次会失败.  

```c
int BankMoney = 1000;
void GetMoney(int money){
    if (money > BankMoney){
        printf("No enough money\n");
        return;
    }
    BankMoney -= money;
    printf("GetMoney: %d\n", money);
    printf("BankMoney: %d\n", BankMoney);
}
int main(int argc , char *argv[]){
    pthread_t thread1, thread2;
    int ret1, ret2;
    ret1 = pthread_create(&thread1, NULL, (void *(*)(void *))GetMoney, (void *)600);
    ret2 = pthread_create(&thread2, NULL, (void *(*)(void *))GetMoney, (void *)800);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    printf("BankMoney: %d\n", BankMoney);
}
```

你觉得这里的多程序程序是安全的吗?  你是否有证明方式?  

这不是很简单吗? 代码只要跑一下,看一下结果不就好了. 

```bash
GetMoney: 600
BankMoney: 400
No enough money
BankMoney: 400
```

在单线程确实如此,可是到了多线程,通过运行程序来判断程序的逻辑是否正确,这个结果就未必正确了. 很有可能你运行几十万次才有可能出现一次错误,只要有可能出现错误,这个算法就是不安全的. 

不相信? 下面请看我复现错误. 
### 一种很呆的复现方式

我们可以发现, 关键位置在于判断当前余额是否大于要取钱的数目,如果B线程在A线程完成取款 操作之前,这时的余额还没有发生变化,进行了余额判断,那么它可以执行取款的操作. 就会出现错误.  

我们只要稍加修改. 确保上面的事件一定发生就好了,比如让取款操作完成需要花费更多的时间.

```c
void GetMoney(int money){
    if (money > BankMoney){
        printf("No enough money\n");
        return;
    }
    sleep(1);
    BankMoney -= money;
    printf("GetMoney: %d\n", money);
    printf("BankMoney: %d\n", BankMoney);
}
```

现在就可以稳定触发Bug,取了1400,结果银行余额还剩余400/200. 令人害怕. 存在不同的余额是因为两个线程执行顺序不一样导致的,这里有的时候结果可能会变成 -400 , 但是也是不合理的,因为我们设计就是银行余额始终大于0的. 
`````col
````col-md
flexGrow=1
===
```bash
GetMoney: 600
BankMoney: 400
GetMoney: 800
BankMoney: 400
BankMoney: 400
```
````
````col-md
flexGrow=1
===
```bash
GetMoney: 600
BankMoney: 200
GetMoney: 800
BankMoney: 200
BankMoney: 200
```
````
`````

我们现在已经可以稳定出现错误了,不过我们有没有更好的方法,比如可以稳定复现某一种错误? 其实还是可以利用我们上面的操作,设置巧妙的`sleep`时间,确保线程的执行顺序. 

但是这样太麻烦,肯定存在更好的方式,相信哪些和你一样被各种计算机问题所困扰的人,他们或许就是你,一定会想到一种足够好的方法来解决这种问题的. 

### [[gdb#调试多线程]]

我们为了实现在临界区的控制,应该在进入`GetMoney`这个函数的入口打一个断点. 

这里我想录制一个视频, 说明如何进行多线程的调试了. 

TODO : 录制一个多线程调试的视频
