
## Simple Message Transfer Protocol


其实你不需要知道其具体实现，会利用就好了。 你不必知道全部的细节。 

## 不要尝试自己搭建邮箱 

为什么？ 因为费力不讨好。 

首先，为了屏蔽 "垃圾邮件",会自动将自建邮箱地址视为"垃圾邮件". 所以即使你花费了时间搭建了邮箱,也可能无法使用. 

其次,商业邮箱服务以及非常成熟了,并且大部分邮箱长期免费.你很难从中得到获得额外的便利和商业价值. 

就算你希望你可以和少部分群体进行交流,使用http/websocket等完全可以实现你的想法,并且还可以定制客户端. 

综上所述,我找不到你花费时间和精力去深入了解比如SMTP的意义. 但是我还是推荐你可以将下面的内容了解一下,可以利用邮件来提醒自己. 
## 利用qq邮箱发送文件

1.开通邮箱的POP3/SMTP服务,以QQ邮箱为例

设置--> 账号--> POP3/SMTP服务 --> 开启服务
![[Pasted image 20231110085414.webp]]

![[Pasted image 20231110085537.webp]]

这里是因为我已经开启成功了,未开启需要一定的验证流程, 验证完成后会给以一个<span class="r">密钥</span>,需要保留下来.
 
![[Pasted image 20231110085552.webp]]

我们现在称密钥为 "token". 


## 邮件大致格式 

from  : xxxx@qq.com
to  : zzz@qq.com
title : 
content : could be html

### basic knowledge 

>[!note] 邮件可以进行html的渲染
>这也解释了例如github的邮件是如何进行美化的. 
>![](SMTP-20240126160010977.webp)



>[!warning] 部分邮箱兼容性比较差(不支持xx选择器)
>为了设置element的样式需要在element 内部 使用 style="xxx:xxx;" 来实现, 不过通过测试,qq邮箱是可以使用的. 



### go 发送邮件


>[!warning] 会自动将 content中的 `\n` 转为`<br>` 
>为避免格式错误,请先将其"压缩". html压缩 : google

参考资料 : [发邮件 · Go语言中文文档](https://www.topgoer.com/%E5%85%B6%E4%BB%96/%E5%8F%91%E9%82%AE%E4%BB%B6.html)

```bash
go get github.com/jordan-wright/email
```

```go
func main (){
	e := email.NewEmail()
	e.From = qq.FromName + " <" + qq.From + "@qq.com>"
	e.To = []string{_toName + " <" + _to + "@qq.com>"}
	e.Subject = _subject
	e.Text = []byte(EmailTemplateHeader + EmailBuilder.String() + EmailTemplateFooter)
	err := e.Send("smtp.qq.com:25", smtp.PlainAuth("", qq.From, qq.Token, "smtp.qq.com"))
	if err != nil {
		return false
	} else {
		return true
	}
}
```

### python 发送邮件 



## 使用案例 

当系统出现了不可恢复的故障,例如无法连接数据库导致的异常出现时,可以通过发送邮件来提醒. 

```go
func main(){
    recover 
}

```