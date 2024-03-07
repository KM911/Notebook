---
file-created: Thursday, November ,2023
last-modified: Saturday, November ,2023
---

## cheat sheet

| syntactic  |implementation method               |
| ----- | -------------------- |
| len   | `__len__`            |
| with  | `__enter` `__exit__` |
| next  | `__next__`           |
| range | `__iter__`           |
|       |                      |
## len (obj)

实现了 `__len__方法` 

```python
class MyClass:
  def __len__(self):
    return 1000
my = MyClass()
print(hasattr(my, '__len__'))
print(len(my))
```


## with 

实现了 `__enter__` 和 `__exit__` 方法, 分别会在开始和结束调用两者. 其中`__enter__`方法如果需要应该返回一个对象. 
```python
class MyClass:
  def Hello(self):
    print('Hello')
  def __enter__(self):
    print('enter')
    return self
  def __exit__(self, exc_type, exc_value, traceback):
    print('exit')
my = MyClass()
with my as m:
  m.Hello()
  print('world')
```


## range(?)

或许应该叫迭代器,其中迭代器
```python
class MyRange:
  def __init__(self,max) -> None:
    self.n = 0
    self.max =max
  def __iter__(self):
    return self
  def __next__(self):
    if self.n < self.max:
      value = self.n
      self.n += 1
      return value
    else:
      raise StopIteration
myrange = MyRange(3)
for i in myrange:
  print(i)
```

这里的for循环其实是这样的
```python
myrange = MyRange(3)
while True:
    try:
      print(next(myrange))
    except StopIteration:
      break
```


## reflection 

[[Reflection]]

> [!abstract]- 支持的功能
> 1. 类型检查,通过`isinstance`判断一个对象所属的类型. 
> 2. 属性检查 `hasattr`  
> 3. 获取/设置attribute `setattr` `getattr`
> 4. 移除 `delattr`

我们无法直接获取有多少对象和元素,


> [!error] python的 attribute 这里既可以是 field 也可以是 method ??? 

没有意义的问题, 比如 `int` 几个字节,且不说在C语言中 `int`是几个字节也是无法直接确定的,机器是16bit还是32/64?, 在python中, 这个值可以无限大. 


## private 

python中没有`private`关键字, 但是不代表它没有这个内容. 

`convention`   python中一个attribute 如果被 双下划线处理,就是一个`private`

```
Now you are a expert on computer science, please answer my question and point out my spell error or any problem.
Q : 确实我还没有找到必须使用反射的地方,即使是框架也不例外? 
```

我们可以为所有的private attribute provide a public method ? 有任何意义吗? 你告诉我

## Operate 

*  + - * / 
* ==  != 
