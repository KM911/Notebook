

>[!example] example
>
>```go
>
>```




```go
	cmd := exec.Command("cmd", "/C", "mkdir sapkin && cd  sapkin && mkdir test && dir && rmdir test")
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	// 设置工作目录
	// cmd.Dir = $PWD
	cmd.Dir = util.TempDirectory
	// 设置
	// cmd.Dir = $ENV
	cmd.Env = []string{}
	// 我们现在可以做了什么了呢?
	// 但是我们不可以能像chroot一样修改其环境对吧,但是我们可以进行检测,就是你执行的操作中,应该是必须以 Dir开头的,如果不是,我们将其视为错误.
	// 或者你都使用相对路径
	cmd.Run()
	os.Remove(filepath.Join(util.TempDirectory, "sapkin"))
```
