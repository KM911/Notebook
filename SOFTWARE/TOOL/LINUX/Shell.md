---
file-created: 2023 11 23
last-modified: 2023 12 05
---

## Hello World

```bash
x="hello world"
echo $x
```
## Variable 

```bash
var=value
echo $var
array=(1 2 3 5)
echo ${array[1]}
```

>[!warning] 注意
>1.声明变量不能有空格 ✔️`var=1` ❌ `var = 1`
>2.弱类型 `str="1"` `int=1` 两者相等.  

>[!tip] 我曾经认为shell中使用变量需要$是非常愚蠢的设计
>后来发现,这样的设计,格式化字符串时非常方便. 
>>[!example]-  format print
>```bash
>username=km911
>passwd=xxdd
>echo "hello $username your passwd is $passwd"
>```

## Operator

>[!example] Unary Arithmetic 	
`````col
````col-md
flexGrow=1
===
```bash
int=1
((int++))
echo $int
```
````
````col-md
flexGrow=1
===
```bash
int=1
((int+=100))
echo $int
```
````
`````
>[!example] Binary Arithmetic	

`````col
````col-md
flexGrow=1
===
```bash
int=1
value=10
int=$((int +value))
echo $int
```
````
````col-md
flexGrow=1
===
```bash
int=10
divide=3
int=$((int/divide))
echo $int
```
````
`````
>[!example] Relational


>[!warning] 字符串操作符和数字的操作符不太一样

````col
```col-md
flexGrow=1
===
| Relation | Operator |
| ---- | ---- |
| -eq | == |
| -nq | != |
| -gt | > |
| -lt | < |
| -gq | >= |
| -lq | <= |
```
```col-md
flexGrow=1
===
| Relation | Operator |
| ---- | ---- |
| contain | =~ |
| HasPrefix | == $value* |
| HasSuffer | == *$value |
| connect | ="$v1 $v2" |
```
````

## condition

>[!v] 我不太理解这里的`[]` 和`()` 它们具体做了什么我是不知道的,这样太难受了.

### test

```bash
if test -e obsidian.exe ;then
echo "obsidian.exe exit"
fi
```

| flag   | function           |
| ------ | ------------------ |
| -e 文件名 | 如果文件存在则为真          |
| -r 文件名 | 如果文件存在且可读则为真       |
| -w 文件名 | 如果文件存在且可写则为真       |
| -x 文件名 | 如果文件存在且可执行则为真      |
| -s 文件名 | 如果文件存在且至少有一个字符则为真  |
| -d 文件名 | 如果文件存在且为目录则为真      |
| -f 文件名 | 如果文件存在且为普通文件则为真    |
| -c 文件名 | 如果文件存在且为字符型特殊文件则为真 |
| -b 文件名 | 如果文件存在且为块特殊文件则为真   |

`````col
````col-md
flexGrow=1
===
```bash
a=10
b=5
if [[ a -gt b ]];then
  echo "a is greater than b"
elif [[ a -lt b ]];then 
  echo "b is less than a"
else
  echo "a is equal to b"
fi

if [[ a%2 -eq 0 ]];then
echo a is even
fi
```
````
````col-md
flexGrow=1
===
```bash
h="hello"
w="word"
wl="world"
hw="hello world"
if [[ $hw =~ $h ]];then
echo "hw contain h"
fi

if [[ $hw == $h* ]];then
echo "hw has prefix h"
fi

if [[ $hw != *$w ]];then
echo "hw not has suffer w"
fi
```
````
`````

## loop

`````col
````col-md
flexGrow=1
===
```bash
for (( i=0; i<4; i++ ));do 
    echo $i
done

```
````
````col-md
flexGrow=1
===
```bash
for i in {1..5};do
echo "i = $i"
done
```
````
`````

## array

| `@` `*` | all element |
| ------- | ----------- |
| `!`     | index array |
| `#`     | length      |
`````col
````col-md
flexGrow=1
===
```bash
array=(1 2 4 199)
echo "array index ${!array[@]}"
```
````
````col-md
flexGrow=1
===
```bash
array=(1 2 4 199)
echo "array length ${#array[@]}"
```
````
`````
`````col
````col-md
flexGrow=1
===
```bash
array=(1 2 4 199)
echo "array all element ${array[@]}"
```
````
````col-md
flexGrow=1
===
```bash
array=(1 2 4 199)
echo "array all element ${array[*]}"
```
````
`````

### traverse an array

`````col
````col-md
flexGrow=1
===
```bash
array=(1 2 4 5 6)
for i in ${array[@]}
do
    echo $i
done
```
````
````col-md
flexGrow=1
===
```bash
array=(1 2 4 5 6)
for i in ${!array[@]}
do
    echo ${array[$i]}
done
```
````
````col-md
flexGrow=1
===
```bash
array=(1 100 99)
for((i=0;i<${#array[@]};i++))
do
    echo ${array[i]}
done
```
````
`````

### string convent array

auto convent or manual convent
`````col
````col-md
flexGrow=1
===
```bash
str="hello world"
array=($str)
echo ${array[1]}
```
````
````col-md
flexGrow=1
===
```bash
str="hello,world"
array=(${str//,/ })
echo ${array[1]}
```
````
`````

### array convent string

`````col
````col-md
flexGrow=1
===
```bash
array=(1 2 4 5 6)
echo ${array[@]}
```
````
````col-md
flexGrow=1
===
```bash

```
````
`````


## function 

说实话 不好用的函数 


### argv 

`````col
````col-md
flexGrow=1
===
```bash
echo "filename is $0"
```
````
````col-md
flexGrow=1
===
```bash
echo "argv is $@"
echo "argc is $#"
```
````
`````

### environment variable

`````col
````col-md
flexGrow=1
===
```bash
echo $PWD
```
````
````col-md
flexGrow=1
===
```bash
echo $USER
```
````
`````

## Example

>[!example] Rust Tool Box
>```bash
>
>```

 
>[!example]- 获取文件夹下的全部文件和子文件夹
>```bash
>for file in $(ls);do
>    echo $file
>done
>```

