

>[!note] SheBang 
>Shebang  shi-BANG sha-bang  hashbang

>[!note] How to run this file 

>[!example] file.sh
> ```bash
> #! /bin/bash
> ls
> ```
>
> 实际上的操作. 将当前文件路径作为参数传给Shebang
> ```bash
> /bin/bash file.sh
> ```

> [!example] 测试 添加参数 
> ```bash
> #! test-argv hello wrold just do ti  
> echo "hello world"
> ```
> 会将 后续参数会作为一个整体     
> ```bash
> test-argv "hello wrold just do it" file.sh
> ```
> 



