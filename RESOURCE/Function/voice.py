import sys
import os
import lib.files as files
import lib.std as std
import lib.table as table

# define table format
# |RGB| Example|



contents = files.ReadFileContent(sys.argv[1])


KeyWords= {
    "English" : -1 ,
    "英式发音的示例" : -1,
    "美式发音的示例" : -1
}


# 其实这里应该是一个dict 

# 其对应的处理逻辑是
# replace / fit 



# 这里的split后位置有一点点问题吗

def MatchTitle(content : str) -> str:
    # 进行match 
    titles = [ x.strip() for x in content.split("|") ]
    global KeyboardInterrupt
    for i in KeyWords.keys():
        # print("items" ,i)
        index = std.Find(titles, i)
        if index != -1:
            KeyWords[i] = index

    if KeyWords["English"] == -1:
        # 应该是放弃 当前的处理逻辑保留原始结果 或者放弃整个文件的处理
        print("can not find the key words")
        # print(titles)
        os._exit(1)
        pass
    global ReplaceTableContent
    ReplaceTableContent = MatchFlags
    return content

def MatchFlags(contents : list):
    global ReplaceTableContent
    ReplaceTableContent = MatchTableContent
    return contents


# TODO : 进行处理
def MatchTableContent(content : list) -> str:
    cells = [ x.strip() for x in content.split("|") ]
    if KeyWords["美式发音的示例"] != -1:
        cells[KeyWords["美式发音的示例"]] = f'<audio controls="controls" preload="none" src="http://dict.youdao.com/dictvoice?type=0&audio={cells[KeyWords["English"]]}"></audio>'

    if KeyWords["英式发音的示例"] != -1:
        cells[KeyWords["英式发音的示例"]] = f'<audio controls="controls" preload="none" src="http://dict.youdao.com/dictvoice?type=1&audio={cells[KeyWords["English"]]}"></audio>'
    # cells[KeyWords["Example"]] = f'<div style="color:{cells[KeyWords["RGB"]][1:-1]}">{cells[KeyWords["RGB"]][2:-1]}</div>'
    res =  table.tableFormatOutput(cells)
    return res
    
    

ReplaceTableContent = MatchTitle


# 让其run起来才是真的,一点点地modify 这样才是比较合理的方式 

for index in range(len(contents)):
    # print(contents[index])
    if not contents[index].startswith("|"):
        ReplaceTableContent = MatchTitle
        continue
    else:
        contents[index] = ReplaceTableContent(contents[index])


files.SaveFileContent(sys.argv[1], contents)
