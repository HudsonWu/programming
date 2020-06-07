# itertools

## 排列组合

```python
>>> import itertools
>>> # 排列
>>> perms = itertools.permutations([1, 2, 3], 2)
>>> next(perms)
(1, 2)
>>> # 组合
>>> list(itertools.combinations('ABC', 2))
[('A', 'B'), ('A', 'C'), ('B', 'C')]
>>> # 返回包含两个序列的笛卡尔乘积迭代器
>>> list(itertools.product('ABC', '123'))
[('A', '1'), ('A', '2'), ('A', '3'),
 ('B', '1'), ('B', '2'), ('B', '3'),
 ('C', '1'), ('C', '2'), ('C', '3')]
```

## 分组

```python
>>> names = ['Dora', 'Ethan', 'Wesley', 'John', 'Lizzie']
>>> names = sorted(names)
>>> names
['Dora', 'Ethan', 'John', 'Lizzie', 'Wesley']
>>> names = sorted(names, key=len)
>>> names
['Dora', 'John', 'Ethan', 'Lizzie', 'Wesley']
>>> import itertools
>>> groups = itertools.groupby(names, len)
>>> groups
<itertools.groupby object at 0x02FB7270>
>>> list(groups)
[(4, <itertools._grouper object at 0x02FA5E10>), 
 (5, <itertools._grouper object at 0x02FA5DD0>), 
 (6, <itertools._grouper object at 0x02FBB990>)]
>>> groups = itertools.groupby(names, len)
>>> for name_length, name_iter in groups:
...     print(f"Names with {name_length} letters")
...     for name in name_iter:
...         print(name)
...
Names with 4 letters
Dora
John
Names with 5 letters
Ethan
Names with 6 letters
Lizzie
Wesley
```

```python
>>> import itertools
>>> list(itertools.chain(range(0, 3), range(10, 13)))
[0, 1, 2, 10, 11, 12]
>>> list(zip(range(0, 3), range(10, 13)))
[(0, 10), (1, 11), (2, 12)]
>>> list(zip(range(0, 3), range(10, 14)))
[(0, 10), (1, 11), (2, 12)]
>>> list(itertools.zip_longest(range(0, 3), range(10, 14)))
[(0, 10), (1, 11), (2, 12), (None, 13)]
```