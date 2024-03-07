---
file-created: 2024 01 07
last-modified: 2024 01 07
---


>[!exp] 
>讲一个需要多参数的函数,变成一个pipe line, 每次给一个参数,至少我看不出来好处吧. 

>[!exp] JavaScript
> ```js
> // Regular function with two arguments:
> function Add(x,y){
> return x + y;
> }
> // Curried add function
> function add(x) {
>   return function(y) {
>     return x + y;
>   };
> }
> 
> const add5 = add(5); // Partially applied function
> console.log(add5(3)); // Output: 8
> 
> ```

