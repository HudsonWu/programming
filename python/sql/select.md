# 查询

## 遍历mysql表中数据

mysql表中存在几千到几亿的数据(不存在自增主键), 需要对表中数据进行遍历

### 方案1

使用`limit`来分块返回数据

劣势: 每次都要从头扫描数据表, 在数据量超过100w时, 性能较低

```python
LIMIT = 5000

def get_name(sql_client, table_name):
    i = 0
    while True:
        sql.ping()
        cur = sql.cursor()

        sql_cmd = 'select did from {} limit {}, {}'.format(table_name, i * LIMIT, LIMIT)

        rt = cur.execute(sql_cmd)
        rt_list = cur.fetchall()
        cur.close()

        yield [rt_tuple[0] for rt_tuple in rt_list]

        if rt < LIMIT:
            yield 0

        i += 1
```

### 方案2

使用流式游标`SSCursor`, 流式游标将执行结果卡在网络缓冲区, 当网络缓冲区堆满时, mysql将查询暂停, 当网络缓存区有位置时, 将会在上次暂停的地方继续读取

```python
def mysql_connect():
    mysql_client = pymysql.connect(**SQL_CONFIG)
    cur = mysql_client.cursor()
    # 设置超时时间
    cur.execute('set session net_write_timeout = 800')
    cur.close()
    return mysql_client

def get_name(mysql_client, table_name):
    sscur = mysql_client.cursor(pymysql.cursors.SSCursor)
    sscur.execute('select name from {}'.format(table_name))
    i = 0
    for name in sscur:
        i +=1
        yield i, name[0]

    mysql_client.commit()
    sscur.close()
    yield i, 0
```

1. 当数据较多时, mysql不能在默认的`net_write_timeout`的时间将数据全部发送到客户端, 程序会抛出`error2013, "Lost connection to MySQL server during query"`异常, 所以修改mysql会话级别的`net_write_timeout`时间, 具体数值根据业务处理时间设置
2. 当会话正在返回数据的时候不能再对数据库进行其他操作, 程序会发出警告`warnings.warn("Previous unbuffered result was left incomplete")`, 并且会伴随着查询数据返回出问题, 如果此时还需要同时对数据库进行操作, 需另外创建会话

