# npm使用

## 常用命令及参数

### npm install

```
# 不指定版本时默认安装最新版本
npm install packagename

# 安装指定版本的模块
npm install packagename 0.0.1

# --global, -g, 安装全局的模块
npm install packagename -g

# list, ll, ls, la, 查看已安装的模块
npm list

# 生成package.json文件
npm init

# --save, -S, 把模块的版本信息保存到dependencies
# (生产环境依赖)中，即package.json文件的dependencies字段
npm install packagename --save

# --save-dev, -D, 把模块版本信息保存到devDependencies
# (开发环境依赖)中，即package.json文件的devDependencies字段
npm install packagename --save-dev

# --save-optional, -O, 把模块安装到optionalDependencies
# (可选环境依赖)中，即package.json文件的optionalDependencies字段
npm install packagename --save-optional

# --save-exact, -E, 精确地安装指定版本的模块
npm install packagename --save-exact
```

## nrm, npm源管理器

```
# 安装
npm install -g nrm

# 验证
nrm --version

# 列出可选择的源
nrm ls

# 切换使用的源
nrm use npm

# 添加一个源
nrm add company http://npm.company.com/

# 删除一个源
nrm del company

# 测试源速度
nrm test npm  # 测试单个源
nrm test  # 测试所有源

# 访问源主页
nrm home taobao
```

不使用nrm时：
```
# 查看当前使用的源
npm config get registry

# 设置一个源
npm config set registry https://registry.npm.taobao.org/

# 安装包时指定源
npm install --registry=https://registry.npm.taobao.org
npm i logo --registry=https://registry.npm.taobao.org
```

## nvm, 版本管理

```
# 启用版本管理
nvm on
# 关闭版本管理
nvm off
# 查看可以下载的版本
nvm list available
# 查看可以使用的版本
nvm list
# 装指定版本
nvm install 12.18.0
# 启用特定版本
nvm use 4.4.0
# 卸载
nvm uninstall 12.18.0
# 设置node mirror
nvm node_mirror https://npm.taobao.org/mirrors/node/
export NVM_NODEJS_ORG_MIRROR=https://npm.taobao.org/mirrors/node/
# 设置npm mirror
nvm npm_mirror https://npm.taobao.org/mirrors/npm/
export NVM_NPM_MIRROR=https://npm.taobao.org/mirrors/npm/
```
