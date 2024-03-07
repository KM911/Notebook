---
file-created: 2023 11 26
last-modified: 2023 11 26
---

>[!faq] What specific actions are executed when the commands `ls -l` and `gcc main.c` are entered into a terminal?

>[!example] 
> ```c
>  #include<stdio.h>
> int main(int argc, char *argv[])
> {
>   for (int i = 0; i < argc; i++)
>   {
>     printf("argv[%d] = %s\n", i, argv[i]);
>   }
> }
> ```

```bash
./a.out -o main main.c
argv[0] = ./a.out
argv[1] = -o
argv[2] = main
argv[3] = main.c
```

>[!tip] full name  
>argc   ==    argument count
>argv   ==    argument value 


>[!note] I could tell you, all command-line interfaces and REPLs utilize the argv array and conditional statements, which enables them to interpret user commands.

