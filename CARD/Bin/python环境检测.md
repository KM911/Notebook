
>[!faq] 在给其他人分享你的代码时,对方如果缺少环境该如何解决

>[!tip] 有一种可能用户没有安装某个库,为了提高兼容性,在库缺失时自动安装 
## python 环境检查

```python
# 内置库
import os
import os.path
import time
import sys

# 第三方库 可能用户环境缺失 通过try except来检测
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import openpyxl
    import requests
    import rich
    from rich.tree import Tree
    rich.print("环境检测[bold green]通过[/bold green]")
except:
    print("环境缺失,正在安装环境...")
    os.system("pip install rich requests openpyxl selenium")
    # 重新导入
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import openpyxl
    import requests
    import rich
    from rich.tree import Tree
    # 可以 cls 和 clear进行清除 , 不过需要注意系统兼容性
    os.system("cls")

```

