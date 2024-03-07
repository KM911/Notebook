---
file-created: 2023 12 08
last-modified: 2023 12 08
---


优化效果 =


10000 times slice append vs R/W file one times 

>[!example] go benchmark
>```go
>package IO
> 
> import (
> 	"os"
> 	"testing"
> )
> 
> func AppendCase() {
> 	s := make([]int, 10)
> 	for i := 0; i < 10000; i++ {
> 		s = append(s, i)
> 	}
> 	//	free
> 	s = nil
> }
> 
> func IOCase() {
> 	filename := "test.txt"
> 	//write
> 	os.WriteFile(filename, []byte("hello world"), os.ModePerm)
> }
> 
> func BenchmarkAppend(b *testing.B) {
> 	b.ReportAllocs()
> 	for i := 0; i < b.N; i++ {
> 		AppendCase()
> 	}
> }
> 
> func BenchmarkIO(b *testing.B) {
> 	b.ReportAllocs()
> 	for i := 0; i < b.N; i++ {
> 		IOCase()
> 	}
> }
> 
>```


>[!note] Benchmark Result
>Writing "hello world" to a file is approximately 20 times slower than performing a 10,000-element slice append operation.
```txt
BenchmarkAppend
BenchmarkAppend-12         31252             38010 ns/op          350178 B/op
              14 allocs/op
BenchmarkIO
BenchmarkIO-12             16002             77040 ns/op             688 B/op
               4 allocs/op
```

>[!tip] Conclude 
>In most cases, I/O operations are significantly slower than other operations, making them the critical bottleneck for performance optimization. Therefore, your efforts should primarily focus on optimizing I/O operations. Avoid wasting time on non-essential tasks.
