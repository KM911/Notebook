

先锐评一波go的RPC实现,我觉得不是很理想,主要是在调用方,我们是通过手动输入MethodName和可变参数传递input和output,没有发挥接口的作用.应该是

Go语言不是面向对象的,但是还是有interface,你可以立即为一种特殊的类型约束,我已经忘记Java里的interface.


`````col
````col-md
flexGrow=
===
```go
    Input := RpcArgv{Input: 100}
    var output RpcReply
    err :=client.Call("Api.StructBB", Input, output)
```
````
````col-md
flexGrow=1
===
调用方利用一个字符串来申明具体调用哪个函数,然后进行传参,其中argv和 reply的类型为 any,没有类型约束,可能会因为传的类型不对导致函数失败,所以可能需要一个更加好的rpc框架了.
````

`````
