
>[!faq] 如何交换两个变量的值

>[!note] 看到这个问题,你未免不会想吐槽, 这么简单的小问题是个人都会 


>[!warning] 细节就在其中. 


>[!exp] 临时变量
>```c
>int main (){
>     int a  =5;
>     int b = 10;
>     printf ( "a = %d b = %d\n" , a , b );   
>     int temp =a;
>     a = b;
>     b = temp; 
>     printf ( "a = %d b = %d" , a , b );   
> }
>```

>[!faq] 有的人就想是否可以减少这一点点内存开销 


>[!example]  加法计算
>```c
>int main (){
>    int a  =5;
>    int b = 10;
>   printf ( "a = %d b = %d\n" , a , b );   
>    a = a + b;
>    b = a - b ;
>    a = a - b ;
>    printf ( "a = %d b = %d" , a , b );   
>}
>```

>[!tip] 不必担心溢出,原理类似于溢出不会改变两个数的绝对大小. 

>[!example] 还有的人使用了 bitwise 位运算中的 异或 XOR
>```c
>int main() {
  int a = 5;
  int b = 10;
  printf("a = %d b = %d\n", a, b);
  a = a ^ b;
  b = a ^ b;
  a = a ^ b;
  printf("a = %d b = %d", a, b);
}
>```


>[!faq] 看上去一切良好是不是? 

>[!warning] 我们不关需要校验其是否生效,还要检验其是否会失效啊!
>

>[!test] 如果两个变量的地址是一样的
>最为常见的情况就是交换数组中的元素. 
>两个相同的值进行异或运算结果为0,又因为地址一样,导致将原始值给覆盖了. 
>```c
>int main() {
  int a = 0xff;
  int *p1  = &a;
  int *p2 = &a;
  printf("%d\n", *p1);
  *p1 = *p1 ^ *p2;
  *p2 = *p1 ^ *p2;
  *p1 = *p1 ^ *p2;
  printf("%d\n", *p1);
}
>```

>[!tip] 谨慎使用,"奇淫巧计". 
>


