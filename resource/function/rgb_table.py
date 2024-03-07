import sys
import os
import lib.files as files
import lib.std as std
import lib.table as table

# define table format
# |RGB| Example|





# TODO : keywords 
Key_Words = ["RGB","Example"]



KeyWords = {}
for item in Key_Words:
    KeyWords.setdefault(item,-1)




def ProcessTitle(content : str) -> str:
    
    titles = [ x.strip() for x in content.split("|") ]
    global KeyWords
    for i in KeyWords.keys():
        index = std.Find(titles, i)
        if index != -1:
            KeyWords[i] = index
    for v in KeyWords.values():
        if v == -1:
            print("can not find the key words")
            os._exit(1)
            pass
    global ReplaceTableContent
    ReplaceTableContent = ProcessFlags
    return content

def ProcessFlags(contents : list):
    global ReplaceTableContent
    ReplaceTableContent = ProcessTableContent
    return contents



def ProcessTableContent(content : list) -> str:
    cells = [ x.strip() for x in content.split("|") ]
    # TODO  : modify content
    cells[KeyWords["Example"]] = f'<div style="color:{cells[KeyWords["RGB"]][1:-1]}">{cells[KeyWords["RGB"]][2:-1]}</div>'
    res =  table.tableFormatOutput(cells)
    print(res)
    return res
    


ReplaceTableContent = ProcessTitle
contents = files.ReadFileContent(sys.argv[1])

def main():
    global ReplaceTableContent
    for index in range(len(contents)):
        if not contents[index].startswith("|"):
            ReplaceTableContent = ProcessTitle
            continue
        else:
            print("process title")
            contents[index] = ReplaceTableContent(contents[index])

    # 写入失败了还是怎么说
    print(contents)
    files.SaveFileContent( contents)

main()