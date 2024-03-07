
## Manjora是基于arch的发行版 

或者你可以说manjora是arch的下游,这样的结果就是manjora的包通常比arch要慢. 
好了,这里就容易出项bug了
## Source 


## Application 


1. Pacman 
2. git 
3. source 



## Configuation



## kvm 

```bash

sudo pacman -Syy
sudo pacman -S archlinux-keyring
sudo pacman -S qemu virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat dmidecode

sudo pacman -S ebtables iptables
sudo pacman -S libguestfs

```




## 说一个我认为很呆的点, 就是 
root用户有自己的配置文件路径