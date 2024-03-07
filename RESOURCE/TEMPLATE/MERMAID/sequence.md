```mermaid
sequenceDiagram
    CPU ->> +程序 : 处理程序
    程序 -->>+服务器 : 发送网络请求
    服务器 -->> 程序 : 返回响应结果
    CPU -->> 程序 : 处理程序
```

