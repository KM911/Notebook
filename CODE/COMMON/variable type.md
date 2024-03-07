
>[!note] previous reading 
>[[pass value vs pass reference]] [[reference vs pointer]]

>[!note] 我们不是在讨论 `int` `string` 这样的变量类型,而是在讨论其作为参数时,是传递了值还是传递了引用的变量类型. 

>[!note] Basic Type and Reference Type

>[!faq] How to identify them.
>one simple way is pass them as a function argument and look wheather it could change the variable value. 
>

>[!example] 
>```c
>void ChangeInt(int a){
  a =10;
}
> 
> void ChangeArray(int a[]){
>   a[0] = 10;
> }
> int main(){
>   int a =1;
>   ChangeInt(a);
>   printf("a = %d\n",a);
>   int array[10] = {1,2,3,4,5,6,7,8,9,10};
>   ChangeArray(array);
>   printf("a[0] = %d",array[0]);
> }
>```

>[!note] `int` is `basic type` , `array` is `reference type`



