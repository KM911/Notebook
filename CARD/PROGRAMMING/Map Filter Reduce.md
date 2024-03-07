---
file-created: 2023 11 15
last-modified: 2023 11 29
---

>[!example] 你现在想要将一个数字切片中为负数的值变为正数.通常的做法是像Method1一样遍历切片,处理元素后赋值,得到全新的切片.Method2将遍历这个过程隐藏了起来,并且将要执行的函数作为参数,这样的好处是提高了复用性,如果以后你需要将数字切片中的元素开根号或者是其他形式的运算,只需要编写对应的函数并将其作为参数传给Map函数就好了.
>

```go
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Map[T, R any](array []T, callback func(T) R) []R {
	result := make([]R, len(array))
	for i := 0; i < len(array); i++ {
		result[i] = callback(array[i])
	}
	return result
}

func Method1(){
	num1 := []int{1, -22, -33, 4, 5}
	num2 := make([]int, len(num1))
	for i := 0; i < len(num1); i++ {
		num2[i] = Abs(num1[i])
	}
	fmt.Println(num2)
}

func Method2() {
	num1 := []int{1, -22, -33, 4, 5}
	num2 := Map(num1, Abs)
	fmt.Println(num2)
}
```

我们现在可以给Map一个简单的定义
Map: list($a_1,a_2... a_n$) --> list($b_1 ,b_2,...b_n$)

Filter: list($a_1,a_2... a_n$) --> list($b_1 ,b_2,...b_m$) 
Reduce: list($a_1,a_2... a_n$) --> target 


这只是函数式编程中的一个特性:高阶函数,将函数作为参数的一部分,可以提高代码的复用率.
函数式编程还有很多特性,例如纯函数,不可变性...感兴趣的可以去了解一下. 
 个人其实不是很喜欢函数式编程,或者说不喜欢严格遵守其特性.
 比如根据不可变性,你不应该修改参数的值,这不可避免要创建新的变量并为其分配内存,从而影响程序的运行效率.


