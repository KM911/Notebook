import sys


assert len(sys.argv) == 2, "must have one argument"


for i in range(len(sys.argv)):
    print("argv[", i, "] = ", sys.argv[i])
