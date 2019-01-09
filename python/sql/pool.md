# pymysql连接池

使用pymysql创建一个conn对象的时候, 就已经和mysql之间创建了一个tcp的长连接, 只要不调用这个对象的close方法, 这个长连接就不会断开, 这样, 我们创建了一组conn对象, 并将这些conn对象放到队列里, 这个队列就是一个连接池

```python
import pymysql
import time

start = time.time()

conn = pymysql.connect(host="192.168.0.127", \
                             port=3306, \
                             user='root', \
                             password='strongpasswd', \
                             database='db_name', \
                             charset='utf8')
conn.autocommit(True)   # 设置自动commit

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) # 设置返回的结果集用字典来表示, 默认是元组

data = (('male', i, 'john%s' %i) for i in range(1000000))   # 伪造数据, data是一个生成器

cursor.executemany("insert into tb1(gender, class_id, sname) values(%s, %s, %s)", data) # 可以使用executemany执行多条sql

# conn.commit()
cursor.close()
conn.close()

print("total time:", time.time()-start)
```

使用queue为pymysql提供一个连接池, 减少多次创建实例的开销
```python
pool = ConnectionPool(
    # maxsize=100, maxsize 用于指定最大连接数, 非必须
    host="localhost",
    port=3306,
    user="test_user",
    passwd="test_passwd",
    db="test_db"
)
pool.execute("select * from test")
```
