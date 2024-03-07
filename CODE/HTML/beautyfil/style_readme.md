
所以这里其实是一个使用文档,是吗? 
## 1.目的 

让你可以在笔记本里开开心心地写css. 无论是用于展示还是学习. 


## 2.可行性解释 

obsidian的文本替换. 

## 3.使用明细 


文档应该分为就是开发文档和使用文档,前者面向开发人员重点解释代码的工作原理和执行流程,后者面向用户. 


## style 开发文档 

### 代码执行流 

>[!done]- 代码格式要求 

我们先默认其是没有空格的. 
其次


`````col
````col-md
flexGrow=1
===
```css
.flex{
    display:flex;
}
.item{
    width:30px;
    height:30px;
    background-color:blue;
    margin:5px; 
}
```
````
````col-md
flexGrow=1
===
<div  class="flex box" style="display:flex;" >
    <div class="item" style="width:30px;height:30px;background-color:blue;margin:5px;" ></div>
    <div class="item" style="width:30px;height:30px;background-color:blue;margin:5px;"> </div>
    <div class="item" style="width:30px;height:30px;background-color:blue;margin:5px;"> </div>
</div>
````
`````

### 先实现功能 然后给出解释 

