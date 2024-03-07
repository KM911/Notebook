---
file-created: 2023 11 15
last-modified: 2023 12 01
---

>[!tip] 要求
>可以参考 [[go install]]
>唯一不同的是, 因为我们发布的是一个`package` , 所以不应该存在 `main` 函数.   
## example

```go
// go.mod
module github.com/KM911/bdg

go 1.21
```

```go
// your repo .go file
package bdb
```


```go
// other repo
package main

import "github.com/KM911/bdg"
func main(){
    data:= "main.go"
    bdb.CheckVar("data",data)
}
```
