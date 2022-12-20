# Notes

- [Notes](#notes)
  - [Basics](#basics)

---
## Basics
`*range()`: The `*` "unpacks" an iterable, so that each element is passed as a separate argument, rather than the function receiving the iterable object as a single argument:

```python
>>> print(range(1,3))
range(1, 3)
>>> print(*range(1,3))
1 2
>>> print(1,2)
1 2

# More examples
>>> n = 3
>>> print(*range(1, n + 1), sep='')
123
```

`map()`:

```python

```

`from collections import Counter`:

`xrange()`:

`set()`: