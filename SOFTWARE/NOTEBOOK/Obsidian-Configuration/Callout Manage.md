---
file-created: 2023 11 30
last-modified: 2023 11 30
---


## Why Callout ?

[[Obsidian Zen#Callout]]


>[!note] Obsidian 本身就有部分Callout 样式

## callout 使用 

| callout | tag |
| ---- | ---- |
| cite quoto | 引用 |
| example exp | 举例子 |
| faq help | 提问 引出背景 |
| missing error danger bug | 错误理解 事实 |
| tip abstract | 总结 汇总 |
| todo note desc | 介绍性文字 |
| transfer | 类比 迁移 |
| v verify | 不确定,带验证 |
| warning | 警告 |
| others | 其他不重要 |

````col
```col-md
flexGrow=1
===
>[!warning]
```
```col-md
flexGrow=1
===
>[!missing]
```
```col-md
flexGrow=1
===
>[!danger]
```
```col-md
flexGrow=1
===
>[!quote]
```
````

````col
```col-md
flexGrow=1
===
>[!transfer]
```
```col-md
flexGrow=1
===
>[!todo]
```
```col-md
flexGrow=1
===
>[!note]
```
```col-md
flexGrow=1
===
>[!example]
```
````

````col
```col-md
flexGrow=1
===
>[!tip]
```
```col-md
flexGrow=1
===
>[!done]
```
```col-md
flexGrow=1
===
>[!faq]
```
```col-md
flexGrow=1
===
>[!abstract]
```
````

````col
```col-md
flexGrow=1
===
>[!bug]
```
```col-md
flexGrow=1
===
>[!error]
```
```col-md
flexGrow=1
===
>[!others]
```
```col-md
flexGrow=1
===
>[!cite]
```
````


> [!help] Can callouts be nested?
> > [!todo] Yes!, they can.
> > > [!example]  You can even use multiple layers of nesting.

if you want to collapse it , add - 

> [!faq]- Are callouts foldable?
> Yes! In a foldable callout, the contents are hidden when the callout is collapsed.

自定义样式
Callouts的类型和图标是用CSS来描述，颜色是r, g, b 三色组，图标有相应的 icon ID (比如lucide-info)。也可以自定义SVG图标。

```css
.callout[data-callout="my-callout-type"] {
    --callout-color: 0, 0, 0;
    --callout-icon: icon-id;
    --callout-icon: '<svg>...custom svg...</svg>';
}
```




