
````col
```col-md
flexGrow=1
===
> [!note] 定义
> 一种提高CPU执行效率的技术

> [!tip] 相关概念
> [[指令重排]] [[CPU执行过程]]
```
```col-md
flexGrow=1
===
> [!info] 别称
> CPU管线化

> [!cite]- 参考资料
> [【CSAPP-深入理解计算机系统】4-5. 流水线的通用原理\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Tp4y187dj/?spm_id_from=333.337.search-card.all.click)
> [【计组】CPU流水线及冒险\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV18k4y1p7dA/?spm_id_from=333.337.search-card.all.click)
```
````

```mermaid
flowchart LR
    A["取指(IF)"] --> B["译码(ID)"]
    B --> C["执行(EX)"]
    C --> D["访存(MEM)"]
    D --> E["写回(WB)"]
```

每一个指令的执行都需要经过上面的5个流程,并且上的每一步只依赖前一步的结果. 

实际上的内容要复杂得多. 
![[Pasted image 20231024153447.webp]]

每一个阶段需要不同的硬件执行

CPU的指令有三个参数 

指令码 + 数据码 + 地址

5级流水线

| 1    | 2    | 3    | 4     | 5     | 6     | 7     | 8    |
| ---- | ---- | ---- | ----- | ----- | ----- | ----- | ---- |
| IF_1 | ID_1 | EX_1 | MEM_1 | WB_1  |       |       |      |
|      | IF_2 | ID_2 | EX_2  | MEM_2 | WB_2  |       |      |
|      |      | IF_3 | ID_3  | EX_3  | MEM_3 | WB_3  |      |
|      |      |      | IF_4  | ID_4  | EX_4  | MEM_4 | WB_4 |

在时钟周期4和5里,4条指令同时执行,这样的效率就要高的多. 

理论上,流水线的级数越多,就可以支持更多的指令并行. 但是实际并非如此. 
