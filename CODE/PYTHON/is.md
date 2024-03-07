
>[!tip] The is keyword is used to test if two variables refer to the same object.
>
> The test returns True if the two objects are the same object.
> 
> The test returns False if they are not the same object, even if the two objects are 100% equal.
> 
> Use the == operator to test if two variables are equal.


>[!exp] x and y are value equal but not point equal. 
>if use `==` to check them wheather `equal` , it will return true , because they are "value equal" 
> ```python
> x = ["apple", "banana", "cherry"]
> 
> y = ["apple", "banana", "cherry"]
> 
> print(x is y)
> print(x==y)
> ```


>[!transfer] js == and === 

