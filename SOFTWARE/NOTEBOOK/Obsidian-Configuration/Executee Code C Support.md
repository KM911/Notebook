---
file-created: 2023 11 30
last-modified: 2023 11 30
---

>[!note] [[Execute Code]]的实现原理黑盒尝试. 

## 获取参数模板 

当我们不知道其执行逻辑的时候,我们最好的方法就是试试看 ,我们可以获取到全部的参数

```go
import (
    "os"
)
func main(){
	for index, arg := range os.Args {
		println(index, arg)
	}
}
```


大部分的执行都是利用这样的效果,然后将其 stdout 的信息显示. 基本上就是这个逻辑,还是比较简单的 .

## C的兼容层

其实和其平时的语言处理是一致的,就是将其保存到一个文件中,然后编译该文件,执行该文件. 就完成了,所以代码量不是很多. 

对啊为什么不采用一致的处理方式呢? 还是为了部分feature的实现. 


## 兼容shell

其实可以看出来,就是只需要将路径转换一下变成wsl模式下的路径就好了. 
比如变成`/mnt/d/path/temp/temp_1701336636409.sh` 这个兼容层我很快就可以写好. 

```
args:  4
0 test-argv.exe
1 -u
2 root
3 D:\PATH\TEMP/temp_1701336636409.sh
```