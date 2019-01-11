# Python异常

异常即是一个事件, 该事件会在程序执行过程中发生, 影响了程序的正常执行. 一般情况下, 在Python无法正常处理程序时就会发生一个异常. 异常是Python对象, 表示一个错误.

当Python脚本发生异常时, 我们需要捕获处理它, 否则程序会终止执行

python提供了两个非常重要的功能来处理python程序在运行中出现的异常和错误, 你可以使用该功能来调试python程序
+ 异常处理
+ 断言(Assertions)

python标准异常:
```
Exception    所有异常的基类
StopIteration    当一个迭代器的next()方法不指向任何对象时引发
SystemExit    由sys.exit()函数引发
StandardError    除了StopIteration异常和SystemExit, 所有内置异常的基类
ArithmeticError    数值计算所发生的所有错误的基类
OverflowError    当数字类型计算超过最高限额引发
FloatingPointError    当一个浮点运算失败时触发
ZeroDivisonError    当除运算或模零在所有数值类型运算时引发
AssertionError    断言语句失败的情况下引发
AttributeError    属性引用或赋值失败的情况下引发
EOFError    当从raw_input()与input()函数输入, 到达文件末尾时触发
ImportError    当一个import语句失败时触发
KeyboardInterrupt    当用户中断程序执行, 通常是通过按Ctrl+c引发
LookupError    所有查找错误基类
IndexError    当在一个序列中没有找到一个索引时引发
KeyError    当指定的键没有在字典中找到引发
NameError    当在局部或全局命名空间中找不到的标识引发
UnboundLocalError    试图访问在函数或方法的局部变量时引发, 但没有值分配给它。
EnvironmentError    Python环境之外发生的所有异常的基类。
IOError    当一个输入/输出操作失败, 如打印语句或open()函数试图打开不存在的文件时引发
IOError    操作系统相关的错误时引发
SyntaxError    当在Python语法错误引发；
IndentationError    没有正确指定缩进引发。
SystemError    当解释器发现一个内部问题, 但遇到此错误时, Python解释器不退出引发
SystemExit    当Python解释器不使用sys.exit()函数引发。如果代码没有被处理, 解释器会退出。
ValueError    当操作或函数在指定数据类型无效时引发
ValueError    在内置函数对于数据类型, 参数的有效类型时引发, 但是参数指定了无效值
RuntimeError    当生成的错误不属于任何类别时引发
NotImplementedError    当要在继承的类来实现, 抽象方法实际上没有实现时引发此异常
```

## 异常处理

捕获异常可以使用try/except语句, try/except语句用来检测try语句块中的错误, 从而让except语句捕获异常信息并处理, 如果你不想在异常发生时结束你的程序, 只需在try里捕获它

语法:
```
try:
    <语句>  # 运行别的代码
except <名字>:
    <语句>  # 如果try部分引发了'name'异常
except <名字>, <数据>:
    <语句>  # 如果引发了'name'异常, 获得附加的数据
else:
    <语句>  # 如果没有异常发生
```

try的工作原理是: 当开始一个try语句后, python就在当前程序的上下文中做标记, 这样当异常出现时就可以回到这里, try子句先执行, 接下来会发生什么, 依赖于执行时是否出现异常:
+ 如果try后的语句执行时发生异常, python就跳回try并执行第一个匹配该异常的except子句, 异常处理完毕, 控制流就通过整个try语句(除非处理异常时又引发新的异常)
+ 如果在try后的语句里发生了异常, 却没有匹配的except子句, 异常将被递交到上层的try, 或者到程序的最上层(这样将结束程序, 并打印默认的出错信息)
+ 如果在try子句执行时没有发生异常, python将执行else语句后的语句(如果有else的话), 然后控制流通过整个try语句

1. python3要求我们的异常必须继承Exception类, Built-in的所有异常也都是继承自这个类
```python
try:
    raise
except Exception as err:
    print(err)
```

2. except后若不接上任何异常类型, 则表示捕捉所有异常, 这包括了所有的系统异常, 有时这并不是你想要的行为, 例如, 下面的程序, 无法通过KeyboardInterrupt来中断循环:
```python
while True:
    try:
        print('Run it...')
    except:
        print('exception happened...')
```
可以改为以下的方式:
```python
while True:
    try:
        print('Run it...')
    except Exception:
        print('exception happened...')
```
在python3中, Exception是BaseException的子类, 可以捕捉除了系统异常以外的所有异常

3. 一个except语句可以同时包括多个异常名, 但需要用括号括起来:
```python
except (RuntimeError, TypeError, NameError):
    pass
```

4. 可以在except捕捉到异常后, 将异常事件指定给变量:
```python
try:
    raise IndexError('11')
except IndexError as e:
    print(type(e), str(e))
```

### 一些例子

```python
try:
    x = int(input('please input an integer:'))
    if 30/x > 5:
        print('Hello world')
except ValueError:
    print('That was no valid number. Try again...')
except ZeroDivisionError:
    print('The divisor can not be zero, Try again...')
except:
    print('Handling other exceptions...')
```

```python
try:
    fh = open("testfile", "w")
    try:
        fh.write("test file, test exception")
    finally:
        print("close file")
        fh.close()
except IOError:
    print("Error: write failed")
```

### `sys.exc_info()` 和  `sys.last_traceback`

`sys.exc_info()`会返回一个3值元表, 其中包含调用该命令时捕获的异常

这个元表的内容为 (type, value, traceback) :
+ type, 从获取到的异常中得到类型名称, 它是BaseException的子类
+ value, 捕获到的异常实例
+ traceback, 一个traceback对象

`sys.last_traceback`包含的内容与`sys.exc_info()`相同, 但主要用于调试, 并不总是被定义

```python
import sys
try:
    raise
except:
    t, v, tb = sys.exc_info()
    print(t, v)
```

### `traceback`

traceback模块用来精确模仿python3解析器的stack trace行为, 在程序中应该尽量使用这个模块

1. `traceback.print_exc()`, 直接打印当前的异常
```python
import traceback
try:
    raise
except:
    traceback.print_exec()
```

2. `traceback.print_tb()`, 用来打印traceback对象
```python
import sys, traceback
try:
    raise
except:
    t, v, tb = sys.exc_info()
    traceback.print_tb(tb)
```

3. `traceback.print_exception()`, 直接打印 `sys.exc_info`提供的元表
```python
import sys, traceback
try:
    raise
except:
    traceback.print_exception(*sys.exc_info())
```

下面两句是等价的:
+ `traceback.print_exc()`
+ `traceback.print_exception(*sys.exc_info())`

## 抛出异常(raise)

raise语句允许强制地抛出一个特定的异常

raise抛出的异常必须是一个异常实例或类(派生自Exception的类)

```
raise [Exception [, args [, traceback]]]
```
语句中Exception是异常的类型(如NameError), args是自己提供的异常参数, 最后一个参数可选(实践中很少), 如果存在, 是跟踪异常对象

test.py:
```python
# 定义函数
def mye( level ):
    if level < 1:
        raise Exception,"Invalid level!"
        # 触发异常后, 后面的代码就不会再执行
try:
    mye(0)            # 触发异常
except Exception,err:
    print(1, err)
else:
    print(2)
```

```console
$ python test.py
1 Invalid level!
```

### 用户自定义异常

通过创建一个新的异常类, 程序可以命名它们自己的异常, 异常应该是典型的继承自Exception类, 通过直接或间接的方式

```
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print(e.args)
```
