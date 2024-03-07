
## transform

不会影响其他的元素布局,这里是非常重要的. 



```css
div{
    width : 100px;
    height : 100px ; 
    color : aqua;
}
```

### translate

虚化的背景用于表示原始元素的位置.

`````col
````col-md
flexGrow=1
===
```css
div{
 transform : translate(40px);
}

```
````
````col-md
flexGrow=1
===
<div style="transform : translate(40px);width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
<div style="position:absolute;top : 16px; opacity:0.4; width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
````
`````

### rotate

`````col
````col-md
flexGrow=1
===
```css
div{
 transform : rotate(45deg);
}

```
````
````col-md
flexGrow=1
===
<div style="transform: rotate(45deg);width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
<div style="position:absolute;top : 16px; opacity:0.3; width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
````
`````

#### transform-origin




### scale

`````col
````col-md
flexGrow=1
===
```css
div{
 transform : scale(0.5);
}

```
````
````col-md
flexGrow=1
===
<div style="transform: scale(0.5);width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
<div style="position:absolute;top : 16px; opacity:0.4; width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
````
`````




### skew 


`````col
````col-md
flexGrow=1
===
```css
div{
 transform : skew(30deg);
}

```
````
````col-md
flexGrow=1
===
<div style="transform: skew(30deg);width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
<div style="position:absolute;top : 16px; opacity:0.4; width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
````
`````



### matrix


