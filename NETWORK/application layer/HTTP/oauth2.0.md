---
file-created: 2023 11 25
last-modified: 2023 11 28
---

>[!v] oauth2 好像是提供给第三方应用的
>比如我想用vscode登陆github,它会跳转到github的验证中心,然后我就可以了? 这里好像没有第三方中心呀. 
>

## Single Sign On（SSO）

>[!note] only sign on once 


这很明显是 理念 , 让用户可以避免重复登陆. 

这个很简单,比如用户登陆时返回一个过期时间+用户id的加密字段,每次请求携带上去,这样我们就可以判断用户是否登陆了,就好了呀

众所周知，HTTP是无状态的协议，这意味着服务器无法确认用户的信息。于是乎，W3C就提出了：给每一个用户都发一个通行证，无论谁访问的时候都需要携带通行证，这样服务器就可以从通行证上确认用户的信息。通行证就是Cookie。

## CAS （Central Authentication Service）
















这段话的意思就是，OAuth 的核心就是向第三方应用颁发令牌。然后，RFC 6749 接着写道：

也就是说，OAuth 2.0 规定了四种获得令牌的流程。你可以选择最适合自己的那一种，向第三方应用颁发令牌。下面就是这四种授权方式。

授权码（authorization-code）
隐藏式（implicit）
密码式（password）：
客户端凭证（client credentials）

## 双token 

听上去是不是很高级,其实很简单 

一个token用于登陆校验,第二个token用于更新第一个token 
