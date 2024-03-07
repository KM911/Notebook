

[css定位 保姆级动画详解 完全掌握position\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV15c411p7Rk/?spm_id_from=333.337.search-card.all.click&vd_source=036ef261e6800ac6f6a743a8d5dce899)


position 和 movement 

position : static(default) relative fixed absolute sticky 
movement : top , bottom , right , left . 

## static 

static can not "move" , so use any movement is useless.

## relative 

relative to static and start move. 

so top 40px will 向下移动40px


## fixed 

relative to window/body and start move. 

如果没有使用任何的movement呢? 
这里的位置其实就是相对于全局的自动居中了不是吗? 不是的,其实是因为受到了 display的影响了,才会居中,就有点免费了


>[!exp] 想要在右下角添加一个沟通标签,应该使用
>```css
>div{
>    position : fixed; 
>    right : 40px
>    bottom : 40px;
>}
>```

## sticky 


## absolute 

相对于直接father,如果father的 position是static就继续向上找. 

如果不移动相当 == static .



都脱离了文档流