---
file-created: 2023 11 23
last-modified: 2023 11 29
---


| Concept        | Description                                 |
| -------------- | ------------------------------------------- |
| Dynamic typing | Type checking is performed at runtime.      |
| Static typing  | Type checking is performed at compile time. |
| Strong typing  | Implicit type conversions are not allowed.  |
| Weak typing    | Implicit type conversions are allowed.      |

* [[CODE/PYTHON/python]] : Dynamic and Strong
* [[CODE/C/C]] : Static and Strong
* [[CODE/GO/go|go]] : Static and Strong 
* [[java]] : Static and Strong 
* [[JS]] : Dynamic and Weak

 
 > [!note] Dynamic and Static 
>static typing require programmer declare variable type , while dynamic typing do not need to 
>Or explicit type is static type 

## python 

```python
a = 10 
b = "hello"
c = a + b 
```

>[!error]  TypeError: unsupported operand type(s) for +: 'int' and 'str'

可以把这个作为单独的一个部分不是吗 ? 


## js


```js
let a = 10
let b = "hello"
let c = a + b
console.log(c) # will echo 10hello 
```

 >[!question] var let const usage 
 
 