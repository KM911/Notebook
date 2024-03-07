
import sys 


## table header format 

# | English | American World | English |


file = open(sys.argv[1], "r", encoding="utf-8")
lines = file.readlines()
file.close()


Table_Header_Index = 3 

while Table_Header_Index < len(lines):
    if not lines[Table_Header_Index].startswith("|"):
        Table_Header_Index += 1
        continue
    else:
        break

English_Index = -1
American_Index = -1
British_Index = -1




table_header = [ x.strip() for x in lines[Table_Header_Index].split("|") ]
print("table header: ", table_header)

for index in range(len(table_header)):
    if table_header[index] == "English":
        English_Index = index
        # 假设表格头中只有一个 English 并且发音在后面
        for index in range(English_Index + 1, len(table_header)):
            if table_header[index] == "美式发音示例":
                American_Index = index
            elif table_header[index] == "英式发音示例":
                British_Index = index
        break

print("English index: ", English_Index)
print("American index: ", American_Index)
print("British index: ", British_Index)

assert English_Index != -1, "table header must have English"
assert American_Index | British_Index != -1, "table header must have American or British"


# 好了可以开始各种解析了不是吗





# def FindEnglish(table_header):
#     for index in range(len(table_header)):
#         if table_header[index] == "English":
#             return index
#     return -1

# print("English index: ", FindEnglish(table_header))


# def tableCheck():