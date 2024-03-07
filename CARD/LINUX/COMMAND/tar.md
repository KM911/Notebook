
>[!note] tape archive
>compress and decompress 


| flag | function |
| ---- | ---- |
| f | output file name |
| c | compress |
| z | gzip |
| x | decompress |
| v | verbose : show detail |
|  |  |
|  |  |

>[!example] compress
>compress a file or folder
>```bash
>echo "hello " >> temp.txt
>tar -cvf out.tar.gz temp.txt
>```


>[!example]   decompress
>```bash
>tar -xvf out.tar.gz 
>```



>[!v] 压缩算法
>看上去好像tar可以使用多种压缩算法, `z` gzip `j`bz2 , 会有什么影响呢?后续有机会去看看. 

## 解压缩 

| 压缩文件 | 解压命令       | 压缩命令                                 |
| -------- | -------------- | ---------------------------------------- |
| `.tar.gz`  | tar -xf "file.tar.gz" | tar -czvf "archive.tar.gz"  file1  |
| `.zip`   | unzip "file.zip"   |          zip -9 archive.zip file1                                |
| `.rar`   | unrar e "file.rar" |      rar a archive.rar file1 file2                                    |
|      `.gz`     |  gzip -d file.gz               |  gzip -9 file1                                          |
