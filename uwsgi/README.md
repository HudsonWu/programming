# uwsgi

uWSGI natively speaks HTTP, FastCGI, SCGI and its specific protocol named “uwsgi” (yes, wrong naming choice). The best performing protocol is obviously uwsgi, already supported by nginx and Cherokee (while various Apache modules are available).

```
# uwsgi协议
uwsgi --socket 127.0.0.1:3031 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

# http协议
uwsgi --http-socket 127.0.0.1:3031 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191

# django
uwsgi --socket 127.0.0.1:3031 --chdir /home/foobar/myproject/ --wsgi-file myproject/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191
```

```
# yourfile.ini
[uwsgi]
socket = 127.0.0.1:3031
chdir = /home/foobar/myproject/
wsgi-file = myproject/wsgi.py
processes = 4
threads = 2
stats = 127.0.0.1:9191
# uwsgi yourfile.ini
```

## 引用

+ [uwsgi文档](https://uwsgi-docs.readthedocs.io/en/latest/index.html)
+ [django-uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/index.html)
