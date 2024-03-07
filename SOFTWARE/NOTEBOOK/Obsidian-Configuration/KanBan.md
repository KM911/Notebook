

>[!note] 效果预览



>[!faq] 为什么KanBan要好于 Table of Content
>解决了graph view污染问题. 

>[!bug] 避免出现这样的情况
>![](KanBan-20240108231421652.webp)

>[!done] KanBan避免路径树无意义
>如果我们在Readme,这样的文件中创建一个 目录(table of content) , 就会导致出现下面的情况 -- 一个大的核心概念有n多个小的从属概念,容易出现"拥堵" 

>[!missing]- 早期的错误
>最开始我使用obsidian url 方式来链接其他文件(不会被graph view 收录) ,但是这样的坏处就是当文件移动后,不会更新obsidian url. 考虑到移动/重命名文件还是非常高频率的操作就放弃了这种方案. 


>[!tip] 最终解决方案
>使用intneral link 进行链接,但是在graph view 中利用正则表达式忽略看板. 

>[!note] 看板都应该遵守 `xxxxx_Kanban`的命名格式(下划线是必须的)

