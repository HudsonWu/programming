# python 中一些易混淆的概念

## python 中的function与method的区别

A function is a piece of code that is called by name. It can be passed data to operate on (i.e. the parameters) and can optionally return data (the return value). All data that is passed to a function is explicitly passed.

A method is a piece of code that is called by a name that is associated with an object. In most respects it is identical to a function except for two key differences:

1. A method is implicitly passed the object on which it was called.
2. A method is able to operate on data that is contained within the class (remembering that an object is an instance of a class - the class is the definition, the object is an instance of that data).

```python
class C(object):
    def foo(self):
        print(self)
C.foo(1)    # 1
C().foo()   # <__main__.C object at 0x7f7a663db550>
C.foo.__class__ # function
C().foo.__class__   # method
```
需要明确传递参数的是function, 不需要明确传递参数的是method, 类直接调用是function, 类的实例调用是method
实例的函数为bound method, 而类的函数以及闭包均为function
