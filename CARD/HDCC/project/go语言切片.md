---
file-created: 2023 12 03
last-modified: 2023 12 05
---
>[!bug] 还未完成！！
>算了，想知道扩容后的容量大小，最好的方式就是运行....而不是深究底层算法，然后拿手算


>[!note] 前言
>在go语言中，如果在`len==cap` 的时候再次添加元素，就会触发扩容机制
>
>1.18之前扩容机制
> 1. 
> 2. 如果当前切片的长度小于 1024 就会将容量翻倍；
> 3. 如果当前切片的长度大于 1024 就会每次增加 25% 的容量，直到新容量大于期望容量；
> 
>1.18及之后
> 1. 原容量超过40之后就不是简单的2倍了
> 2. 如果当前切片的长度(容量)小于阈值（默认 256）就会将容量翻倍；
> 3. 如果当前切片的长度(容量)大于等于阈值（默认 256）即 newcap = oldcap+0.25 * (oldcap + 256)；
> 4. 最后还会根据你的数据类型进行内存对齐(eg:整型)；、
> 5. 触发扩容机制会创建新的切片，也就是append之后返回的是一个新的切片，原切片并没有增加元素哈哈




### 废话

我创建了一个整形切片，容量为100，已经满了，现在我再添加元素，理应进行扩容并且因为没有超过阈值（256），容量应该是原来的两倍 即200

>[!note] go
> ```go
> package main
> import "fmt"
> func main(){
> 	arr2 := make([]int, 100)
> 	arrAft2 := append(arr2, 1)
> 	fmt.Println("添加之前长度", len(arr2), "容量", cap(arr2))
> 	fmt.Println("添加之后长度", len(arrAft2), "容量", cap(arrAft2))
> }
> ```

但是却是 224，这就是go语言的内存对齐机制导致的。源代码中给出了我们计算方法：

在源码中规定了，如果我们的类型所占字节与`goarch.PtrSize`（8byte）相同,那我们最终的容量应该由下方代码计算。

newcap就是我们扩容后的容量 我们给`roundupsize`的参数是 200 * 8
200 = 100 * 2 是我们预计的容量，而8是 `goarch.PtrSize` 的大小,
`uinpyr(newcap)=200`
```go
capmem = roundupsize(uintptr(newcap) * goarch.PtrSize)
newcap = int(capmem / goarch.PtrSize)
```
------------------------------*-*-----------------------------------------

由于我们的size为1600 > 1024-8 所以我们
`return uintptr(class_to_size[size_to_class128[divRoundUp(size-smallSizeMax, largeSizeDiv)]])`
所以 首先要计算divRoundUp（）函数的返回值，这个函数在下方
```go
const (
	_MaxSmallSize   = 32768
	smallSizeDiv    = 8
	smallSizeMax    = 1024
	largeSizeDiv    = 128
	_NumSizeClasses = 68
	_PageShift      = 13
)

func roundupsize(size uintptr) uintptr {
	if size < _MaxSmallSize {
		if size <= smallSizeMax-8 {
			return uintptr(class_to_size[size_to_class8[divRoundUp(size, smallSizeDiv)]])
		} else {
			return uintptr(class_to_size[size_to_class128[divRoundUp(size-smallSizeMax, largeSizeDiv)]])
		}
	}
	if size+_PageSize < size {
		return size
	}
	return alignUp(size, _PageSize)
}
```


size=1600
```go
//divRoundUp函数
const (
	smallSizeMax    = 1024
	largeSizeDiv    = 128
)
divRoundUp(size-smallSizeMax, largeSizeDiv)
//divRoundUp(1600-1024,128)
func divRoundUp(n, a uintptr) uintptr {
	// a is generally a power of two. This will get inlined and
	// the compiler will optimize the division.
	return (n + a - 1) / a
}
```

返回值为 5（向下取整）
>[!note] python
> ```python
> print((1600-1024+128-1)/128)
> ```



下面这一步是计算我们的 最终容量
>[!note] python
> ```python 
> size_to_class128 = [32, 33, 34, 35, 36, 37, 37, 38, 38, 39, 39, 40, 40, 40, 41, 41, 41, 42, 43, 43, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 48, 48, 48, 49, 49, 50, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 53, 53, 54, 54, 54, 54, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60,
> 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67]
> class_to_size = [0, 8, 16, 24, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 288, 320, 352, 384, 416, 448, 480, 512, 576, 640, 704, 768, 896, 1024, 1152, 1280, 1408, 1536, 1792,2048, 2304, 2688, 3072, 3200, 3456, 4096, 4864, 5376, 6144, 6528, 6784, 6912, 8192, 9472, 9728, 10240, 10880, 12288, 13568, 14336, 16384, 18432, 19072, 20480, 21760, 24576, 27264, 28672, 32768]
> 
> 
> print(class_to_size[size_to_class128[5]])
> print(class_to_size[size_to_class128[5]]/8)
> 
> ```

运行之后可以看到是224，yes!
容量为1000 也可以采用类似的方法计算，由于1000超过阈值(256)，所以1000的理论值为 1000 + 0.25*（1000+256）

参考文献 [CSDN#点击跳转](https://blog.csdn.net/qq_42763782/article/details/129717567?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-129717567-blog-105844125.235%5Ev39%5Epc_relevant_default_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-129717567-blog-105844125.235%5Ev39%5Epc_relevant_default_base&utm_relevant_index=2)
