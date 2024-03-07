---
file-created: 2023 12 05
last-modified: 2023 12 05
---

跟其他语言一样，底层都是一个字符数组......
unsafe.Pointer 是一个特殊的类型，它可以包含任何类型的指针地址。你可以将任何类型的指针转换为 unsafe.Pointer，也可以将 unsafe.Pointer 转换为任何类型的指针。传说中的万金油？
```go
type stringStruct struct {
 str unsafe.Pointer
 len int
}
```

```go
//go:nosplit
func gostringnocopy(str *byte) string {
 ss := stringStruct{str: unsafe.Pointer(str), len: findnull(str)} // 先构造 stringStruct
 s := *(*string)(unsafe.Pointer(&ss)) // stringStruct 转换成 string
 return s
}
```