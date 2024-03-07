````col
```col-md
flexGrow=1
===
> [!note] 定义
> 浮点数计算单元 


> [!tip] 相关概念
>  [[x86_64寄存器数量]]
```
```col-md
flexGrow=1
===
> [!info] 别称
>  floating-point unit 

> [!cite]- 参考资料
> <% tp.file.cursor() %>
```
````


目前看来,我们可以简单地理解为我们的CPU集成了FPU, 体现在我的CPU有下面这些寄存器. 

st   8  浮点寄存器 FPU 80bit 为什么位宽是80bit呢? 
fxxx 8 浮点数控制寄存器

媒体寄存器应该不算浮点数基础器,因为这里其实不能帮助我们进行浮点数计算吗? 
mmx  16 128位媒体寄存器 
