import sys

file = open(sys.argv[1],"a+",encoding="utf-8")
file.write("hello world \n")
file.close()
