import sys
import os


import lib.files as files
import lib.std as std
import lib.table as table


# Environment Check
assert len(sys.argv) == 2, "must have one argument"
assert sys.argv[1][-3:] == ".md", "must be a markdown file"

# allowed_filenames = ["pronounce.md"]



# function implementation

contents = files.ReadFileContent(sys.argv[1]) 

# 手动迭代contents不就好了吗 有道理 但是我想用函数式编程

def Iterator(contents :list): 
    index = 0 
    def iteration(type :str ="value" ):
        nonlocal index
      
        if type != "value":
          if index >= len(contents):
            raise StopIteration
          index += 1
        return contents[index]
    
    return iteration




# `````col
# ````col-md
# flexGrow=1
# ===
# ```css
# div{
#     border-radius : 25px;
# }

# ```
# ````
# ````col-md
# flexGrow=1
# ===
# <div style="color:red;width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
# ````
# `````


# TODO 
# contents.append(table.BuildTable([["RGB","Example"],["data1","data2"],["data3","data4"]]))


# files.SaveFileContent(contents)