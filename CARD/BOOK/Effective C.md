---
file-created: 2023 11 15
last-modified: 2023 11 30
---

## 一句话评价

刚开始看到这本书,以为内容是大量的由于动态内存,多线程,锁相关的内容,结果在读到"本书的目标读者"时,发现是入门书,对的就是入门书.加上这本书内容本身就非常少,所以像控制流这样的章节只能泛泛而谈.不过还是有部分内容带给我一些新的内容.

推荐程度: 
==新人== 🌟🌟🌟🌟
==老人== 🌟


## 从Hello world开始

`````col
````col-md
flexGrow=
===
你会发现这个"hello world"有一点点不一样

```c
#include <stdio.h>
#include <stdlib.h>
int main(void) {
  puts("Hello, world!");
  return EXIT_SUCCESS;
}
```
````
````col-md
flexGrow=1
===

正常的"hello world"

```c
#include <stdio.h>
int main(){
  printf("Hello World!\n");
  return 0;
}
```

````

`````

个人更加喜欢本书中给出的版本,尽管复杂了一点点,但是很早就指出了其他内容.比如main函数可以接受其他参数,为什么是return 0,格式化输出存在安全漏洞.

尽管只是提了一句的内容,但是我觉得还是不错的,毕竟我已经学习完了学校的课程,我还是不知道上面这些.

## 错误处理

C语言中没有"error"类型,一般是以int类型的函数返回负数或者指针类型NULL作为错误.如果文件不存在或者其他原因引发错误的话,你将会看到 `Process finished with exit code 1`的提示信息.
```c
#include <stdio.h>
#include <stdlib.h>
int main(){
  FILE *file = fopen("test.txt", "r");
  if (file == NULL){
    return EXIT_FAILURE;
  }else{
      // Do something with the file
    return EXIT_SUCCESS;
  }
}
```

这里又涉及了一个问题,C语言中如果实现一个函数即可以存在错误处理又可以返回值?
1. 利用union类型 也就是返回的类型要么是错误信息,要么是正确的值. 不过这样有点点麻烦,每当你想要返回一个其他类型时,你就需要去重写一共union.
2. 函数还是返回一个值比如int,将原本是利用赋值修改变量改为传递指针修改其值.

个人认为还是第二种方式比较好,就是传值的时候麻烦了一点点
`````col
````col-md
flexGrow=
===
```c
#include <stdio.h>
#include <stdlib.h>

union Float_Error{
    float f;
    int error;
};

typedef union Float_Error Float_Error;

union Float_Error divide(int a, int b){
    if (b == 0){
        Float_Error msg;
        msg.error = 1;
        return msg;
    }
    else{
        Float_Error msg;
        msg.f = (float)a / b;
        return msg;
    }
}
int main(){
    int a ,b;
	scanf("%d%d",&a,&b);
    Float_Error msg = divide(a, b);
    if (msg.error == 1){
        printf("Error\n");
        return EXIT_FAILURE;
    }
    else{
        printf("%f\n", msg.f);
    }
    return EXIT_SUCCESS;
}
```
````
````col-md
flexGrow=1
===
```c
#include <stdio.h>
#include <stdlib.h>

int divide(int a,int b, int*ans){
	if (b==0){
		return -1;
	}else{
		*ans = a/b;
		return 0;
	}
}

int main(){
	int a ,b;
	scanf("%d%d",&a,&b);
	int *ans = (int*)malloc(sizeof(int));
	int error = divide(a,b,ans);
	if (error == -1) {
		printf("Error\n");
		return EXIT_FAILURE;
	}else{
		printf("a / b = %d\n",*ans);
		return EXIT_SUCCESS;
	}
}
```

````

`````

其实我们从库函数中可以窥见一些内容.比如malloc,


## main函数是程序的入口吗?

尝试运行下面的代码,你可以收获不一样的效果.gcc可以指定其他函数作为程序的入口.实现的方式有很多,比如C++全局变量的构造函数等等.
```c
#include<stdio.h>
__attribute((constructor)) void before_main()
{
	printf("Hello, world");
}

int main() {
	return 0;
}
```

利用这个可以做什么,当然是我们的benchmark了啦.
## benchmark

通常情况下,我们会采用下面的方式来判断某个函数的性能.


## 其他

本书涉及了大量诸如字符编码字符串集等底层问题,本人对于这部分不是非常感兴趣,就不了解了.
