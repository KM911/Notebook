---
file-created: 2023 11 25
last-modified: 2023 11 30
---



>[!note] Name From. 
The name "Matplotlib" is a combination of "Matlab" and "plot"


```python
import matplotlib.pyplot as plt
```

这里我选择给出足够多的API,然后供你去查看, 你的水平其实已经到了可以查看API文档了不是吗? 


## example

>[!note] Nothing Could Be Better than Guide Example  [Examples — Matplotlib 3.8.2 documentation](https://matplotlib.org/stable/gallery/index.html) 



line  pie bar scatter  histogram  box 

### line

````col
```col-md
flexGrow=1
===
>[!example] y = x + 3
>```python
>x = [i for i in range(-10,11)]
y = [i*i for i in x]
plt.plot(x, y)
plt.show()
>```
```
```col-md
flexGrow=1
===
![[Pasted image 20231125184946.png]]
```
````



````col
```col-md
flexGrow=1
===
>[!example] y = x + 3
>```python
>x = [i for i in range(-3,4)]
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
>
```
```col-md
flexGrow=1
===
![[Pasted image 20231125185651.png]]
```
````





### Pie

>[!note] Core Value
>1.Labels 
>2.Size

````col
```col-md
flexGrow=1
===
>[!example] 
>```python
>labels = [ 'Python', 'C++', 'Ruby', 'Java']
sizes = [215, 130, 245, 210]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.show()
>```
```
```col-md
flexGrow=1
===
![[Pasted image 20231125185140.png]]
```
````

### Bar


````col
```col-md
flexGrow=1
===
>[!example] 
>```python
>x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,5,7,6,8,9,11,12,12]
plt.bar(x,y)
plt.show()
>```
```
```col-md
flexGrow=1
===
![[Pasted image 20231125185310.png]]
```
````


### scatter 

````col
```col-md
flexGrow=1
===
>[!example] 
>```python
>x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,5,7,6,8,9,11,12,12]
plt.scatter(x,y)
plt.show()
>```



```
```col-md
flexGrow=1
===
![[Pasted image 20231125185804.png]]
```
````

### histogram

>[!note] histogram will count every value times and show . 


````col
```col-md
flexGrow=1
===
>[!example]
>```python
>x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,5,7,6,8,9,11,12,12]
plt.hist(y, bins=5)
plt.show()
>```

```
```col-md
flexGrow=1
===
![[Pasted image 20231125185909.png]]
```
````

### box


````col
```col-md
flexGrow=1
===
>[!example]
>```python
>values = [[i for i in range(1,11)], [i for i in range(11,21)], [1,2,3,4,5,39,40,41,42,0]]
plt.boxplot(values)
plt.show()
>```

```
```col-md
flexGrow=1
===
![[Pasted image 20231125190216.png]]
```
````
## Configuration 

>[!note] you may want to add some info for grame just 

title , axiso yaxiso
## Layout

>[!note] Background
>In certain situations, it may be desirable to combine multiple plots into a single image. To achieve this, familiarity with the fundamental layout principles of Matplotlib is essential.