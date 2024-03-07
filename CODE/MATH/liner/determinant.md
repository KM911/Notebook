
>[!help] 虽然国内大部分的教程都是将 ==行列式== determinant 作为前置知识 
>其实并不非常合理的. 不过我们不是在记录知识体系,而是在重新搭建自己的知识内容. 
>

>[!note] 其意义在不同场景有不同含义,所以我们还是介绍其计算方式.

### 计算方式

行列式一定是nxn的,行列数目相等. 

计算方式为, 从不同行,不同列中取三个值,如果行数和+列数和为

$$\begin{vmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{vmatrix}
$$


$$
 \begin{vmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{vmatrix} = (a \times ei - b \times fi) - (c \times ei - b \times gi) + (c \times fh - a \times fh)
$$

这个结果可以用来判断一个 3x3 矩阵是否可逆。如果行列式不为零，则矩阵可逆；如果行列式为零，则矩阵不可逆。


$$
\begin{vmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \dots & a_{nn}
\end{vmatrix} = a_{11} \begin{vmatrix}
a_{22} & \dots & a_{2n} \\
\vdots & \ddots & \vdots \\
a_{n2} & \dots & a_{nn}
\end{vmatrix} - a_{12} \begin{vmatrix}
a_{21} & \dots & a_{2n} \\
\vdots & \ddots & \vdots \\
a_{n1} & \dots & a_{nn}
\end{vmatrix} + \dots + (-1)^{n+1} a_{1n} \begin{vmatrix}
a_{21} & \dots & a_{22} \\
\vdots & \ddots & \vdots \\
a_{n1} & \dots & a_{n1}
\end{vmatrix}

$$


### 行列式的性质 

1.行列式经过装置后,行列式的值不变. 

