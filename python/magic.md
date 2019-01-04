# Python 特殊属性与方法

python对象中以双下划线开头和结尾的属性称为特殊属性, 由于对象的方法也属于属性, 因此以双下划线开头和结尾的方法称为特殊方法, 对这些对象执行一些特定的运算时, python会自动调用这些实例的特殊方法, 从而在python中可以很轻易地实现运算符的重载


## Python自定义函数的特殊属性

Python中通过函数定义所创建的用户自定义函数对象均具有一些特殊属性

```python
class Test():
    def func(self, v = 'dog'):
        '''这里是一个闭包函数'''

        name = 'dobi'
        def inn_func(age = 1):
            print(name, v, age)

        return inn_func

test = Test()
clsfunc = test.func()

print(Test.func)    # <function Test.func at 0x7ff7c7afdd90>
print(test.func)    # <bound method Test.func of <__main__.Test object at 0x7ff7c7a5f6a0>>
print(clsfunc)  # <function Test.func.<locals>.inn_func at 0x7ff7c7b51bf8>
```

1. `__doc__`
可写, 用于获取函数的文档说明, 如果没有, 则返回`None`
```console
>>> print('Test.func.__doc__:', Test.func.__doc__)
Test.func.__doc__: 这里是一个闭包函数
>>> Test.func.__doc__ = 'ddd'   # 注意, 这里是Test, 不是test
>>> print('Test.func.__doc__:', Test.func.__doc__)
Test.func.__doc__: ddd
```

2. `__name__`
可写, 获取函数的名称
```console
>>> print('Test.func.__name__:', Test.func.__name__)
Test.func.__name__: func
>>> Test.func.__name__ = 'pet'
>>> print('Test.func.__name__:', Test.func.__name__)
Test.func.__name__: pet
```

3. `__qualname__`
可写, 获取函数的qualname, 点示法显示函数名称、所在的类、模块等梯级地址
```console
>>> print('Test.func.__qualname__:', Test.func.__qualname__)
Test.func.__qualname__: Test.func
>>> Test.func.__qualname__ = 'path'
>>> print('Test.func.__qualname__:', Test.func.__qualname__)
Test.func.__qualname__: path
```

4. `__module__`
可写, 返回函数所在的模块, 如果无则返回None
```console
>>> print('Test.func.__module__:', Test.func.__module__)
Test.func.__module__: __main__
>>> Test.func.__module__ = 'a'
>>> print('Test.func.__module__:', Test.func.__module__)
Test.func.__module__: a
```

5. `__defaults__`
可写, 以元组的形式返回函数的默认参数, 如果无默认参数则返回None
```console
>>> print('Test.func.__defaults__:', Test.func.__defaults__)
Test.func.__defaults__: ('dog',)
>>> Test.func.__defaults__ = ('cat',)
>>> print('Test.func.__defaults__:', Test.func.__defaults__)
Test.func.__defaults__: ('cat',)
>>> print('clsfunc.__defaults__:', clsfunc.__defaults__)
clsfunc.__defaults__: (1,)
```

6. `__code__`
可写, 返回已编译的函数对象
```console
>>> print('Test.func.__code__:', Test.func.__code__)
Test.func.__code__: <code object func at 0x7ff7c7a5e540, file "<stdin>", line 2>
>>> def func2():print('cat')

>>> def func2():print('cat')
>>> Test.func.__code__ = func2.__code__
>>> Test.func()
cat
>>> print('Test.func.__code__:', Test.func.__code__)
Test.func.__code__: <code object func2 at 0x7ff7c7a5e660, file "<stdin>", line 1>
```

7. `__globals__`
只读, 以字典的形式返回函数所在的全局命名空间所定义的全局变量
```console
>>> print('Test.func.__globals__:', Test.func.__globals__)
Test.func.__globals__: {'clsfunc': <function Test.func.<locals>.inn_func at 0x7ff7c7b51bf8>, '__name__': '__main__', 'func2': <function func2 at 0x7ff7c7afde18>, '__spec__': None, 'test': <__main__.Test object at 0x7ff7c7a5f6a0>, '__builtins__': <module 'builtins' (built-in)>, '__package__': None, 'Test': <class '__main__.Test'>, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__doc__': None}
```

8. `__dict__`
可写, 以字典的形式返回命名空间所支持的任意自定义的函数属性
```console
>>> print('Test.func.__dict__:', Test.func.__dict__)
Test.func.__dict__: {}
```

