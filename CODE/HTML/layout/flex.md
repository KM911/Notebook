

## flex 

[flex弹性布局 动画详解系列 css科普教程\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Rv4y177rj/?spm_id_from=333.788&vd_source=036ef261e6800ac6f6a743a8d5dce899)



| property                                   | usage                                        |
| ------------------------------------------ | -------------------------------------------- |
| [flex-direction](flex.md#flex-direction)   | row column row-reverse column-reverse        |
| [justify-content](flex.md#justify-content) | flex-start center space-between space-evenly |
| [align-items](flex.md#align-items)         | flex-start center baseline stretch           |
| flex-warp                                  | nowarp warp warp-reverse                     |
| align-content                              |                                              |

### flex-direction
>[!note] 默认排列 
>

`````col
````col-md
flexGrow=1
===
```css
.container{
    display:block;
}
.item{
    width:20px;
    height:20px;
    background-color:red;
    margin:3px; 
}
```
````
````col-md
flexGrow=1
===
<div style="" class="box flex">
    <div class="item" style="width:20px;height:20px;background-color:red;margin:3px;" ></div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin:3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin:3px;"> </div>
</div>
````
`````

>[!note] flex 默认会将元素按照x轴排列

`````col
````col-md
flexGrow=1
===
```css
.flex{
    display:flex;
}
.item{
    width:20px;
    height:20px;
    background-color:red;
    margin: 3px; 
}
```
````
````col-md
flexGrow=1
===
<div  class="flex box" style="display:flex;" >
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;" ></div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
</div>
````
`````

>[!note] 如果想要修改为按照y轴排列 
>使用 flex-direction :column;

`````col
````col-md
flexGrow=1
===
```css
.flex{
    display:flex;
      flex-direction: column;

}
.item{
    width:20px;
    height:20px;
    background-color:red;
    margin: 3px; 
}
```
````
````col-md
flexGrow=1
===
<div  class="flex box" style="display:flex;flex-direction: column;" >
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;" ></div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
</div>
````
`````

### justify-content

>[!note] align items for x axis 

>[!done] flex-start center space-between space-evenly

#### center

`````col
````col-md
flexGrow=1
===
```css
.flex{
    display:flex;
    justify-content:center;    
}
.item{
    width:20px;
    height:20px;
    background-color:red;
    margin: 3px; 
}
```
````
````col-md
flexGrow=1
===
<div  class="flex box" style="display:flex;justify-content:center;" >
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;" ></div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
</div>
````
`````
#### space-between

`````col
````col-md
flexGrow=1
===
```css
.flex{
    display:flex;
    justify-content:space-between;    
}
.item{
    width:20px;
    height:20px;
    background-color:red;
    margin: 3px; 
}
```
````
````col-md
flexGrow=1
===
<div  class="flex box" style="display:flex;justify-content:space-between;" >
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;" ></div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
</div>
````
`````

#### space-evnely

`````col
````col-md
flexGrow=1
===
```css
.flex{
    display:flex;
    justify-content:space-evenly;    
}
.item{
    width:20px;
    height:20px;
    background-color:red;
    margin: 3px; 
}
```
````
````col-md
flexGrow=1
===
<div  class="flex box" style="display:flex;justify-content:space-evenly;" >
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;" ></div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
</div>
````
`````


### align-items

perfect center , just set align-items and justify-content both center; 


#### center

`````col
````col-md
flexGrow=1
===
```css
.flex{
    display:flex;
    align-items:center;    
}
.item{
    width:20px;
    height:20px;
    background-color:red;
    margin: 3px; 
}
```
````
````col-md
flexGrow=1
===
<div  class="flex box" style="display:flex;align-items:center;" >
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;" ></div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
</div>
````
`````
#### baseline

`````col
````col-md
flexGrow=1
===
```css
.flex{
    display:flex;
    align-items:baseline;    
}
.item{
    width:20px;
    height:20px;
    background-color:red;
    margin: 3px; 
}
```
````
````col-md
flexGrow=1
===
<div  class="flex box" style="display:flex;align-items:baseline;" >
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;" ></div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
</div>
````
`````

#### stretch

`````col
````col-md
flexGrow=1
===
```css
.flex{
    display:flex;
    align-items:stretch;    
}
.item{
    width:20px;
    height:20px;
    background-color:red;
    margin: 3px; 
}
```
````
````col-md
flexGrow=1
===
<div  class="flex box" style="display:flex;align-items:stretch;" >
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;" ></div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
</div>
````
`````

### flex-warp 

>[!note] 默认是不会换行的,所以会出现挤压导致子元素的宽度异常.

`````col
````col-md
flexGrow=1
===
```css
.flex{
    display:flex;
}
.item{
    width:20px;
    height:20px;
    background-color:red;
    margin: 3px; 
}
```
````
````col-md
flexGrow=1
===
<div  class="flex box" style="display:flex;" >
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;" ></div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
</div>
````
`````

#### warp

`````col
````col-md
flexGrow=1
===
```css
.flex{
    display:flex;
    flex-warp:warp;
      align-content: space-between;

}
.item{
    width:20px;
    height:20px;
    background-color:red;
    margin: 3px; 
}
```
````
````col-md
flexGrow=1
===
<div  class="flex box" style="display:flex;flex-warp:warp;align-content: space-between;" >
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;" ></div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
    <div class="item" style="width:20px;height:20px;background-color:red;margin: 3px;"> </div>
</div>
````
`````