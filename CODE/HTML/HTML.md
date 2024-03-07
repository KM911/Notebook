---
file-created: Thursday, November ,2023
last-modified: Saturday, November ,2023
---

[[vue]]

[[PROJECT/TRICK/CSS]]



## 构建你自己的卡片 

首先灵感来自-- 当初我想要美化自己的github主页的时候的事情了.然后就开始接触这些事情了. 



![%E5%86%99%E4%BD%9C%E5%B7%A5%E5%85%B7-typora-blue](https://img.shields.io/badge/%E5%86%99%E4%BD%9C%E5%B7%A5%E5%85%B7-typora-blue) ![%E5%86%99%E4%BD%9C%E5%B7%A5%E5%85%B7-typora-blue](https://img.shields.io/badge/%E5%86%99%E4%BD%9C%E5%B7%A5%E5%85%B7-typora-blue)

简单的处理一下请求的url就好了,还是非常简单的不是吗? 

该请求会返回一个svg,浏览器会自动渲染它,就可以得到上面的结果了,我们现在如果要做的话,就是去拼接字符串来构造下面的这个svg就好了. 

```svg
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100" height="20" role="img" aria-label="写作工具: typora"><title>写作工具: typora</title><linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="r"><rect width="100" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#r)"><rect width="55" height="20" fill="#555"/><rect x="55" width="45" height="20" fill="#007ec6"/><rect width="100" height="20" fill="url(#s)"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><text aria-hidden="true" x="285" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="450">写作工具</text><text x="285" y="140" transform="scale(.1)" fill="#fff" textLength="450">写作工具</text><text aria-hidden="true" x="765" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="350">typora</text><text x="765" y="140" transform="scale(.1)" fill="#fff" textLength="350">typora</text></g></svg>
```