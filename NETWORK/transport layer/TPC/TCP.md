---
file-created: 2023 11 15
last-modified: 2023 11 29
---


## TCP头的详情

问题来了 这个是谁解析的 其实这里就是到网卡了吧 都需要对应的网卡了 

![](https://img-blog.csdnimg.cn/20200415235320394.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3MyNjAzODk4MjYw,size_16,color_FFFFFF,t_70)

| 字段     | 长度   | 含义                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| 源端口   | 16比特 | 源端口，标识哪个应用程序发送                                 |
| 目的端口 | 16比特 | 目的端口，标识哪个应用程序接收                               |
| 序列号   | 32比特 | 序号字段。TCP链接中传输的数据流中每个字节都编上一个序号。序号字段的值指的是本报文段所发送的数据的第一个字节的序号。 |
| 确认号   | 32比特 | 确认号，是期望收到对方的下一个报文段的数据的第1个字节的序号，即上次已成功接收到的数据字节序号加1。只有ACK标识为1，此字段有效。 |
| 首部长度 | 4比特  | 首部长度指出TCP报文段的数据起始处距离TCP报文段的起始处有多远，以32比特（4字节）为计算单位。最多有60字节的首部，若无选项字段，正常为20字节。 |
| 保留位   | 4比特  | 必须填0                                                      |
| CWR      | 1比特  | 拥塞窗口减（发送方降低它的发送速率）                         |
| ECE      | 1比特  | ECN回显（发送方收到一个更早的拥塞通告）                      |
| URG      | 1比特  | 紧急指针有效标识。它告诉系统此报文段中有紧急数据，应尽快传送（相当于高优先级的数据）。很少被使用 |
| ACK      | 1比特  | 确认序号有效标识。只有当ACK=1时确认号字段才有效。当ACK=0时，确认号无效。 |
| PSH      | 1比特  | 标识接收方应该尽快将这个报文段交给应用层。接收到PSH = 1的TCP报文段，应尽快的交付接收应用进程，而不再等待整个缓存都填满了后再向上交付。 |
| RST      | 1比特  | 重建连接标识。当RST=1时，表明TCP连接中出现严重错误（如由于主机崩溃或其他原因），必须释放连接，然后再重新建立连接。 |
| SYN      | 1比特  | 同步序号标识，用来发起一个连接。SYN=1表示这是一个连接请求或连接接受请求。 |
| FIN      | 1比特  | 发端完成发送任务标识。用来释放一个连接。FIN=1表明此报文段的发送端的数据已经发送完毕，并要求释放连接。 |
| 窗口大小 | 16比特 | 窗口：TCP的流量控制，窗口起始于确认序号字段指明的值，这个值是接收端正期望接收的字节数。窗口最大为65535字节。 |
| 校验和   | 16比特 | 校验字段，包括TCP首部和TCP数据，是一个强制性的字段，一定是由发端计算和存储，并由收端进行验证。在计算检验和时，`要在TCP报文段的前面加上12字节的伪首部`。 |
| 紧急指针 | 16比特 | 紧急指针，只有当URG标志置1时紧急指针才有效。TCP的紧急方式是发送端向另一端发送紧急数据的一种方式。紧急指针指出在本报文段中紧急数据共有多少个字节（紧急数据放在本报文段数据的最前面）。 |
| 选项     |        | 选项字段。TCP协议最初只规定了一种选项，即**最长报文段长度**（数据字段加上TCP首部），又称为MSS。MSS告诉对方TCP“我的缓存所能接收的报文段的数据字段的最大长度是MSS个字节”。 新的RFC规定有以下几种选型：选项表结束，无操作，最大报文段长度，窗口扩大因子，时间戳。 *窗口扩大因子*：3字节，其中一个字节表示偏移值S。新的窗口值等于TCP首部中的窗口位数增大到（16+S），相当于把窗口值向左移动S位后获得实际的窗口大小。 *时间戳*：10字节，其中最主要的字段是时间戳值（4字节）和时间戳回送应答字段（4字节）。 选项确认选项： |