

| 问题                      | 原因分析                                        | 解决方案                       |
| ----------------------- | ------------------------------------------- | -------------------------- |
| 只有sudo docker run 才可以执行 | docker相关的文件例如 /var/run/docker.sock所属用户为root | sudo chown -hR $user files |
| go build 无法执行           | go build 会携带版本信息                            | go build --builcvs=false   |
|                         |                                             |                            |
|                         |                                             |                            |

