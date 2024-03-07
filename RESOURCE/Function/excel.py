import sys
import os


import lib.files as files
import lib.std as std
import lib.table as table



sys.stdout.reconfigure(encoding='utf-8')

print(table.BuildTable(table.ConventClipIntoTable()))
