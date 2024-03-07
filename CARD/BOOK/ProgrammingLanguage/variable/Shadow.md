
>[!faq] variable scope problem
>Sometimes, we may create "same" variable (refer same variable name), compiler/interpreter must choose one variable to modify. 
>In C , the scope of a variable is the end of current code block which is create by symbol `{}`. 
>Most language choose the "shadow rule" -- use the inner variable and blocking the outer variable. 
>Here are example in C. 

>[!example] 
>```c
>int main() {
>   int a = 10;
>   {
>     int a = 20;
>     printf("a = %d\n", a);
>   }
>   printf("a = %d\n", a);
> }
>```

>[!exp]- Python Version
> ```python
> def outer():
>   def inner():
>     x = 20
>     print(x)
>     
>   x = 10
>   inner()
>   print(x)
> 
> outer()
> ```
 

>[!tip] Personal View 
>It is an act of desperation , which you should avoid declaring two variable with same name. 
>So forget "shadowing rule" and write more code . 


