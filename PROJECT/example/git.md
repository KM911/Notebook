---
file-created: 2023 11 04
last-modified: 2023 11 28
---

>[!error] .gitignore为什么失效 
>我们应该最先添加 `.gitignore`文件,因为`.gitignore`是无法忽略已经被添加的文件.


>[!note] 项目结构
├── .gitignore
└── LICENSE

>[!faq]- 如何快速生成项目结构
>利用tree生成的项目结构,这里是nushell生成的所以非常平滑. 


其中 `.gitignore` 

```.gitignore
# idea 
.idea
.vscode

# build 
*.bin
*.exe
*.class
*.o
*.out
*.so

#image
*.png
*.jpg
*.jpeg
*.gif
*.webp


/node_modules/
/dist/
/out/
/target/
/build/

```


