---
file-created: 2023 12 05
last-modified: 2023 12 05
---

## Linux 提示符

核心是 $PS1 修改其值. 

没有什么意义的内容. 

| expression | mean     |
| ---------- | -------- |
| `\u`       | username |
| `\h`       | host     |
| `\w`       | pwd         |

```bash
export PS1="\u\h:\w"
```

