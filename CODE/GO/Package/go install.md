---
file-created: 2023 11 29
last-modified: 2023 12 01
---

>[!note] go install
> compile and install packages and dependencies

>[!faq] 如何快速发布软件呢? 
>我们有的时候会提供一些工具给用户,如何快速分发呢? 


>[!tip] 要求 
>1. go.mod init 作为GitHub repo的地址. 
>2. 发布tags
>3. 项目必须是可编译的,不是 `package` [[publish your go package]]. 

>[!faq] 在我没有上传仓库前,岂不是无法编译?
>不是的,在本地项目时, go.mod 下的名字只是为了区分而已.

发布了tags以后, 你就可以利用 `go install github.com/KM911/repo` 下载你的软件包了.  