# lambda, filter, reduce and map

## Lambda

+ `lambda argument_list: expression`

```python
>>> sum = lambda x, y : x + y
>>> sum(3, 4)
7
>>>
```

## The map() Function

+ `r = map(func, seq)`

```python
>>> C = [39.2, 36.5, 37.3, 38, 37.8]
>>> F = list(map(lambda x: (float(9)/5)*x + 32, C))
>>> print(F)
[102.56, 97.7, 99.14, 100.4, 100.03999999999999]
>>> C = list(map(lambda x: (float(5)/9)*(x-32), F))
>>> print(C)
[39.2, 36.5, 37.300000000000004, 38.00000000000001, 37.8]
>>>
```

```python
>>> a = [1, 2, 3, 4]
>>> b = [17, 12, 11, 10]
>>> c = [-1, -4, 5, 9]
>>> list(map(lambda x, y : x+y, a, b))
[18, 14, 14, 14]
>>> list(map(lambda x, y, z : x+y+z, a, b, c))
[17, 10, 19, 23]
>>> list(map(lambda x, y, z : 2.5*x + 2*y -z, a, b, c))
[37.5, 33.0, 24.5, 21.0]
>>>
```

## Filtering

+ `filter(function, sequence)`

```python
>>> fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> odd_numbers = list(filter(lambda x: x % 2, fibonacci))
>>> print(odd_numbers)
[1, 1, 3, 5, 13, 21, 55]
>>> even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
>>> print(even_numbers)
[0, 2, 8, 34]
>>>
>>> even_numbers = list(filter(lambda x: x % 2 -1, fibonacci))
>>> print(even_numbers)
[0, 2, 8, 34]
>>>
```

## Reducing a List

+ `reduce(func, seq)`

```python
>>> from functools import reduce
>>> f = lambda a, b: a if (a > b) else b
>>> reduce(f, [47, 11, 42, 102, 13])
102
>>>
>>> reduce(lambda x, y: x+y, range(1, 101))
5050
>>>
```

```python
>>> from functools import reduce
>>> a = '0 1 abc def ghi jkl mno pqrs tuv wxyz'.split()
>>> b= '23'
>>> reduce(lambda last, current: [x + y for x in last for y in a[int(current)]], b, [''])
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
```
