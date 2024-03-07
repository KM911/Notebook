
> [!faq] Backgroud 
>Programming languages provide built-in types and operators, but user-defined types cannot be added in C.

>[!example]-
>```c
> struct Point {
>     int x;
>     int y;
> };
> 
> typedef struct Point Point;
> Point* createPoint(int x, int y) {
>     Point* p = (Point*)malloc(sizeof(Point));
>     p->x = x;
>     p->y = y;
>     return p;
> }
> int main() {
>     Point* p1 = createPoint(0, 3);
>     Point* p2 = createPoint(4, 0);
>     Point* p3 = p1 + p2;  # invalid operands to binary expression ('Point *' (aka 'struct Point *') and 'Point *')
>     return 0;
> }
> ```


>[!abstract] Solution 
>You can define a function to act like the '+' operator.
> In C++, object-oriented programming (OOP) is provided and the '+' operator is regarded as a method, so you can overload the '+' operator for a class and add it.

>[!example]- C
>```c
> Point* Add(Point* p1, Point* p2) {
>     Point* p = (Point*)malloc(sizeof(Point));
>     p->x = p1->x + p2->x;
>     p->y = p1->y + p2->y;
>     return p;
> }
>```

>[!example]- CPP
> ```cpp
> class Point{
>   int x, y;
>   public:
>     Point(int x, int y) : x(x), y(y) {}
>     Point() : Point(0, 0) {}
>     Point operator+(const Point& p) const {
>         return Point(x + p.x, y + p.y);
>     }
> };
> int main() {
>     Point p1(1, 2);
>     Point p2(3, 4);
>     Point p3 = p1 + p2;
>     return 0;
> }
> ```


>[!done] Benefit
>It will keep code clean, and you could write code as usual. 


## which operate could be overload  ? 
>[!cite] 
[Operator Overloading in C++ - GeeksforGeeks](https://www.geeksforgeeks.org/operator-overloading-cpp/)


### CPP example

### provided class

```cpp
#include <iostream>
using namespace std;
 
class Complex {
private:
    int real, imag;
 
public:
    Complex(int r = 0, int i = 0)
    {
        real = r;
        imag = i;
    }
 
    // This is automatically called when '+' is used with
    // between two Complex objects

    void print() { cout << real << " + i" << imag << '\n'; }
};
```
### + 

```cpp
Complex operator+(Complex const& obj)
{
    Complex res;
    res.real = real + obj.real;
    res.imag = imag + obj.imag;
    return res;
}
```

```cpp
int main()
{
    Complex c1(10, 5), c2(2, 4);
    Complex c3 = c1 + c2;
    c3.print();
}
```

 
## Which operate you could overload 

````col
```col-md
flexGrow=1
===
| type           | symbol   |
| -------------- | -------- |
| binary operate | + - *  % |
```
```col-md
flexGrow=1
===
| type           | symbol   |
| -------------- | -------- |
| binary operate | + - *  % |
```

````

> [!faq] why I could not overload every operate? 
> 1. some operate even overload have no meaning, like :: , it just define scope 
> 2. it could be overload in other complier just stand c++ do not implement it. 
|

 
| Operators that can be overloaded        | Examples                  |
| --------------------------------------- | ------------------------- |
| Binary Arithmetic                       | `+, -, *, /, %`           |
| Unary Arithmetic                        | `+, -, ++, —`             |
| Assignment                              | `=, +=,*=, /=,-=, %=`     |
| Bitwise                                 | `& , << , >> , ~ , ^` |
| De-referencing                          | `(->)`                    |
| Dynamic memory allocation,De-allocation | `New, delete `            |
| Subscript                               | `[ ]`                     |
| Function call                           | `	()`                     |
| Logical                                 | `&`,  `!`             |
| Relational                              | `>, < , = =, <=, >=`      |


## list of operators that cannot be overloaded. 

```cpp
sizeof
typeid
Scope resolution (::)
Class member access operators (.(dot), .* (pointer to member operator))
Ternary or conditional (?:)
```

>[!done] reason 
> They are simple operations that doesn't require any custom behavior.



## default operator 

>[!faq] empty class 
>if you do not write any operator for a class ( empty class) , complier will generat default operator for this class. 

```cpp
New 
Copy

```
## Important Points about Operator Overloading 

