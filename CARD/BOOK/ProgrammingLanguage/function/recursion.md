
>[!tip] Recursion 
> A programming technique where a function calls itself directly or indirectly to solve a problem.

>[!faq] Infinite Loop ? 
>The function includes a conditional exit, ensuring finite loop execution




$$
F_n = \begin{cases}
0 & \text{if } n = 1 \\
1 & \text{if } n = 1 \\
F_{n-1} + F_{n-2} & \text{if } n > 1
\end{cases}
$$
 
>[!example] Fibonacci sequence
>```python
>def fib(n):
  if n == 1 or n == 2 : return 1
  else : return fib(n-1) + fib(n-2)
>print(fib(5))
>```

还有什么经典问题,树的先序遍历后续遍历以及中序遍历. 




>[!faq] Exits Problem
>1. stack limit. recursion will create a lot function call stack , if the recursion depth is out of range, will cause stack overflow.
>2. performance bad. "function call stack" will use a lot resource ,so recursion function is usually performance lower than common loop function.  
>3. hard to understand. For some problem, use recursion will promote the understanding effort. 

>[!v] a recursion function must could be rewrite into a loop function ? 

如何从数学上去证明? 
目前没有看见非常好的证明,



