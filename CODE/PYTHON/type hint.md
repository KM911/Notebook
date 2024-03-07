---
file-created: Wednesday, November ,2023
last-modified: Saturday, November ,2023
---

> [!note]   type hinting
> Dynamic languages do not need to declare variable type, but this can cause some problems for type errors, so Python provides a method like this example below:

```python
# Type hint for a variable
name: str = "Alice"

# Type hint for a function argument
def greet(name: str) -> str:
  return "Hello, {}!".format(name)

# Type hint for a function return value
def add_numbers(a: int, b: int) -> int:
  return a + b

# Type hint for a generic type
class MyList(list[int]):
  pass
```
