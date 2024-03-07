---
file-created: 2023 11 15
last-modified: 2023 11 30
---

#### 理解host作用
> [!note] 本地DNS 


1. 屏蔽网址
2. 避免DNS污染
3. 提高访问速度 

##### win10 host文件位置
```bash
C:\Windows\System32\drivers\etc\hosts
```

##### 文件配置格式

这里通过将谷歌更新重定向到本机,避免其自动更新,方便我们开发. 

```
127.0.0.1 update.googleapis.com
127.0.0.1 zhihui.com
```

##### 清空缓存
```bash
ipconfig /flushdns
```

##### 查看本机DNS
```bash
ipconfig /displaydns 
ipconfig /displaydns  >> test.txt   # 通过查询判读
```
