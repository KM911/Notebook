
## transition 

>[!note] Syntax 
> ```css
> transition : property duration timing-function delay;
> ```


| property | avavl value |
| ---- | ---- |
| property |  |
| duration |  |
| timing-function |  |
| dealy  |  |


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
<div class="trans" style="width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>

````
`````

## timing function 

```css
div{
    animation: trans200px 2s ease infinite;
}
@keyframes trans200px{
  0%{
    transform: translate(0px);
  }
  50%{
    transform: translate(200px);
  }
  100%{
    transform: translate(0px);    
  }
}

```

`````col
````col-md
flexGrow=1
===
```css
div{
    animation: trans200px 2s ease infinite;
}

```
````
````col-md
flexGrow=1
===

<div class="ease" style="width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
````
`````

`````col
````col-md
flexGrow=1
===
```css
div{
    animation: trans200px 2s ease-in infinite;
}

```
````
````col-md
flexGrow=1
===
<div class="ease-in" style="width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
````
`````


`````col
````col-md
flexGrow=1
===
```css
div{
    animation: trans200px 2s ease-out infinite;
}

```
````
````col-md
flexGrow=1
===
<div class="ease-out" style="width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
````
`````


`````col
````col-md
flexGrow=1
===
```css
div{
    animation: trans200px 2s ease-in-out infinite;
}

```
````
````col-md
flexGrow=1
===
<div class="ease-in-out" style="width: 100px;height: 100px; background-color: aqua; border-radius: 25px;"></div>
````
`````


