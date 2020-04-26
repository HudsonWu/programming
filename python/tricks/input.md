# 输入处理


## 多个空格替换为一个

```py
import re

line = str(input())
line = re.sub('\s+', ' ', line)
```

# 输入分离为多个数字

```py
inp = list(map(int, input().split()))
```
