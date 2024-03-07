

## api-platform 

>[!quote] 灵感来源于vercel,它允许你部署你的nodejs项目.
>所以我想实现一个可以部署go的api管理平台,或者这个应该叫做云函数是吗? 


## 可行性分析 

>[!faq] go需要编译,无法像nodejs一样直接利用moduel直接引入. 
>并且该如何定义request和respond呢? 


我们先看看nodejs的实现好吧. 


>[!v] 尝试利用代码生成
>我们可以获取api目录下的文件,生成最终的router不就好了吗? 

