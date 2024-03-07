

>[!note] 一个解析toml的库 
>[toml package - github.com/pelletier/go-toml/v2 - Go Packages](https://pkg.go.dev/github.com/pelletier/go-toml/v2@v2.1.0)


## 使用教程 

我们经常会有配置文件解析的场景,关键在于go这种静态类型语言,对于配置文件是比较头痛的. 因为我们必须定义配置文件的格式,将其作为一个结构体,类似于ORM. 




其实我们的函数功能已经完善了,不需要我们做其他的事情了,因为我们只需要两个使用场景. 

检测当前项目是否存在配置文件,如果有加载. 反之退出程序,同时创建配置文件. 

所以我们需要做的唯一一个事情就是定义其格式就好了


## toml的缺陷 

>[!warning] toml不适合表达复杂的逻辑结构
>虽然这句话感觉对于哪一种逻辑结构都是对的,是一句正确的废话,但是我还是要说,因为toml中表达一对多的关系时,一旦不是简单元素的数组,就会变得分崩离析. 
>

```toml
[[Applications.ExecuteBoxs]]
ExecuteCommand = './sapkin'
ExecuteCommandArgs = []
ExecuteCommandEnv = []
ExecuteCommandDir = ''
ExitCode = 0

[[Applications.ExecuteBoxs]]
ExecuteCommand = 'go run main.go'
ExecuteCommandArgs = []
ExecuteCommandEnv = []
ExecuteCommandDir = ''
ExitCode = 0
```

所以如果存在表示一对多的需求的,我建议还是使用json比较好. 

## json in go

官方库 : json