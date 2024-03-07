
[【Code Review】十行循环变两行？argparse注意事项？不易察觉的异常处理？\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Ab4y1j7KL/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=036ef261e6800ac6f6a743a8d5dce899)


1.flag argumeng 是否是必须 , 是否可以为空? 
2.语法约束和逻辑约束
3.source managment

如果进行了诸如打开文件的操作,一定要考虑,是否可能出现意外,导致文件没有被关闭,虽然如果程序退出后,会释放之前没有关闭的程序. 

go panic了 defer还会执行吗? 会执行,所以可以利用defer
但是如果使用了os.exit就不可以了,直接将程序kill了
