---
file-created: 2023 12 01
last-modified: 2023 12 01
---

> [!faq] dynamic create a function 

[[Lazy evaluation]] : I want to create a function which will simplified after some environment check. For example , if current OS is linux , will use bash instead of cmd. Because of simplified , the function will become more effective. 

By the way , this idea could implement by many method . if platform problem , you could use [[conditional compilation]]

```c
void Win(){
  printf("Windows\n");
}

void Linux(){
  printf("Linux\n");
}

// 返回一个函数指针
void (*getOS())(){
  printf("getOS called\n");
  int a = 1;
  if(a == 1){
    return Win;
  }else{
    return Linux;
  }
}

int main(){
  void (*os)() = getOS();
  os();
  os();
  return 0;
}
```


>[!transfer] different anonymous function 
>python java lambda
>js arrow function 
>go function 