9. `__closure__`
只读, 以包含cell的元组形式返回闭包所包含的自由变量
```console
>>> print('Test.func.__closure__:', Test.func.__closure__)
Test.func.__closure__: None
>>> print('clsfunc.__closure__:', clsfunc.__closure__)
clsfunc.__closure__: (<cell at 0x7ff7c7a62168: str object at 0x7ff7c7a5f420>, <cell at 0x7ff7c7a620d8: str object at 0x7ff7c7a5f3e8>)
>>> print('clsfunc.__closure__[x]:', clsfunc.__closure__[0].cell_contents, clsfunc.__closure__[1].cell_contents)
clsfunc.__closure__[x]: dobi dog
```

10. `__annotations__`, python的函数注释
```python
def dog(name:str = 'dobi', age:(1, 99) = 3, species:'breed of dogs' = 'Labrador') -> tuple:
    return (name, age, species)
```
使用`:`对参数逐个进行注释, 注释内容可以是任何形式, 比如参数的类型、作用、取值范围等, 返回值使用`->`标注, 所有的注释都会保存至函数的属性
```console
>>> dog.__annotations__
{'age': (1, 99), 'name': str, 'return': tuple, 'species': 'breed of dogs'}
```

11. `__kwdefaults__`, Keyword-Only Arguments, 强制关键字参数
```python
def dog(name, host, *, age):
    print(name, host, age)

dog('dobi', 'xuzhoufeng', 2)    # TypeEroor: dog() takes 2 positional arguments but 3 were given
dog('dobi', 'xuzhoufeng', age = 2)  # dobi xuzhoufeng 2
```
参数中有一个`*`, 在该符号之后的所有参数(可一至多个)均被称为强制关键字参数


## Python中一些通用的特殊函数

### 初始化与终止化

+ `__new__(cls[, args...])`

  `__new__()`是一个静态方法, 用于根据类型创建实例. Python在调用`__new__()`方法获得实例后, 会调用这个实例的`__init__()`方法, 然后将最初传给`__new__()`方法的参数都传给`__init__()`方法. 


+ `__init__()`

  `__init__()`是一个实例方法, 用来在实例创建完成后进行必要的初始化, 该方法必须返回None.

  Python不会自动调用父类的`__init__()`方法, 这需要额外的调用: 

```
super(C, self).__init__()
```
 

+ `__del__(self)`

   在GC之前, Python会调用这个对象的`__del__()`方法完成一些终止化工作. 如果没有`__del__()`方法, 那么Python不做特殊的处理; 

  Python无视`__del__()`方法的返回值; 

  Python不会自动调用父类的`__del__()`方法, 除非显式调用; 

  定义了`__del__()`方法的实例无法参与到循环GC中, 所以对于这样的实例应该避免循环引用; 

  try/finally语句或with语句可能是比`__del__()`更好的方式. 

 

### 表现形式

+ `__repr__(self)`

  Python内置的repr()函数, `x`表达式形式, 或者交互式解释器在显示一个表达式语句的结果时, 都调用这个对象的`__repr__()`方法; 

  `__repr__()`方法返回的字符串主要是面向解释器的, 改写的话应该满足:  eval(repr(x)) == x . 

  如果没有定义`__repr__()`, 那么Python使用一种默认的表现形式. 

 

+ `__str__(self)`

  Python内置的1. str()函数, 2. print(x)语句, 都会调用对象的`__str__()`方法; 

  与`__repr__()`返回的详尽的、准确的、无歧义的对象描述字符串不同, `__str__()`方法只是返回一个对应对象的简洁的字符串表达形式; 

  当`__str__()`缺失时, Python会调用`__repr__()`方法; 

  `__str__()`返回的字符串应该是面向用户的, 可读的. 

 

+ `__unicode__(self)`

  Python内置的unicode(x)方法会调用`__unicode__()`方法; 

  该方法如果定义, 优先级高于`__str__()`方法; 

  同时定义这两个方法的实例, 调用它们的结果应该相同. 

 

### 比较、哈希与布尔值

+ `__lt__(self, other)`

  `x<y` 运算将会调用实例x的__lt__(self, other)方法; 

 

+ `__le__(self, other)`

  `x<=y` 运算将会调用实例x的__le__(self, other)方法; 

 

+ `__gt__(self, other)`

  `x>y` 运算将会调用实例x的__gt__(self, other)方法; 

 

+ `__ge__(self, other)`

  `x>=y` 运算将会调用实例x的__ge__(self, other)方法; 

 

