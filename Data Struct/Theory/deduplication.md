---
file-created: 2023 11 25
last-modified: 2023 11 30
---

>[!note] 去重首先需要定义什么是"重". 
>1. 什么是重,对于普通类型,比如int,两者的值相同就是 "重",对于对象而言,是其全部的属性都相同还是 ? 

## array

目前看来基于hashmap的O(n), 复杂度的应该是最好的了. 


```go
func HashDeduplication(array []int) []int {
	hashMap := make(map[int]bool)
	for _, number := range array {
		hashMap[number] = true
	}
	distinctNumbers := []int{}
	for number := range hashMap {
		distinctNumbers = append(distinctNumbers, number)
	}
	return distinctNumbers
}

func Deduplication(array []int) []int {
	distinctNumbers := []int{}
	for _, number := range array {
		exists := false
		for _, distinctNumber := range distinctNumbers {
			if number == distinctNumber {
				exists = true
				break
			}
		}
		if !exists {
			distinctNumbers = append(distinctNumbers, number)
		}
	}
	return distinctNumbers
}
```

如何不开辟新的空间然后时间复杂度也可以低一点呢? 

这里可以将前面的数组排序,这样去重就简单多了不是吗? 