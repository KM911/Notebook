
## regex

>[!faq] regex 是什么 ? -- 解决了什么问题 ? 
>正则表达式是一种用于`字符串模式匹配`的工具. 

>[!done] 推荐学习资料
>[Regex 101 - ZH-CN](https://regexlearn.com/zh-cn/learn/regex101)


>[!faq]- 我是为什么开始学习regex
>因为我使用obsidian,我希望可以将KanBan从`graph view`中过滤. (需要重启生效) 

## Core Concept 


>[!tip] Regex
在大多数编程语言中，正则表达式匹配的返回值类型都是一个列表，列表中的元素是匹配到的字符串。例如，在 Python 中，可以使用 re.findall(r'\d') 方法来匹配字符串中的所有数字. 



## regex in python 

```python
import re 


```


## use regex to solve problem. 

>[!exp] find the ip of domain. 
>
> ```bash
> nslookup baidu.com
> ```

>[!warning] 这里我们想要获取其IP,如果使用比如正常的字符串处理,就比较麻烦,但是使用regex就很快速了.

>[!tip] 因为ip(v4) 肯定是 4个0-255的数字组成,中间用`.`隔开. 正则表达式可以写成. 
>`\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`

>[!example] python示例
>```python
>import re 
src = """
Server:		172.19.0.1
Address:	172.19.0.1#53
> 
> Non-authoritative answer:
> Name:	baidu.com
> Address: 39.156.66.10
> Name:	baidu.com
> Address: 110.242.68.66
> """
> regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
> result = regex.findall(src)
> print(result)
>```


### 提取日志信息 我们只要10月到11月的日志 

这个其实也非常好用不是吗? 

这里我们需要首先给出日志的格式. 

### 验证用户输入合法性 

>[!warning] All user input is evil. 

>[!exp] 1.用户输入被限制为数字和字符串 
> ```python
> import re
> 
> def is_valid_username(username):
>     pattern = r'^[a-zA-Z0-9]+$'
>     return re.match(pattern, username) is not None
> 
> print(is_valid_username('abc123'))  # True
> print(is_valid_username('abc@123'))  # False
> ```

>[!exp] 2.判断是否是电话号码 (国内电话号码必定是11位的数字)
> ```python
> import re
> 
> def is_valid_username(username):
>     pattern = r'\d{11}'
>     return re.match(pattern, username) is not None
> 
> print(is_valid_username('10123456789'))  # True
> print(is_valid_username('0123456789'))  # False
> ```
> 


## 提取wsl的ip

```go
func main() {
	ifconfig := system.ExecuteCommandSilentResult("wsl -u root bash -c ifconfig")
	regex := regexp.MustCompile("\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}")
	ip := regex.FindString(ifconfig)
	println(ip)
}

```



>[!warning] 不解释了,请你自己体会
![](regex-20240115211641921.webp)

