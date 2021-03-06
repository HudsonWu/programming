# rvm, Ruby Version Manager

RVM能在系统中安装和管理多个Ruby版本, 同时还能管理不同的gem集

1. 安装RVM
```
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
curl -sSL https://get.rvm.io | bash -s stable
source ~/.bashrc
source ~/.bash_profile  //载入RVM环境
rvm -v  //检查是否安装正确
echo "ruby_url=https://cache.ruby-china.com/pub/ruby" ~/.rvm/user/db  //修改ruby安装源
```

2. 用RVM安装Ruby环境
```
rvm list known  //列出已知的ruby版本
rvm install 2.4.2  //安装2.4.2版本
```

3. rvm常用命令
```
rvm list  //查询已经安装的ruby
rvm remove 1.9.2  //卸载一个已经安装的版本
rvm 2.0.0 --default  //将指定版本的Ruby设置为默认版本
```

4. Rails
```
gem install rails
rails -v
gem install bundler  //安装bundler
```

5. 替换源为ruby-china
```
gem source -r https://rubygems.org/
gem source -a https://gems.ruby-china.com/
gem source -l  //验证是否替换成功
bundle config mirror https://rubygems.org https://gems.ruby-china.com
```

6. gemset的使用

gemset可以理解为一个独立的Gem环境, 每一个gemset都是相互独立的

gemset是附加在ruby语言版本下面的

```
//建立gemset
rvm use 1.8.7
rvm gemset create rails23
//切换语言或者gemset
rvm use 1.8.7
rvm use 1.8.7@rails23
//列出当前gemset
rvm gemset list
//清空gemset中的Gem
rvm gemset empty 1.8.7@rails23
//删除一个gemset
rvm gemset delete rails2-3
```

7. 部署多个ruby版本, 项目自动加载gemset
```
rvm install 2.0.0
rvm use 2.0.0
rvm gemset create rails416
rvm use 2.0.0@rails416
```
进入到项目目录, 建立一个.rvmrc文件:
```
rvm use 2.0.0@rails416
```

8. 卸载rvm
```
rvm implode
```
或者创建脚本文件:
```
/usr/bin/sudo rm -rf $HOME/.rvm $HOME/.rvmrc /etc/rvmrc /etc/profile.d/rvm.sh /usr/local/rvm /usr/local/bin/rvm
/usr/bin/sudo /usr/sbin/groupdel rvm
/bin/echo "RVM is removed. Please check all .bashrc|.bash_profile|.profile|.zshrc for RVM source lines and delete
or comment out if this was a Per-User installation."
```
