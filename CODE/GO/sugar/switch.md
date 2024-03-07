
>[!example] common switch
>```go
>
> func main() {
> 	flag := 10
> 	switch flag {
> 	case 1:
> 		println("hello world")
> 
> 	case 10:
> 		println("hello flag")
> 	default:
> 		println("hello default")
> 	}
> }
>```

>[!tip] use switch to replace mutil if. 


> [!example] switch
> ```go
> import "math"
> func main() {
> 	flag := 10
> 	switch {
> 	case flag == 1:
> 		println("hello world")
> 	case flag%2 == 0:
> 		println("hello flag")
> 	case math.Abs(float64(flag)) == 10:
> 		println("hello abs flag")
> 	default:
> 		println("hello default")
> 	}
> }
> 
>```

>[!warning] Only one case will be match
>the above code equal `if elif else`  

>[!v] Check their asm

