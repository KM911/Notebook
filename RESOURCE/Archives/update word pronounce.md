---
file-created: 2023 11 30
last-modified: 2023 11 30
---

> [!done ] 查看效果 [[CARD/English/pronounce]]

>[!note] 为什么行
> 1. 为了提高程序的性能,大部分文本编辑器都会选择在开始将文件加载到内存中,平时的编辑于修改都是在修改内存,只有当保存时才会将数据写入磁盘. 换言之,其并没有占据该文件,我们可以进行修改操作. 
> 2. 利用[[Execute Code]]执行我们提前编写好的程序,处理文件. 

>[!tip] 有道翻译单词发音API 
>利用query传参 , audio=单词，type=0为美国发音，type=1为英国发音
>"https://dict.youdao.com/dictvoice?audio=pronounce&type=1"


## 代码实现 

>[!note] 简单的字符串处理
>表格会以字符 "|" 开头, 利用这个判断是否执行`ChangeRowContent` , 同时为了避免重复执行, 还需要检验当前单元内是否以及有 音频了. 
>

```python
import sys 
allowed_filenames = ["pronounce.md"]

assert len(sys.argv) == 2, "must have one argument"


file = open(sys.argv[1], "r", encoding="utf-8")
lines = file.readlines()
file.close()


def ChangeRowContent(row_content)-> str :
    new_row_content = [ x.strip() for x in row_content.split("|") ]
    if new_row_content[3] == "":
        return f'| {new_row_content[1]} | {new_row_content[2]} | <audio controls="controls" preload="none" src="http://dict.youdao.com/dictvoice?type=0&audio={new_row_content[1]}"></audio> | <audio controls="controls" preload="none" src="http://dict.youdao.com/dictvoice?type=1&audio={new_row_content[1]}"></audio> | \n'
    else:
        return row_content


read_file = open(sys.argv[1], "w", encoding="utf-8")
for index in range(len(lines)):
    if not lines[index].startswith("|"):
        read_file.write(lines[index])
        continue
    read_file.write(ChangeRowContent(lines[index]))
read_file.close()
```