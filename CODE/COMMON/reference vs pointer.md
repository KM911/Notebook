
>[!faq] What are we talking about reference when we said pass-by-reference. 
 
 >[!example] Equal Function
 >```cpp
 >void Change(int& x, int& y) {
>     int temp = x;
>     x = y;
>     y = temp;
> }
> 
> void ChangePointer(int* x, int* y) {
>     int temp = *x;
>     *x = *y;
>     *y = temp;
> }
> int main() {
>     int a = 10, b = 20;
>     Change(a, b);
>     ChangePointer(&a, &b);
>     cout << "a = " << a << ", b = " << b << endl;
>     return 0;
> }
>```

>[!tip] 
> C has pointers, but it does not have a built-in "reference" type like some other languages. While pointers can be used to achieve similar functionality by providing access to variable memory addresses, they lack the automatic dereferencing and null-safety features that true references offer.

>[!faq] How to proof the two function are equal?
>If you look at their asm, you'll see they're exactly the same.
> `````col
> ````col-md
> flexGrow=1
> ===
> ```diff
> Change(int&, int&):
>         push    rbp
>         mov     rbp, rsp
>         mov     QWORD PTR [rbp-24], rdi
>         mov     QWORD PTR [rbp-32], rsi
>         mov     rax, QWORD PTR [rbp-24]
>         mov     eax, DWORD PTR [rax]
>         mov     DWORD PTR [rbp-4], eax
>         mov     rax, QWORD PTR [rbp-32]
>         mov     edx, DWORD PTR [rax]
>         mov     rax, QWORD PTR [rbp-24]
>         mov     DWORD PTR [rax], edx
>         mov     rax, QWORD PTR [rbp-32]
>         mov     edx, DWORD PTR [rbp-4]
>         mov     DWORD PTR [rax], edx
>         nop
>         pop     rbp
>         ret
> ```
> ````
> ````col-md
> flexGrow=1
> ===
> ```diff
> ChangePointer(int*, int*):
>         push    rbp
>         mov     rbp, rsp
>         mov     QWORD PTR [rbp-24], rdi
>         mov     QWORD PTR [rbp-32], rsi
>         mov     rax, QWORD PTR [rbp-24]
>         mov     eax, DWORD PTR [rax]
>         mov     DWORD PTR [rbp-4], eax
>         mov     rax, QWORD PTR [rbp-32]
>         mov     edx, DWORD PTR [rax]
>         mov     rax, QWORD PTR [rbp-24]
>         mov     DWORD PTR [rax], edx
>         mov     rax, QWORD PTR [rbp-32]
>         mov     edx, DWORD PTR [rbp-4]
>         mov     DWORD PTR [rax], edx
>         nop
>         pop     rbp
>         ret
> ```
> ````
> `````

>[!done] interchangeably in casual conversation
> While the terms "reference" and "pointer" might be used interchangeably in casual conversation, particularly outside the context of C++, they represent distinct concepts with different technical roles. In simpler terms, a "reference" can be thought of as a helpful tool for humans to understand how to access data indirectly, while a "pointer" represents the actual code instructions used by the machine to perform this operation. While both serve the same purpose of providing indirect access, they are different entities with distinct functionalities.
> 


>[!tip] 
>Cpp : [[reference]]
>[[pass value vs pass reference]] [[variable type]]
>

