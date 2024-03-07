---
file-created: 2023 11 15
last-modified: 2023 11 29
---

## Mixed Content

有的时候打开网页/编写seleium时会遇到. 

Mixed Content: The page at “https://“ was loaded over HTTPS, but requested an insecure “http://“

简单来说就是目标站点是HTTPS的,但是其中部分链接是HTTP的,就会出现这个问题,我们需要在网页上添加

这样会自动将http升级为https
```html
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
```

我不知道如何解决在seleium中的问题
