
[【Code Review】传参的时候有这么多细节要考虑？冗余循环变量你也写过么？\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1gh4y1y7Rv/?spm_id_from=333.788&vd_source=036ef261e6800ac6f6a743a8d5dce899)

1: flag parser , 对于枚举类型,应该是 choice 而不是 string 
2: 进行显示传参 而不是利用可变参数, 特别是当你的参数格式是固定时
3: 报错信息应该和输入保持一致
4: 循环变量的冗余