---
file-created: 2023 11 21
last-modified: 2023 11 30
---


counter : 

>[!example!]- go实现 
>```go
> type Limiter struct {
> 	limit     int
> 	window    time.Duration
> 	count     int
> 	lastCheck time.Time
> }
> 
> func NewLimiter(limit int, window time.Duration) *Limiter {
> 	return &Limiter{
> 		limit:  limit,
> 		window: window,
> 		count:  0,
> 	}
> }
> 
> func (l *Limiter) Allow() bool {
> 	now := time.Now()
> 	if now.Sub(l.lastCheck) > l.window {
> 		l.count = 0
> 		l.lastCheck = now
> 	}
> 
> 	if l.count < l.limit {
> 		l.count++
> 		return true
> 	}
> 	return false
> }
> 
> func main() {
> 	l := NewLimiter(10, time.Second)
> 	for i := 0; i < 20; i++ {
> 		if l.Allow() {
> 			fmt.Println("allow")
> 		} else {
> 			fmt.Println("deny")
> 		}
> 	}
> }
> ```

>[!error] 流量波峰 
>假设设置为1秒内运行100个请求,在0.99s发送100个请求,然后在1.01s后再发送100个请求.还是存在一个可能的流量波峰. 


leaky bucket : 

>[!note]- go实现
>```go
>
>```


token bucket : 
