
>[!note] 一系列命令和动作的集合 
## define

```c
>[!info]efine N 100
```

你可以将其理解为, `file.replace("N","100")`. 

不过对于带参数的宏,就相对要复杂一些.  
## ifdef 

only check the marco wheather define even null value, and will execute the next content

```c
#ifdef DEBUG
printf(format);
#endif 
```

## if 

if for marco, check marco value . 

```c
#if DEBUG_LEVEL == 1
printf("DEBUG_LEVEL = 1\n");
#endif 
```
### Defining a constant

```c
>[!info]efine PI 3.141592653589793
int main() {
  float radius = 5.0f;
  float area = PI * radius * radius;
  printf("The area of the circle is %f\n", area);
  return 0;
}

```

### Defining a function


```c
>[!info]efine ABS(x) ((x < 0) ? -x : x)
int main(int argc, char *argv[]) {
	printf("ABS(-1) = %d\n", ABS(-1));
    return 0 ;
}
```

```c
>[!info]efine MAX(a, b) ((a) > (b) ? (a) : (b))
int main() {
  int a = 10;
  int b = 20;
  int max = MAX(a, b);
  printf("The maximum of %d and %d is %d\n", a, b, max);
  return 0;
}

```

### Condition complier 

debug code and release code 
```c
void Debug_Printf(const char *format, ...){
	#ifdef DEBUG
	printf(format);
	#endif
}
int main(){
	int a =10;
	int b ; 
	Debug_Printf("a = %d\n", a);
	Debug_Printf("b = %d\n", b);
	return 0;
}
```

```bash
gcc main.c -DDEBUG -o debug && ./debug 

a = 10
b = 16
```

Do not have any output. And a.out is small as a "empty".  
```bash
gcc main.c -o release && ./release 
```

```bash
ls -l 
```

### Built-in macros

gcc and most compiler provide some built-in macros. 

```c
int main(){
	printf("build-in macro\n");
	printf("FILE: %s\n", __FILE__);
	printf("DATE: %s\n", __DATE__);
	printf("TIME: %s\n", __TIME__);
	printf("LINE: %d\n", __LINE__);
	printf("VERSION %s\n", __VERSION__);
    return 0;
}
```

`````col
````col-md
flexGrow=1
===
```bash
build-in macro
FILE: main.c
DATE: Oct 20 2023
TIME: 14:50:10
LINE: 58
VERSION Clang 17.0.1
```
````
````col-md
flexGrow=1
===
```bash
build-in macro
FILE: main.c
DATE: Oct 20 2023
TIME: 14:49:37
LINE: 58
VERSION 10.3.0
```
````
`````


## Should I use macro ? 

Macros should be used with caution. They can make code difficult to read and maintain, and they can lead to unexpected errors. However, macros can be useful for conditional compilation.

Conditional compilation allows you to compile different parts of your program based on certain conditions, such as the target platform or the compiler version. This can be useful for developing portable code or for supporting different features on different platforms.


### Built with macro

Maybe the example is too simple , I think it had told you hot to build protable application. 
```c
int main(){
	#ifdef __WIN32__
	printf("win32 environment init \n");
	#endif

	#ifdef __linux__
	printf("linux environment init \n");
	#endif
	printf("Your application implement\n");
	return 0;
}
```




>[!note] 一系列命令和动作的集合 


