# python的退出方式

一般情况下使用sys.exit()即可, 一般在fork出来的子进程中使用os.exit()

## os.exit()

直接退出python程序, 其后的代码也不会继续执行


## sys.exit()

引发一个SystemExit异常, 若没有捕获这个异常, python解释器会直接退出, 捕获这个异常可以做一些额外的清理工作

0为正常退出, 其他数值(1-127)为不正常, 可抛出异常事件供捕获

## 终止程序并给出错误信息

向标准错误打印一条消息并返回某个非零状态码来终止程序运行
```python
raise SystemExit('It failed!')
```
它会将消息在sys.stderr中打印, 然后程序以状态码1退出
