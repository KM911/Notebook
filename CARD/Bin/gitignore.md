---
file-created: 2023 11 15
last-modified: 2023 11 26
---

> [!faq] Exclude Files
> In our git repo, it may contain some log build cache. we do not want to add them into our git repo , so .gitignore come out. 
> 
> >[!note] Our Git repository might contain build log caches, which we don't want to include in the repository. This is where the .gitignore file comes into play
> 

>[!note]- Usage 
> Within the root directory of your Git repository, create a file named .gitignore and add the desired patterns to exclude specific files or directories from Git tracking.


>[!example] A C project 
>It may contain `.log` `.o` and `build` folder , we want to exclude them. 
>```.gitignore
>*.log
>*.o
>build
>```


## Match rules patterns 

>[!note]  Let's delve into the outcome of the provided example and gain a deeper understanding of the .gitignore file's pattern matching rules.

### file extension match 

>[!note] `*.ext` this will exclude / ignore any file with same extension . It is easy to understand . 

### whole name match

>[!note] `build` will match any file or directory named log, regardless of where it is located in the repository. This includes folders and their containers.


>[!tip] Just enough 
>In fact , only use above patterns could solve most problem , it enough for a beginner


### "absolute" path match

ignore file or directory with absolute path match
```.gitignore
path1/path2 
/path1/path2
```


>[!tip] Summary Pattern 
> 1. Extension match
> 2. Name match
> 3. Path match


