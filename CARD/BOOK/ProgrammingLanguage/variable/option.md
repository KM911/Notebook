
>[!exp]

>[!faq] 什么时候会变成空或者Null 
>1.数据库查询不到对应的数据. 
>2.网络请求超时
>3.异常


>[!tip] 意义
>The purpose of Optional is not to replace every single null reference in your codebase but rather to help design better APIs in which—just by reading the signature of a method—users can tell whether to expect an optional value. In addition, Optional forces you to actively unwrap an Optional to deal with the absence of a value; as a result, you protect your code against unintended null pointer exceptions.

>[!tip] Force you to actively unwarp an optional to deal with the absence of a value . 

>[!note] 但是实际上还是没有足够地好. 



>[!note] 相关内容
>[[rust option]]