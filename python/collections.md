# python3之collections模块

## namedtuple

namedtuple是一个函数, 它用来创建一个自定义的元组对象, 并且规定了元组元素的个数, 可以用属性而不是索引来引用元组的某个元素. 可以通过namedtuple来定义一种数据类型, 它具备元组的不变性, 又可以根据属性来引用

```python
>>> from collection import namedtuple
>>> Mytuple = namedtuple('Mytuple', ['x', 'y'])
>>> n = Mytuple(11, 22)
>>> n.x
11
>>> n.y
22
```

## deque


使用list存储数据时, 按照索引访问元素很快, 但是插入和删除元素就很慢了, 因为list是线性存储, 数据量大的时候, 插入和删除效率很低. deque是为了高效实现插入和删除操作的双向列表, 适合用于队列和栈

```python
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')    # 默认添加到列表最后一项
>>> q.appendleft('y')    # 默认添加到列表第一项
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
>>> q.pop()    # 默认删除列表最后一个元素
'x'
>>> q.popleft()    # 删除列表的第一个元素
'y'
>>> q
deque(['a', 'b', 'c'])
```

## defaultdict

使用字典时, 如果引用的key不存在, 就会抛出KeyError, 如果希望key不存在时, 返回一个默认值, 就可以用defaultdict

```python
>>> from collections import defaultdict
>>> Mydict = defaultdict(lambda: 'N/A')
>>> Mydict['key1'] = 'abc'
>>> Mydict['key1']
'abc'
>>> Mydict['key2']
'N/A'
```
注意默认值是调用函数返回的, 而函数在创建defaultdict对象时传入, 除了key不存在而返回默认值, 其他功能与普通字典无异

## OrderedDict

有序字典的应用, OrderedDict的有序性是按照插入的顺序, 而不是KEY的顺序

```python
>>> from collections import OrderedDict
>>> d = dict([('a', 1), ('b', 2), ('c', 3)])
>>> d # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
>>> od = OrderedDict([('a': 1), ('b': 2), ('c': 3)])
>>> od # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

通过OrderedDict可以实现一个FIFO(先进先出)的字典, 当容量超出限制后, 先删除最早添加的KEY

```python
from collections import OrderedDict
 
class LastUpdatedOrderedDict(OrderedDict):
 
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity
 
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
```

## Counter

简单的计数器, 例如, 统计字符出现的个数

```python
>>> from collections import Counter
>>> c = Counter()
>>> for ch in 'programming':
...     c[ch] = c[ch] + 1
...
>>> c
Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
```
