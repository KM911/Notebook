
## create table



## modify table 

我们可能会修改表的结构,1.创建时出错了,2.业务发生了变化,

>[!abstract] 修改表的操作
>修改表名, sp_rename 'name_old','name_new';
>修改列名, sp_rename 'table.name_old', 'name_new', 'column';
>新增列,  alter table jobs add year int;
>删除列,  alter table jobs drop column year;
> 修改列的类型 alter table jobs alter column year date;

>[!error] 修改列的类似是不能随意修改的,已有的数据类型无法转换.可能会导致丢失数据或者操作失败.

>[!error] 新增列
>如果一个表中已经存在了数据,此时创建新列,已有数据的该列将会为NULL. 

 
这里其实又有一个问题了
- [ ] 当table 以有数据了, 我们执行修改列的操作可以成功吗? 我认为是不可以的.