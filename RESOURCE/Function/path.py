import os 

import sys



os.system("echo %s | clip" % sys.argv[1].replace("\\", "/"))
