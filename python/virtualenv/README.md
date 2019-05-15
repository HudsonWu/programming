# virtualenv

```
# 安装
pip install virtualenv

# 创建项目的虚拟环境
cd my_project_folder
virtualenv venv  # venv可替换为别的虚拟环境名称
virtualenv --system-site-packages venv  # 如果想使用系统环境的第三方软件包时

# 使用虚拟环境
cd venv
source bin/activate  # windows下运行Scripts\
python -V

# 退出虚拟环境
deactivate

# 删除虚拟环境
(venv)$ deactivate
rm -r /path/to/venv
```
