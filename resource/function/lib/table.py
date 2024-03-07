

def tableFormatOutput(rows : list) -> str :
  length = len(rows)
  if length == 3:
    return f'| {rows[1]} |\n'
  elif length ==4:
    return f'| {rows[1]} | {rows[2]} |\n'
  elif length == 5:
    return f'| {rows[1]} | {rows[2]} | {rows[3]} |\n'
  elif length == 6:
    return f'| {rows[1]} | {rows[2]} | {rows[3]} | {rows[4]} |\n'
  elif length == 7:
    return f'| {rows[1]} | {rows[2]} | {rows[3]} | {rows[4]} | {rows[5]} |\n'
  elif length == 8:
    return f'| {rows[1]} | {rows[2]} | {rows[3]} | {rows[4]} | {rows[5]} | {rows[6]} |\n'
  elif length == 9:
    return f'| {rows[1]} | {rows[2]} | {rows[3]} | {rows[4]} | {rows[5]} | {rows[6]} | {rows[7]} |\n'
  else:
    return f'| {rows[1]} | {rows[2]} | {rows[3]} | {rows[4]} | {rows[5]} | {rows[6]} | {rows[7]} | {rows[8]} |\n'
  

  
def parseTableTitle(content : str):
  global ParseTableContent
  # ParseTableContent = 
  new_row_content = [x.strip() for x in content.split("|")]
  return new_row_content

def parseTableFlags(content : str) -> str:
  global ParseTableFlags
  # ParseTableFlags = 
  new_row_content = [x.strip() for x in content.split("|")]
  return new_row_content[1]

def parseTableContent(content :str) :
  global ParseTableContent
  # ParseTableContent = 
  new_row_content = [x.strip() for x in content.split("|")]
  return new_row_content[2:]



def BuildTable(data : list)-> str:
  stringBuilder = []
  stringBuilder.append(" | " + " | ".join(data[0]) + " |")
  stringBuilder.append(" | " + " | ".join(["---" for x in range(len(data[0]))]) + " |")
  for i in range(1, len(data)-1):
    stringBuilder.append(" | " + " | ".join(data[i]) + " |")
  stringBuilder.append(" | " + " | ".join(data[len(data)-1]) + " |\n")
  return "\n".join(stringBuilder)

# ParseTableContent = parseTableTitleContent





# 1 return title : list
# 2 return flags : str
# 3:n return content : list 

import pyperclip

def ConventClipIntoTable():
    # 读取剪切板
    clipboard_text = pyperclip.paste().strip()
    # print(clipboard_text)
    # 解析text
    lines = clipboard_text.split("\n")

    # 判断解析格式,因为可能有的分割符号 用的不是\t 可能是n * space. 

    
    
    for i in range(len(lines)):
        lines[i] = [x.strip() for x in lines[i].strip().split("\t")]

    #移除last line
    lines.pop() 
    return lines

def SplitCharacter(_String : str) -> str :
  stripedString = _String.strip()
  lens = len(stripedString.split("\t"))
  for i in range(1,8):
    new_lens = len(stripedString.split(i*" "))
    if new_lens > lens :
      return i*" "
  return "\t"