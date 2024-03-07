import sys
import os


import lib.files as files
import lib.std as std
import lib.table as table


sys.stdout.reconfigure(encoding='utf-8')


#TODO : print output redirect to obsidian cursor position 
print(table.BuildTable(table.ConventClipIntoTable()))
