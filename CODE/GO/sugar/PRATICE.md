
## Table of Content
1. [[PRATICE#path.Isabs|path.IsAbs]] 
2. 


## path.Isabs


````col
如你所见 path.IsAbs 是通过 "/"来判断是否为根目录的,这在unix系统上或许正确,但是在windows上肯定就无法获取正确的结果了
```go
func IsAbs(path string) bool {
	return len(path) > 0 && path[0] == '/'
}
```
````

````col
相比之下filepath.IsAbs 就要严谨得多,会通过volumeNameLen去判断是否是根路径,
```go
func IsAbs(path string) (b bool) {
	l := volumeNameLen(path)
	if l == 0 {
		return false
	}
	// If the volume name starts with a double slash, this is an absolute path.
	if isSlash(path[0]) && isSlash(path[1]) {
		return true
	}
	path = path[l:]
	if path == "" {
		return false
	}
	return isSlash(path[0])
}
```
````

## Os.Move

