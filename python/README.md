# Python

## pip

```
# 依赖文件
pip freeze > requirements.txt
pip install -r requirements.txt

# 更新为指定版本
pip install --upgrade tensorflow==1.1.0rc2
```

## Trace

```
python -m trace --count -C . somefile.py

python -m pdb somefile.py
```

```
import pdb
pdb.set_trace()
```

## Tips

```
# CentOS系统下python3交互界面反向键、删除键启用
yum install -y readline-devel
```

## References

+ [Python Programming Language](https://www.geeksforgeeks.org/python-programming-language/)
+ [Dive Into Python3](http://bigsec.net/b52/dive-into-python3/index.html)