+ `__eq__(self, other)`

  `x==y` 运算将会调用实例x的__eq__(self, other)方法; 

 

+ `__ne__(self, other)`

  `x!=y` 运算将会调用实例x的__ne__(self, other)方法; 

  *上述用于实例间比较的特殊方法应该返回True或False, 或者返回NotImplemented来告诉Python解释器使用其他的方式进行比较. 

 

+ `__cmp__(self, other)`

  对于上面提到的比较操作, 如果对应的特殊方法没有定义或者返回NotImplemented, 则会调用__cmp__(self, other)再进行一次尝试; 

  一些内置的方法: cmp(x, y), max(x, y)或者列表对象的sort()方法也会调用`__cmp__()`方法; 

  实现x.`__cmp__()`方法时, 如果x小于y, 应该返回-1, 如果x大于y, 应该返回1; 如果x等于y, 应该返回0.

  对于序列化比较（<, <=, >=, >）, 如果最终`__cmp__()`也没有定义, 那么会抛出异常; 

  对于相等与否的比较（==, !=）, 如果最终`__cmp__()`也没有定义, 将会变成身份检验: 判断id(x) == id(y)是否成立. 

 

+ `__hash__(self)`

  三种情形会调用`__hash__()`方法: 1. 内置的hash()方法, 2.作为字典的键时, 3.作为集合的成员时; 

  `__hash__()`方法应该返回一个32位长的整数, 对与同一个对象, `__hash__()`方法应该总是返回相同的值; 对于 x == y , 即使二者不属于相同的类型, 只要他们是可哈希的（hashable）, 都应该确保得到 hash(x) == hash(y) ; 

  没有 `__hash__()` 方法, 也没有 `__cmp__()` 和 `__eq__()` 方法, 上面提到的三种情形将使用id(x)作为替代; 

  没有 `__hash__()` 方法, 但是有 `__cmp__()` 和 `__eq__()` 方法, 上面提到的前两种方法会抛出异常; 

  通常只为同时定义了 `__cmp__()`和/或`__eq__()` 方法的不可变（immutable）对象定义`__hash__()`方法, 

  

+ `__nonzero__(self)`

  判断一个对象是为真还是假时, 例如调用bool(x)方法时, Python会调用x.__nonzero__(self)方法, `__nonzero__()`方法应该返回True或False. 

  如果实例没有`__nonzero__()`方法, 那么Python会调用实例的`__len__()`方法, 当`__len__()`方法返回0时, Python认为该对象为假. 所以如果实例没有`__nonzero__()`方法与`__len__()`方法, 则Python认为该实例总是真的; 

  *所以以一个容器是否非空为判断条件时, 应该写成: 

if container:
  pass
而不是: 

if len(container) > 0 :
  pass
因为后者将错过`__nonzero__()`方法的检验. 

 

### 属性的引用、绑定与解绑定

+ `__getattribute__(self, name)`

  访问对象的属性 x.y 时, Python会自动调用 x.__getattribute__('y') 方法; 

  `__getattribute__()` 方法应该返回被访问的属性或者是抛出异常 AttributeError ; 

  重写类型的 `__getattribute__()` 方法会导致实例的属性访问变慢. 

 

+ `__getattr__(self, name)`

  当常规的属性访问（ x.__class__ 或 x.__dict__ 的键访问）无法找到目标属性时, Python会调用 `__getattr__()` 方法; 

  如果该方法没能找到目标属性, 应该抛出 AttributeError . 

 

  *区别 __getattribute__ 和 __getattr__, 前者是任何通过 x.y 访问实例的属性时都会调用的特殊方法, 而后者则是在正常访问形式下无法找到的情况下才会被调用. 

+ `__setattr__(self, name, value)`

  绑定实例的某个属性（赋值）, 例如 x.y = value 时, Python会自动调用 x.__setattr__('y', value) 方法; 

  Python无视 `__setattr__()` 方法的返回值; 

  如果没有定义 `__setattr__()` 方法, Python将赋值 x.y = value 解释成 x.__dict__['y'] = value . 

 

+ `__delattr__(self, name)`

  当解绑定一个对象的某个属性（例如调用 del x.y ）时, 会调用 x.__delattr__('y') 方法; 

  Python无视`__delattr__()`方法的返回值; 

  如果没有定义`__delattr__()`方法, 那么Python将 del x.y 解释成 del x.__dict__['y'] . 

 

### 可调用对象

+ `__call__(self[, args...])`

   定义了该方法的对象可以像函数那样被调用, 因此被称为可调用对象. 
