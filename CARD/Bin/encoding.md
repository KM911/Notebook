
>[!tip] Encoding is the process of converting data from one format to another.

>[!example] 
>Translate "中文" into "Chinese" ✔️
>氧化还原反应 ❌
>儿童长成大人 ❌
>将10进制表示的8变成二进制的1000 ✔️

> [!tip]  Format Change 

>[!faq] 


[[decoding]]

>[!tip] Decoding is the process of converting encoded data into its original form.


>[!faq] 从这个角度看, "decoding" is a type of "encoding" .In most case, it only refer  the reverses process of encoding. 


>[!tip] 表述清晰
>有的时候,我们会利用编码特别指代将原始数据(人类可读的) , 转为机器可读的, 这个行为叫做编码, 相对应的 the reverse process, 将机器可读的转为人类可读的行为叫做解码.  


## 常见中文乱码问题 

| 乱码样式 | 示例 | 特点 | 产生原因 |
| ---- | ---- | ---- | ---- |
| 古文码 | 鐢辨湀瑕佸ソ濂藉涔犲ぉ澶╁悜涓? | 大都为不认识的古文，并加杂日韩文 | 以 GBK 方式读取 UTF-8 编码的中文 |
| 口字码 | ����Ҫ�¨2�ѧϰ������ | 大部分字符为小方块 | 以 UTF-8 的方式读取 GBK 编码的中文 |
| 符号码 | å¤©å¤©å�‘ä¸Š￥½å￥½å- | 大部分字符为各种符号 | 以 ISO8859-1 方式读取 UTF-8 编码的中文 |
| 拼音码 | óéÔÂòaoÃoÃÑ§Ï°ììììÏòéÏ | 大部分字符为头顶带有各种类似声调符号的字母 | 以 ISO8859-1 方式读取 GBK 编码的中文 |
| 问句码 | 好好学习天天向?? | 字符串长度为偶数时正确，长度为奇数时最后的字符变为问号 | 以 GBK 方式读取 UTF-8 编码的中文，然后又用 UTF-8 的格式再次读取 |
| 锟拷码 | 锟斤拷锟斤拷要锟矫猴拷 | 全中文字符，且大部分字符为“锟斤拷”这几个字符 | 以 UTF-8 方式读取 GBK 编码的中文，然后又用 GBK 的格式再次读取 |
| 烫烫烫 | 烫烫烫烫烫烫烫烫烫烫烫烫烫烫 | 字符显示为“烫烫烫”这几个字符 | VC Debug 模式下，栈内存未初始化 |


