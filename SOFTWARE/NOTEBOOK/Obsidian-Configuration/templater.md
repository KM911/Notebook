
>[!note] obsidian 本身就提供简单的"模板"功能, templater进行了增强


>[!tip] let's define a few terms:
>A template is a file that contains commands.
A text snippet that starts with an opening tag <%, ends with a closing tag %> is what we will call a command.
A function is an object that we can invoke inside a command and that returns a value (the replacement string)



>[!exp] 将templater 的 function 作为参数使用. 
>通过tp.file.path()可以获取当前文件的绝对路径,交给python程序处理. 
><% tp.user.python("template",tp.file.path())%>

>[!exp] 同样的,我们应该也可以将python函数的返回值作为参数交给templater的函数. 

