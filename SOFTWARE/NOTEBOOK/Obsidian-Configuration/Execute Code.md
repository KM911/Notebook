---
file-created: 2023 11 29
last-modified: 2023 12 01
---

>[!done] Now You could run code in your notebook 🥂

[GitHub - twibiral/obsidian-execute-code: Obsidian Plugin to execute code in a note.](https://github.com/twibiral/obsidian-execute-code)


## Support Language Test

>[!example]- C
> ```cpp
> #include <stdio.h>
> 
> int main() {
> 	printf("Hello, World!");
> 	return 0;
> }
> ```

>[!example]- CPP
>```cpp
>int main(){
>  cout << "hello world" <<endl; 
>  }
>```

>[!example]- go
> ```go
> import "fmt"
> 
> func main() {
> 	fmt.Println("Hello World")
> }
> ```

>[!example]- javascript
> ```js
> console.log("hello world")
> ```

>[!example]- Python
> ```python
> import os
> os.system("echo 'hello world'")
> ```

 
>[!example]- Java
> ```java
> public class HelloWorld {
> 	public static void main(String[] args) {
> 		System.out.println("Hello World!");
> 	}
> }
> ```


>[!example]- RUST 
> ```rust
> fn main() {
> 	println!("Hello World");
> }
> ```

>[!example]- shell
>```shell
>echo "Hello World!"
ls -la
>```

>[!example]- Powershell
>```powershell
>echo "Hello World!"
>```

>[!example]- R
>```r
> hello <- function(name){
> 	print(paste("Hello", name, sep = " "))
> }
> hello("Bob")
>```

>[!example]- Lua
>```lua
>print('Hello, World!')
>```


## Magic Value

@vault_path: Inserts the vault path as string (e.g. "/User/path/to/vault")
@vault_url: Inserts the vault url as string. (e.g. "app://local/path/to/vault")
@note_path: Inserts the vault path as string (e.g. "/User/path/to/vault/Note.md")


## Advance Usage Example

````col
```col-md
flexGrow=1
===
[[Executee Code C Support]]
```
```col-md
flexGrow=1
===
[[update word pronounce]]
```
```col-md
flexGrow=1
===
[[table_translate]]
```
```col-md
flexGrow=1
===


```
````

### Run and Preview 

```run-python
def hello(name):
    print("Hello", name)

if __name__ == "__main__":
    hello("Eve")
```


## Addition Settings

1. Clion are not support on win, so I write a adaptor for it .
2. SQL are need suport tow. 


## My Personal Enhancement

[[Executee Code C Support]]
[[Executee Code SQL Support]]