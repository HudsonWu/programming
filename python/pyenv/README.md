# 使用pyenv

## python多版本管理

```
# 更新可发现的python版本
pyenv update
# 查看可安装版本
pyenv install --list
# 安装指定版本
pyenv install 3.7.2
# 查看当前版本
pyenv versions
# 卸载指定版本
pyenv uninstall 2.7.15
# 启用指定版本
pyenv global 3.7.2
# 查看python路径
pyenv which python
# 设置本地python版本
pyenv local 3.8.5
# 查看命令
pyenv commands
# 查看帮助
pyenv shims --help
# 启动shell
pyenv shell 3.8-dev
```

## 虚拟环境管理 (pyenv-virtualenv插件)

```
# 创建虚拟环境
pyenv virtualenv 3.6.8 myproject
# 激活虚拟环境
pyenv activate myproject
# 退出虚拟环境
pyenv deactivate
```

## 使用技巧

```
# 国内加速, 配置环境变量
变量名: PYTHON_BUILD_MIRROR_URL
变量值: https://npm.taobao.org/mirrors/python/

# 使用指定源下载python
$ export v=2.7.6; wget https://npm.taobao.org/mirrors/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/; pyenv install $v 
```
