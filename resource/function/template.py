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
sys.stdout.reconfigure(encoding='utf-8')


contents = files.ReadFileContent(sys.argv[1]) 

# TODO 
contents.append(table.BuildTable([["RGB","Example"],["data1","data2"],["data3","data4"]]))


files.SaveFileContent(contents)

# 前面的预处理部分还是会执行的所以你不用担心
if __name__ == "__main__":
    print("Done")
