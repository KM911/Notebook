---
file-created: Wednesday, November ,2023
last-modified: Saturday, November ,2023
---

>[!tip] 好处
>充分利用每一个代理节点的网络资源,提升网络效率,特别是当单一节点网络资源紧张的时候. 

 
 >[!warning] 缺点
>部分站点会记录你的IP,因为负载均衡导致你的IP频发变动,可能触发安全机制. 



## 实现

>[!note] 利用CFW 的parser功能. 
>在 settings --> profile --> parsers  将下面的内容复制
>
> ```yaml
> parsers:
>   - reg: 'load_balance$'
>     yaml:
>       append-proxy-groups:
>         - name: ⚖️ 负载均衡-散列
>           type: load-balance
>           url: 'http://www.google.com/generate_204'
>           interval: 300
>           strategy: consistent-hashing
>         - name: ⚖️ 负载均衡-轮询
>           type: load-balance
>           url: 'http://www.google.com/generate_204'
>           interval: 300
>           strategy: round-robin
>       commands:
>         - proxy-groups.⚖️ 负载均衡-散列.proxies=[]proxyNames
>         - proxy-groups.0.proxies.0+⚖️ 负载均衡-散列
>         - proxy-groups.⚖️ 负载均衡-轮询.proxies=[]proxyNames
>         - proxy-groups.0.proxies.0+⚖️ 负载均衡-轮询
> ```
> 
> 2. 修改订阅链接  
> 
> profiles --> settings --> url  在订阅链接的URL后面添加上 `#load_balance` 然后更新
> 
> 
> 如果成功了就可以在策略组中看见负载均衡的策略了.
> 


```c
int main(){
printf("hello world");
}
```

