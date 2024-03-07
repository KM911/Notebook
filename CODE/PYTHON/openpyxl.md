---
file-created: Thursday, November ,2023
last-modified: Saturday, November ,2023
---



## 数据持久化

老师肯定考excel相关的操作. 

我们记录一下如何操作就好了. 

```python
# createe workbook 
workbook = openpyxl.Workbook()
# sheet chose
sheet = workbook["sheetname"]


```




```python
# 读写功能实现
### append data
1. append 
```python
sheet.append([list...])

sheet["A"][i].value 

workbook.save(filenme)
```

```