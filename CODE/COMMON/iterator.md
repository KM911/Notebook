
## 如何遍历一个数组? 

C语言中可以这样去写

```c
int a[10];
for (int i=0;i<10;i++){
    a[i] = 0;
}
```
如何去遍历一个链表? 
```c
PNode p;
while(p){
    printf("%c",*p);
    p = p->next;
}
```

这样非常麻烦,因为我们会发现我们需要编写不同代码针对不同的结构体. 是否可以找到一个通用的方法取获取一个对象/结构体全部的内容呢? 

```python
for i in Obj:
    pass
```
### python中的迭代器 

__iter__() 方法, 如果存在就是一个可迭代对象, 需要返回一个存在 __next__ 方法的对象, 
next() 方法 执行真正的 "迭代操作"

## 实现一个简单的python range 

我们常用range来实现执行n次的操作. 

```python
for i in rnage(10):
    pass
```

你可以实现一个类似的

```python
class MyRange:
  def __init__(self, n):
    self.n = -1
    self.Max = n-1
  def __iter__(self):
    return self
  def __next__(self):
    if self.n != self.Max:
      self.n += 1
      return self.n
    else:
      raise StopIteration
```

### 区分可迭代对象和迭代器 

如果一个对象同时实现了__iter__方法和__next__方法，它就是迭代器。
如果一个对象实现了__iter__方法，那么这个对象就是可迭代对象。

我不喜欢这个说法,因为
但是这个说法问题在于,如果一个对象只有 __next__方法呢? 

比如list就是只有__iter__方法,因为其会返回一个持有__next__方法的对象. 

会看我们的for循环. 

for循环这里执行的内容其实是

首先调用MyRange的iter方法返回一个，然后调用一直next方法,直到抛出StopIteration异常退出无限循环


### Java的迭代器

我们可以看到java的实现其实就有些不同了,

```java
  ArrayList<String> list = new ArrayList<String>();  
        list.add("Apple");  
        list.add("Banana");  
        list.add("Orange");  
        list.add("Grape");  
  
        Iterator<String> iterator = list.iterator();  
  
        while (iterator.hasNext()) {  
            String fruit = iterator.next();  
            System.out.println(fruit);  
        }  
```


## 生成器 

```python
generator
```

我的天哪,这个东西其实不是很好理解.

generator function , return value is a generator, 

生成器对象有一个__iter__方法和一个__next__方法。当你第一次获取生成器对象的值时，它将会执行函数直到遇到yield语句，然后它将记住停止的位置。当你再次请求值时，它将从停止的位置开始执行，直到再次遇到yield语句。