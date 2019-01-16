# httplib2

Python3自带两个用于和HTTP web服务交互的标准库(内置模块):
+ http.client, HTTP协议的底层库
+ urllib.request, 创建在http.client之上的一个抽象层, 它为访问HTTP和FTP服务器提供一个标准的API, 
                  可以自动跟随HTTP重定向并处理一些常见形式的HTTP认证

httplib2是一个第三方的开源库. 它比python3中的http.client更完整的实现了HTTP协议, 同时比urllib.request提供了更好的抽象. 

## Simple Retrieval

```python
import httplib2
h = httplib2.Http('.cache')
resp, content = h.request('http://example.org/', 'GET')
```

## Authentication

```python
import httplib2
h = httplib2.Http('.cahce')
h.add_credentials('name', 'password')
resp, content = h.request('http://example.org/chap/2',  # ssl+base认证
    "PUT", body='This is text',
    headers={'content-type': 'text/plain'})
```

## Cache-Control

```python
import httplib2
h = httplib2.Http('.cache')
resp, content = h.request('http://bitworking.org/') # 请求被缓存, 下次会用到这个缓存而不去发送新的请求
...
resp, content = h.request('http://bitworking.org/',
    headers={'cache-control': 'no-cache'})  # 设置不用缓存
```

## Forms

```python
from httplib2 import Http
from urllib import urlencode
h = Http()
data = dict(name='Joe', comment='A test comment')
resp, content = h.request('http://bitworking.org/news/223/Meet-Ares', 'POST', urlencode(data))
```

## Cookies

```python
import urllib
import httplib2

http = httplib2.Http()

url = 'http://www.example.com/login'
body = {'USERNAME': 'foo', 'PASSWORD': 'bar'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))

headers = {'Cookie': response['set-cookie']}    # 将获得的cookie设置到请求头, 以备下次使用

url = 'http://www.example.com/home'
response, content = http.request(url, 'GET', headers=headers)
```

## Proxies

```python
import httplib2
import socks

httplib2.debuglevel = 4
h = httplib2.Http(proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, 'localhost', 8000))
r, c = h.request('http://bitworking.org/news/')
```

## Http对象的构造方法

```
__init__(self, cache=None, timeout=None, proxy_info=None, ca_certs=None, disable_ssl_certificate_validation=False)  

    proxy_info 的值是一个 ProxyInfo instance.  
    
    cache:   
    存放cache的位置, 要么为字符串, 要么为支持文件缓存接口的对象  
    
    timeout:   
    超时时间, 默认时会取python对socket链接超时的值  
    
    ca_certs:   
    一个用于ssl服务器认证用的包涵了主CA认证的文件路径, 默认会使用httplib2绑定的证书  
    
    disable_ssl_certificate_validation:   
    确定是否进行ssl认证  
    

add_certificate(self, key, cert, domain)  
添加一个ssl认证key和文件  

add_credentials(self, name, password, domain='')  
添加一个用户名, 密码信息  

clear_credentials(self)  
删除掉所有的用户名, 密码信息, 貌似还是可以存多个用户名和密码  


Http.request(self, uri, method='GET', body=None, headers=None, redirections=5, connection_type=None)  
执行单次的http请求  

    uri:   
    一个以'http' 或 'https'开头的资源定位符字串, 必须是一个绝对的地址  
    
    method:   
    支持所有的http请求方式. 如:  GET, POST, DELETE, etc..  
    
    body:   
    请求的附件数据, 一个经过urllib.urlencode编码的字符串  
    
    headers:   
    请求头信息, 一个字典对象  
    
    redirections:   
    最大的自动连续的重定向次数默认为5  
    
    返回:   
    (response, content)元组, response是一个httplib2.Response对象, content就是包含网页源码的字符串  


httplib2.Response对象  
其实就是一个包含所有头信息的字典, 因为它本身就是集成自字典对象的  
```

