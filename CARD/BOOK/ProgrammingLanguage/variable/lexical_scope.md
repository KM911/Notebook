

>[!tip] variable scope == lexical scope 
>the area which you could access or modify the variable.


>[!faq] 如何确定一个变量的范围 

>[!warning] 无关 局部 local 全局 global 变量 

>[!tip] 理解 
>一个变量的范围是其申明语句到其对应的 `{}` curly  结束. 所谓的全局变量不过是最大的一层 `{}`

>[!note] 所以我不想看看到你以后讨论相关的内容了.

>[!exp] quiz 
>请问下面的print可以输出a的值吗? 
```c
int main(){
    {
    int a = 10;
    }
    printf("a = %d",a);
}
```

```c
int a = 10;
int main() {
  { printf("a = %d", a); }
}
```


>[!transfer] 
>[Shadow](CARD/BOOK/ProgrammingLanguage/variable/Shadow.md) 
>[closure](closure.md)

