# eval

```python
>>> eval('1 + 1 == 2')
True
>>> eval('"A" + "B"')
'AB'
>>> eval('[*] * 5')
['*', '*', '*', '*', '*']
>>> x = 5
>>> eval("pow(x, 2)")
25
>>> import math
>>> eval('math.sqrt(x)')
>>> import subprocess
>>> eval("subprocess.getoutput('ls ~')")
'dir1' 'dir2' 'file1'
>>> eval("__import__('subprocess').getoutput('rm /some/random/file')")
```

## 安全使用eval

```python
>>> # 传给eval函数第二和第三个参数作为独立的全局和局部变量
>>> # 将"__builtins__" (内建函数的集合) 映射为None
>>> x = 5
>>> import math
>>> eval('x * 5', {"x": x}, {})
25
>>> eval("math.sqrt(x)", {"__builtins__": None, 'x': x, "math": math}, {})
2.23606797749979
>>> # 未解决安全问题，拒绝服务攻击
>>> eval("2 ** 2147483647", {"__builtins__: None"}, {})
```