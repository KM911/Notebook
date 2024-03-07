---
file-created: 2023 11 25
last-modified: 2023 11 30
---

## Table of Content

目前已知的排序算法


>[!faq] 排序算法的稳定性是什么意思?

我们说快速排序是不稳定的，是因为在快速排序的过程中，可能会交换相同元素的位置，从而导致相同元素的相对顺序被改变。




## Bubble Sort 

>[!note] 形式类似泡泡上浮的过程,因此得名. 
>每次比较相邻两个元素的值 

解释这种事情其实我都觉得不需要,只要我们去收集就好了


>[!example]-  Bubble Sort 
> ```go
> func bubbleSort(arr []int) {
>     for i := len(arr) - 1; i >= 0; i-- {
>         for j := 0; j < i; j++ {
>             if arr[j] > arr[j+1] {
>                 arr[j], arr[j+1] = arr[j+1], arr[j]
>             }
>         }
>     }
> }
> ```

 >[!example]- Insert Sort
> ```go
> func insertionSort(arr []int) {
> 	for i := 1; i < len(arr); i++ {
> 		key := arr[i]
> 		j := i - 1
> 		for j >= 0 && arr[j] > key {
> 			arr[j+1] = arr[j]
> 			j--
> 		}
> 		arr[j+1] = key
> 	}
> }
> ```

>[!example]- Quick Sort
> ```go
> func quickSort(arr []int, low, high int) {
> 	if low < high {
> 		pivot := partition(arr, low, high)
> 		quickSort(arr, low, pivot-1)
> 		quickSort(arr, pivot+1, high)
> 	}
> }
> 
> func partition(arr []int, low, high int) int {
> 	pivot := arr[high]
> 	i := low - 1
> 	for j := low; j < high; j++ {
> 		if arr[j] <= pivot {
> 			i++
> 			arr[i], arr[j] = arr[j], arr[i]
> 		}
> 	}
> 	arr[i+1], arr[high] = arr[high], arr[i+1]
> 	return i + 1
> }
> ```


## Benchmark 

我们进行多种不同长度的不同混乱程度的排序. 


```
%% 要是 可以识别然后进行go test %% 我就称其为绝杀
```