
## malloc 

>[!note] memory allocate 
> IT is used to dynamically allocate memory. This means that the memory is not allocated when the program is compiled, but rather at runtime when the program is being executed.
>```c
>// syntax , need include stdlib
>void * void_pointer = (void*) malloc(size_t size);
>```

>[!tip] 1. Dynamic 
>2. Heap
>3. Contiguous


## Dynamic 

>[!faq] if you do not know the size of a variable, how could you allocate memory for it ? 

>[!note] Dynamic memory allocation refers to the allocation of memory during the execution of a program, while static memory allocation occurs during the compilation stage, before the program is run.



## Stack Vs Head 

>[!note] Stack 
>The operating system typically allocates a memory block for each program. This block is called a stack, and it is used to store local variables, function arguments, and return addresses. The stack operates using push and pop operations, which allow for efficient data storage and retrieval. These operations must be precise, as each push operation adds a fixed amount of memory to the stack, typically 4 bytes for an integer value. This ensures that data is stored and accessed correctly within the stack's memory structure



>[!note] Heap
>In contrast to the stack, which is a structured memory region managed by the operating system, the heap is an unorganized pool of memory that programs can dynamically allocate and deallocate as needed. Dynamic memory allocation involves requesting memory from the heap using functions like malloc() and explicitly releasing it using free() to prevent memory leaks. The heap is not subject to the same strict memory management rules as the stack, allowing for more flexible memory usage. However, this flexibility comes with the responsibility of properly managing memory allocations and deallocations to avoid memory leaks.




>[!note] In C, a variable declared within a block, such as int a, will have its memory automatically recycled when the block exits. This memory is allocated on the stack. If you want to prevent this automatic memory recycling and retain the variable's value beyond the block's scope, you need to allocate the variable on the heap using dynamic memory allocation functions like malloc().

>[!warning] Not every local variable will be allocated at stack. 
>For example , the variable is very big and bigger than program stack, it could only be allocated on heap. 

## Contiguous

>[!note] Each memory block allocated through the malloc() function occupies a contiguous region of memory. This means that the memory block's starting address is followed by a sequence of consecutive addresses, ensuring that the allocated memory is a single, uninterrupted segment.


## free

>[!note] Compared to malloc(), which allocates memory, the free() function is simpler to use and comprehend. 
>It serves the purpose of reclaiming the memory that was previously allocated by malloc(). By utilizing free(), you can effectively return the memory to the heap for reuse, preventing memory leaks and ensuring efficient memory management.

>[!example]
>```c
>```


## calloc 

>[!example] Clear allocte
>allocate and initialize it will zero. 
>```c
>   void * void_pointer2 = calloc(12, 1);
    printf("%d\n", *(int*)void_pointer2); 
>```


## realloc

>[!note] change the size of block and won't loss data . 




