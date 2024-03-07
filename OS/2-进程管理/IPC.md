
>[!others] Everything 会对磁盘全部的文件建立索引. 我现在想要在我的程序中复用Everything的索引,就必须要和Everything这个程序进行交互. 


>[!note] IPC : Inter-process communication 

## How

 | Method | Short Description | Provided by (operating systems or other environments) |
 | --- | --- | --- |
 | File | A record stored on disk, or a record synthesized on demand by a file server, which can be accessed by multiple processes. | Most operating systems |
 | Communications file | A unique form of IPC in the late-1960s that most closely resembles Plan 9's 9P protocol | Dartmouth Time-Sharing System |
 | Signal; also Asynchronous System Trap | A system message sent from one process to another, not usually used to transfer data but instead used to remotely command the partnered process. | Most operating systems |
 | Socket | Data sent over a network interface, either to a different process on the same computer or to another computer on the network. Stream-oriented (TCP; data written through a socket requires formatting to preserve message boundaries) or more rarely message-oriented (UDP, SCTP). | Most operating systems |
 | Unix domain socket | Similar to an internet socket, but all communication occurs within the kernel. Domain sockets use the file system as their address space. Processes reference a domain socket as an inode, and multiple processes can communicate with one socket | All POSIX operating systems and Windows 10[3] |
 | Message queue | A data stream similar to a socket, but which usually preserves message boundaries. Typically implemented by the operating system, they allow multiple processes to read and write to the message queue without being directly connected to each other. | Most operating systems |
 | Anonymous pipe | A unidirectional data channel using standard input and output. Data written to the write-end of the pipe is buffered by the operating system until it is read from the read-end of the pipe. Two-way communication between processes can be achieved by using two pipes in opposite "directions". | All POSIX systems, Windows |
 | Named pipe | A pipe that is treated like a file. Instead of using standard input and output as with an anonymous pipe, processes write to and read from a named pipe, as if it were a regular file. | All POSIX systems, Windows, AmigaOS 2.0+ |
 | Shared memory | Multiple processes are given access to the same block of memory, which creates a shared buffer for the processes to communicate with each other. | All POSIX systems, Windows |
 | Message passing | Allows multiple programs to communicate using message queues and/or non-OS managed channels. Commonly used in concurrency models. | Used in LPC, RPC, RMI, and MPI paradigms, Java RMI, CORBA, COM, DDS, MSMQ, MailSlots, QNX, others |

