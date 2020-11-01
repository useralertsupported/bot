If you ever find yourself writing something like this:
```py
squre_numbers = []
for n in range(10):
    square_numbers.append(n ** 2)
```
Using a list comprehensions can greatly improve your code's readability.
```py
square_numbers = [n ** 2 for n in range(10)]
```

For more info, check out [this post](http://www.pythonforbeginners.com/basics/list-comprehensions-in-python) or read [PEP 202](https://www.python.org/dev/peps/pep-0202/).
