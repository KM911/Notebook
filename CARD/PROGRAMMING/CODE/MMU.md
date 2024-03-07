设想一下,如果每一次从硬盘中读取数据都需要CPU的参与.这样CPU就必须花费很长的时间等待,不然就无法进行其他工作. 

硬件工程师非常的聪明,既然IO需要花费大量的时间,那么我们为什么不去设计一个专门的处理单元来进行IO呢? 只需要IO完成后,通知CPU,让CPU继续下面的运算就好了 .


```c
#include<stdio.h>
#include<unistd.h>

int a = 2;
int main(){
  printf("a value is %d  \n", a);
  printf("a address is %p \n", &a);
  sleep(10000);
}
```

将上面a的值修改为不同的值,比如1和2,分别编译,运行可以得到类似下面的结果. 
`````col
````col-md
flexGrow=1
===
```bash
a value is 1  
a address is 0x558b00c99010
```
````
````col-md
flexGrow=1
===
```bash
a value is 2  
a address is 0x5556cbc99010
```
````
`````

>[!note] 我们发现两个进程a的地址值是一样的,并且它们有不同的值. 

如果这里的地址是真实物理地址,是不是因为后来加载的程序修改了a的值? 
我们修改一下程序,每隔一段时间输出a的值和地址

```c
int a = 1;
int main() {
  while (1) {
    printf("a value is %d  \n", a);
    printf("a address is %p \n", &a);
    sleep(5);
  }
}
```

>[!info] 结果是两者的地址虽然是一样的,但是值是不一样的.

思考 这里的地址有没有可能是"虚假"的? 是这个进程内部的地址空间,这样就实现了进程间的隔离.? 

`````col
````col-md
flexGrow=1
===
```bash
a value is 1  
a address is 0x55bf2d697010
a value is 1  
a address is 0x55bf2d697010
a value is 1  
a address is 0x55bf2d697010
a value is 1  
a address is 0x55bf2d697010
```
````
````col-md
flexGrow=1
===
```bash
a value is 2  
a address is 0x5616df61b010
a value is 2  
a address is 0x5616df61b010
a value is 2  
a address is 0x5616df61b010
a value is 2  
a address is 0x5616df61b010
```
````

`````



## MMU的介绍 

虚拟地址到物理地址之间的转换. 

任何的虚拟地址,最后肯定还是对应一个真实的物理地址. 

TODO 虚拟地址到物理地址之间的转换. 
