import sys
import os
import re

import lib.files as files
import lib.std as std
import lib.table as table





def Iterator(contents: list):
    index = 0
    def iteration(type: str = "value"):
        nonlocal index
        if type == "index":
            return index
        if type == "prev":
            index -= 1
        elif type == "next":
            index += 1
        return contents[index]
    return iteration


def repeat(exit_flag, func):
    while True:
        if exit_flag():
            return
        else:
            func()

sys.stdout.reconfigure(encoding='utf-8')


content = files.ReadFileContent(sys.argv[1]) 
print(sys.argv[1])

# 过滤\n

# content = [line for line in content if line != "\n"]
Index= 0

def AddIndex():
    global Index
    Index+=1
# `````col
# ````col-md
# flexGrow=1
# ===
# ```css





class_pattern = r'class="([^"]*)"'
style_pattern = r'style="([^"]*)"'
tag_pattern = r'<(\w+)'

# 预先编译正则表达式
class_re = re.compile(class_pattern)
style_re = re.compile(style_pattern)
tag_re = re.compile(tag_pattern)






def find_next_css_code_block():
    global Index
    repeat(lambda : content[Index].startswith("`````col") ,AddIndex)
    # 理论上其应该后续会包含如下的内容
    # `````col
    # ````col-md
    # flexGrow=1
    # ===
    # ```css
    AddIndex()
    if content[Index].startswith("````col-md") and content[Index+1].startswith("flexGrow=1") and content[Index+2].startswith("===") and content[Index+3].startswith("```css"):
        Index +=4
        return 
    else:
        # 不是css代码块() 继续下一个
        find_next_css_code_block()

CSS = {}

def resolve_css_code_block():
    global Index ,CSS
    CSS = {}
    while True :
        tag = content[Index].split("{")[0].strip()
        Index+=1
        style = []
        def resolve_style():
            global Index
            while True:
                if content[Index].startswith("}"):
                    Index+=1
                    return
                style.append(content[Index].strip())
                AddIndex()
        # repeat(lambda : content[Index].startswith("}"),lambda : style.append(content[Index].strip()))
        resolve_style()
        if tag.startswith(".") or tag.startswith("#"):
            tag = tag[1:]

        CSS[tag] = style
        if content[Index].startswith("```\n"):
            
            break

    # pass to html code block 
    # 4 is a magic number , refer to the code block rules.
    Index+= 5


def resolve_html_code_block():
    global Index ,CSS
    while True:
        _index = content[Index].find("<")
        if  _index != -1 and content[Index][_index+1] != "/":
            tag = tag_re.search(content[Index]).group(1)
            styles_index = style_re.search(content[Index]).span() if style_re.search(content[Index]) else (-1,-1)

            classes = class_re.search(content[Index]).group(1) if class_re.search(content[Index]) else ""

            # styles 通过css 来进行解析
            styles = [] 
            styles.extend(CSS.get(tag,[]))
            if classes != "":
                for _class in classes.split(" "):
                    styles.extend(CSS.get(_class,[]))


            if styles_index == (-1,-1):
                content[Index] = content[Index].replace("<"+tag,"<"+tag+" style=\""+"".join(styles)+"\"")
            else :
                # 利用style 的 span
                content[Index] = content[Index][:styles_index[0]] +"style=\"" +"".join(styles) + content[Index][styles_index[1]-1:] 
            # print("替换后的内容",content[Index])

        elif content[Index].startswith("````\n") :
            break
        
        Index+=1

# 下一步是对于函数的封装 
if __name__ == "__main__":
    while True :
        # 通过手动抛出异常来进行退出
        try : 
            find_next_css_code_block()
            resolve_css_code_block()
            resolve_html_code_block()
        except IndexError:
            break
    files.SaveFileContent(content)
