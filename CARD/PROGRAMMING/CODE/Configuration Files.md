---
file-created: 2023 11 23
last-modified: 2023 11 28
---

>[!note] 常见的配置文件有
>xml,json,toml,yaml,txt 


## 常见格式 

* Key Value Pair
* Array
* Nest

## XML


## JSON

>[!note] 全称是 JavaScript Object Annotation , 看上去是js的一个对象,其实就是其序列化之后的格式. 

>[!example] 
>```json
>
>```


## Toml

>[!example] 
>```toml
>Delay = 2000
Command = 'go build -o main.exe && main.exe'
WatchFiles = ['go']
IgnoreFolders = ['node_modules', 'vendor', '.git', '.idea', '.vscode', 'log', 'build', 'dist', 'bin', 'public', 'target', 'output']
>```

## Yaml


>[!example]
>```yaml
>name: Bard
age: 2
skills:
>   - programming
>   - machine learning
>   - natural language processing
> 
> ```
>



## 优劣对比

>[!note] 考虑标准
>我将从,可读性,解析效率,的角度来比较它们. 叠加: 可能存在部分主观因素影响. 

### 可读性

>[!note] 配置文件是给人看的,所以可读性很重要


### 解析效率

>[!note] 解析效率其实没有那么从重要,因为通常情况下只需要在程序启动时加载配置文件 

### 是否支持注释 

>[!note] 是的,有的配置文件是不支持注释的
>例如json在5.0之前就不支持注释. 
>



## 总结 

>[!tip] 配置文件总体差异不大,很多时候选择更多的是因为历史遗留问题和习惯问题 
>但是如果日后有机会的话,我个人将选择[[Configuration Files#Toml|toml]]作为我主要的配置文件格式. 


