
>[!note] 初始化一个文件 

目前我觉得最好的实践是我的 `exec.go`

利用`init` 配合`Lazy envalue` , 实现了更加简洁的跨平台兼容. 


```go
package util

import (
	"os"
	"os/exec"
	"runtime"
)

var (
	CreateCommand func(command string) *exec.Cmd
)

func init() {
	if runtime.GOOS == "windows" {
		CreateCommand = createCmd
	} else {
		CreateCommand = createBash
	}
}

func createCmd(command string) *exec.Cmd {
	return exec.Command("cmd", "/C", command)
}

func createBash(command string) *exec.Cmd {
	return exec.Command("bash", "-c", command)
}

func ExecuteCommand(command string) int {
	cmdExecutor := CreateCommand(command)
	cmdExecutor.Stdout = os.Stdout
	cmdExecutor.Stdin = os.Stdin
	cmdExecutor.Stderr = os.Stderr
	cmdExecutor.Run()
	return cmdExecutor.ProcessState.ExitCode()
}

func ExecuteCommandSilent(command string) int {
	cmdExecutor := CreateCommand(command)
	cmdExecutor.Run()
	return cmdExecutor.ProcessState.ExitCode()
}

func ExecuteCommandResult(command string) string {
	cmdExecutor := CreateCommand(command)
	cmdExecutor.Stdout = os.Stdout
	cmdExecutor.Stdin = os.Stdin
	cmdExecutor.Stderr = os.Stderr
	cmdExecutor.Run()
	return cmdExecutor.ProcessState.String()
}

```


