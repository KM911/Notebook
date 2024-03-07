
## defer and recover 

>[!tip] defer will execute even panic 
>so it is a good way to defer close file or tcp connection. 

>[!warning] panic in defer 
>this will cause current function panic

recover : capture the painc and make


1. main thread exit , goroutine will exit forcely. 
2. any goroutine panic just like main thread exit

Point Of View : Every goroutine must defer a `recover` to avoid the main thread exit. 

```go
go func(){
    defer func() {
            if r := recover(); r != nil {
                log.Error("goroutine paniqued: ", r)
            }
        }()
    // do something may cause panic 
}() 
```

defer记录的是函数的pc而不是真的一个有待执行的程序

