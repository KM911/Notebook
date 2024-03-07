---
file-created: 2023 08 26
last-modified: 2023 12 08
---

>[!faq] How can we compare the performance of two functions? 
>Is measuring their execution time once enough to be reliable? Will different inputs result in different performance?

>[!done] go benchmark
>To solve above problem, go provide a special tool to measure performance. 

>[!example] Benchmark Example
>1. create a file `xxx_test.go`
>2. write some special function like below .
>```go
> package bench
> func BenchmarkFunction(b *testing.B) {
> 	b.ReportAllocs()
> 	for i := 0; i < b.N; i++ {
> 		// function operation
> 	}
> }
>```

```bash
go test -bench .
```

```output
BenchmarkFunction-12         34040             36665 ns/op          350178 B/op         14 allocs/op
```


