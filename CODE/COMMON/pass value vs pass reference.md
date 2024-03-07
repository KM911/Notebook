---
file-created: 2023 12 07
last-modified: 2023 12 08
---


>[!example] Swap two variable value
>```c
void Swap(int a, int b){
  a = a^b;
  b =a ^ b;
  a = a^ b; 
}
>
int main (){
  int a =10 , b=5;
  printf("a=%d b=%d\n",a,b);
  Swap(a,b);
  printf("a=%d b=%d\n",a,b);
>
}  
>```

>[!fail] Your attempt to swap values failed 
>Because you are only copying the values into the function and not the actual variables themselves. 

>[!example] copy value proof
>We will print the memory address of each variable in the current function block.
>```c
>void Swap(int a , int b){
  printf("&a = %p , &b = %p\n" , &a , &b);
  a = a ^ b;
  b = a ^ b;
  a = a ^ b;
}
int main() {
  int a = 10 , b = 20;
  printf("&a = %p , &b = %p\n" , &a , &b);
  Swap(a , b);
  printf("a = %d , b = %d\n" , a , b);
}
>```
>You will find that the two variables have different memory addresses, which means they are distinct objects in memory. Modifying the value of one variable will not affect the value of the other variable.

>[!note]- Detail About Function Pass Value
>When you pass a value as an argument to a function, a copy of that value is created within the function's memory space. Inside the function, any modifications affect only this copy, not the original variable outside the function. This explains why the original values remain unchanged after the function call, even if the function appears to manipulate them.

>[!tip] To modify the value of a variable within a function, pass its address as a pointer. If you simply need to use the value without modifying it, passing the value itself will suffice, and the function will automatically create a copy.


>[!faq]- Isn't copying the object always necessary?
> If we need to pass a large object as an argument, is copying it through pass-by-value a good option?


>[!example] Swap two variable value , pass-by-reference
>```c
> void Swap(int *a, int *b) {
>   *a = *a ^ *b;
>   *b = *a ^ *b;
>   *a = *a ^ *b;
> }
> 
> int main() {
>   int a = 10, b = 5;
>   printf("a=%d b=%d\n", a, b);
>   Swap(&a, &b);
>   printf("a=%d b=%d\n", a, b);
> }
>```

>[!done] Congratulations! 🥂 
>Now, you could exchange values by pass their pointer. 

>[!tip] Conclude 
>


>[!example] Change Array Value
>You have draw a conclude before , now you write a function and do not want to change the value of an array , so you pass value instead of reference. Howeve ... 
>```c
>void ModifyArray(int a[5]){
  a[0] = 100;
}
> 
> int main() {
>   int array[5] = {1,2,3,4,5};
>   printf("a[0]=%d\n",array[0]);
>   ModifyArray(array);
>   printf("a[0]=%d\n",array[0]);
> 
> }
>```

>[!warning] value of pointer
>some variable like array , it is a pointer . even if you pass value with them , you still could change them value . 


>[!faq]- What happens when we pass the reference of a reference variable?
>we could change the variable  value by reference and get the reference by the reference of reference. So it is "equal" pass reference. 

>[!example] pass the reference of reference variable
>```c
 >void ChangeReference(int **arr){
>   (*arr)[0] = 10;
> }
> int main() {
>   int arr[100] = {1,2,3,4,5};
>   ChangeArray3(arr);
>   printf("%d\n", arr[0]);
>   return 0;
> }
>```




>[!tip] More Detail [[variable type]] [[reference vs pointer]]