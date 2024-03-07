
>[!note] add user for linux

| flag | function |
| ---- | ---- |
| `-d` | home director |
| `-g` | set group |
| `-G` | group list |
| `-s` | default shell `/bin/bash` |
| `-p` | password |

>[!example] useradd usage
> ```bash
> sudo useradd -d /home/new_home -g root -p 123dzglks -s /bin/bash km-test
> cat /etc/passwd | grep km-test
> sudo userdel km-test
> ```



