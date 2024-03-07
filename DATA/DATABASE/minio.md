---
file-created: 2023 11 15
last-modified: 2023 11 26
---

````col
```col-md
flexGrow=1
===
> [!note] 定义
> 


> [!tip] 相关概念
> 
```
```col-md
flexGrow=1
===
> [!info] 别称
> 

> [!cite]- 参考资料
> 
```
````


[MinIO | Code and downloads to create high performance object storage](https://min.io/download#/linux)

## 安装

```bash
minio server 
```


```bash
mc alias set 'myminio' 'http://10.21.87.168:9000' 'admin' 'password' 
```

利用dashboard登陆 
```

```

## bucket 

a container for items. 

## get accessKey

it is very easy to see the accessKye , espcial when it was . 


### go quick demo 

this will create a bucket and upload main.go file into your minio server . 
```go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/minio/minio-go/v7"
	"github.com/minio/minio-go/v7/pkg/credentials"
)

func main() {
	ctx := context.Background()
	endpoint := "localhost:9000"
	accessKeyID := "2pOTJkwyjLIF3NyfsGwr"
	secretAccessKey := "s3IWiCzShHnZk5qFf3hKLgLRoNBXyEyeWMWRRAy2"
	useSSL := false

	// Initialize minio client object.
	minioClient, err := minio.New(endpoint, &minio.Options{
		Creds:  credentials.NewStaticV4(accessKeyID, secretAccessKey, ""),
		Secure: useSSL,
	})
	if err != nil {
		fmt.Println("connetc error")
		log.Fatalln(err)
	}

	bucketName := "test"
	// location := "us-east-1"

	err = minioClient.MakeBucket(ctx, bucketName, minio.MakeBucketOptions{})
	if err != nil {
		// Check to see if we already own this bucket (which happens if you run this twice)
		exists, errBucketExists := minioClient.BucketExists(ctx, bucketName)
		if errBucketExists == nil && exists {
			log.Printf("We already own %s\n", bucketName)
		} else {
			log.Fatalln(err)
		}
	} else {
		log.Printf("Successfully created %s\n", bucketName)
	}

	objectName := "main.go"
	filePath := "main.go"
	contentType := "application/octet-stream"
	info, err := minioClient.FPutObject(ctx, bucketName, objectName, filePath, minio.PutObjectOptions{ContentType: contentType})
	if err != nil {
		log.Fatalln(err)
	}
	log.Printf("Successfully uploaded %s of size %d\n", objectName, info.Size)
}

```

### give download priviage 

```bash
mc  anonymous set  download myminio/test
```

```bash
weget http://localhost:9000/test/main.go
```

this will download it. 

## 前后端协作 

这里其实sendfile是不合理的,如果是接收的文件呢? 


## 我现在还有一个问题没有解决

我需要学会构建/模拟集群 不然的话我根本就无法使用/体会到分布式的作用,加上使用`localhost`会让你认为你的服务非常有用,但是我只能说不太行. 




CDN

```mermaid
flowchart LR
    A["浏览器]-->B["CDN"]
    B-->C["服务器"]     
```


简单理解就好了,


DNS和CDN其实是一个中间件不过功能不同罢了,帮助你去了解真实世界还是有非常大的帮助的不是吗? 


```mermaid
flowchart LR
    A["用户设备"] --> B["路由中心A"] 
    B-->A
    B --> C["路由中心B"]
    C --> B
    C --> D["服务器"]
    D -->C
```



```mermaid
flowchart LR
    A["浏览器"] --> B["CDN"] 
    B --> |接口请求|C["服务器"]
   B --> |静态资源| A
```


