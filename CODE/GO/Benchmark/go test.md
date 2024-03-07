---
file-created: 2023 12 08
last-modified: 2023 12 08
---

>[!note] go test
>go test is a built-in command-line tool that enables you to write and run unit tests for your Go code. It simplifies the testing process by offering several key features:


>[!example] go test example
>create a file name format `xxx_test.go`
>```go
>package test
> 
> import "testing"
> 
> func Function() int {
> 	return 1
> }
> func TestFunction(t *testing.T) {
> 	if Function() != 1 {
> 		t.Error("Function() != 1")
> 	}
> }
> 
> func TestFunctionEqual2(t *testing.T) {
> 	if Function() != 2 {
> 		t.Error("Function() != 2")
> 	}
> }
> 
>```

```result

```


## flag explain

  

| flag | usage |
| ---- | ---- |
| v | verbose , show detail |
| c | compiler but not run |
| o | output and run  |
| args | pass args for test |

很神奇的是,我们的test 其实是生成了一个可执行文件,然后执行该文件以获取输出信息. 
说明了这是经过编译的程序,和最终生产环境的结果是一致的. 

