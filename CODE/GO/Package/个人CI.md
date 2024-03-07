---
file-created: 2023 11 28
last-modified: 2023 11 30
---

寒假再来写吧 现在全部的时间都交给复习流程好吧. 

## 我不喜欢gitlab的CI/CD流程 


>[!v] 利用`chroot` 和 硬链接 尝试实现隔离 


>[!tip] 利用 `docker run /bin/bash -c` 来明确是否执行成功 
>


我们这样就可以不用担心我们的程序影响我们的环境了,不是吗? 

你好聪明啊. 


### 方案二

1. 运行容器并设置name , 让其执行命令
```bash
docker run  -d --name C-name alpine /bin/sh -c ls
```

2. 获取该容器退出的状态码 
```bash
docker inspect CI-test
```

解析一下json就好了,不是非常复杂. 不过这里其实只有一个有用的信息不是吗? 
```json
"State": {
    "ExitCode": 0,
    ...
}
```

容器执行结果就都可以知道了, 结合我们的程序

完美就是这样. 


```go
container_create()
container_execute()
container_check_result()
container_destroy() 
```

