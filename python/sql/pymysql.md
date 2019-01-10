# pymysql

使用Python进行MySQL的库主要有三个, Python-MySQL(更熟悉的名字可能是MySQLdb), PyMySQL和SQLAlchemy. 

Python-MySQL资格最老, 核心由C语言打造, 接口精炼, 性能最棒, 缺点是环境依赖较多, 安装复杂, 近两年已停止更新, 只支持Python2, 不支持Python3. 

SQLAlchemy是一个ORM框架, 它并不提供底层的数据库操作, 而是要借助于MySQLdb、PyMySQL等第三方库来完成, 目前SQLAlchemy在Web编程领域应用广泛

PyMySQL为替代Python-MySQL而生, 纯python打造, 接口与Python-MySQL兼容, 安装方便, 支持Python3. 

pymysql是一个纯python实现的mysql客户端操作库, 支持事务, 存储过程, 批量执行等

pymysql遵循python数据库API v2.0规范, 并包含了pure-Python Mysql 客户端库

## 安装和导入

```sh
//简单的方式安装
pip3 install pymysql

//tar包安装
pip3 install pymysql-x.x.x.tar.gz

//源代码安装
git clone https://github.com/PyMySQL/PyMySQL
cd PyMySQL/
python3 setup.py install

//指定版本号, x.x为版本号
curl -L https://github.com/PyMySQL/PyMySQL/tarball/pymysql-x.x | tar xz
cd PyMySQL*
python3 setup.py install

//导入
import pymysql
```

## 游标

游标 (Cursor), 是处理数据的一种方法, 为了查看或者处理结果集中的数据, 游标提供了在结果集中一次一行或者多行前进或向后浏览数据的能力, 可以把游标当作一个指针, 它可以指定结果中的任何位置, 然后允许用户对指定位置的数据进行处理

通俗来说, 操作数据和获取数据库结果都要通过游标来操作

### 设置游标类型

+ Cursor, 默认, 元组类型
+ DictCursor, 字典类型
+ DictCursorMixin, 支持自定义的游标类型, 需先自定义才可使用
+ SSCursor, 无缓冲元组类型
+ SSDictCursor, 无缓冲字典类型

```
//指定为字典类型
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

//对于大数据通常使用sscursor方法来操作, 它相当于一个迭代器, 
//每次只取一条, 并且使用fetchone时, 取完一条后再取下一条
cur = conn.cursor(pymysql.cursors.SSCursor)
```

### 游标控制

所有数据查询操作均基于游标, 通过cur.scroll(num, mode)控制游标的位置
```python
cur.scroll(1, mode='relative')   # 相对当前位置移动
cur.scroll(2, mode='absolute')   # 相对绝对位置移动
```

### 游标的方法和属性

1. execute(sql, args), 执行单条sql
2. fetchall(), 取所有结果, 就是获得执行sql语句后的结果
3. fetchone(), 得到结果集的下一行
4. executemany(sql, args), 批量执行sql

```python
cur.fetchone()   # 获取单条数据
cur.fetchmany(3) # 获取N条数据
cur.fetchall()   # 获取所有数据
```

```
//rowcount, 只读属性, 执行execute()方法后影响的行数
effect_row = cur.execute(sql_str)
cur.rowcount

//lastrowid, 获取自增id
cur.lastrowid
```

## 事务处理

+ 开启事务, `conn.begin()`
+ 提交修改, `conn.commit()`
+ 回滚事务, `conn.rollback()`

## 防止sql注入

+ 转义特殊字符, `conn.escape_string(str)`
+ 参数化语句, 支持传入参数进行自动转义、格式化sql语句, 以避免sql注入等安全问题

```python
# 插入数据(元组或列表)
effect_row = cur.execute('INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))

# 插入数据(字典)
info = {'name': 'fake', 'age': 15}
effect_row = cur.execute('INSERT INTO `users` (`name`, `age`) VALUES (%(name)s, %(age)s)', info)

# 批量插入
effect_row = cur.executemany(
    'INSERT INTO `users` (`name`, `age`) VALUES (%s, %s) ON DUPLICATE KEY UPDATE age=VALUES(age)', [
        ('hello', 13),
        ('fake', 28),
    ])
```

## 连接

```python
def connect_db():
    return pymysql.connect(host='10.123.5.28',
                           port=3306,
                           user='root',
                           password='strongpasswd',
                           database='db_name',
                           charset='utf8')
```

## 查询

```python
def query_country_name(cc2):
    sql_str = ("SELECT Fcountry_name_zh"
               + " FROM t_country_code"
               + " WHERE Fcountry_2code='%s'" % (cc2))"
    logging.info(sql_str)

    conn = mysql_api.connect_db()
    cur = conn.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close() # 关闭游标
    conn.close() # 关闭连接

    assert len(rows) == 1, 'Fatal error: country_code does not exists!'
    return rows[0][0]
```

## 插入

1. 简单插入
```python
def insert_file_rec(self, file_name, file_md5):
        conn = mysql_api.connect_db()
        cur = conn.cursor()
        try:
            sql_str = ("INSERT INTO t_forward_file (Ffile_name, Ffile_md5)", 
                       + " VALUES ('%s', '%s')" % (file_name, file_md5))
            cur.execute(sql_str)
            conn.commit()
        except:
            conn.rollback()
            logging.exception('Insert operation error')
            raise
        finally:
            cur.close()
            conn.close()
```

2. 批量插入
```python
remit_ids = [('1234', 'CAD'), ('5678', 'HKD')]

conn = mysql_api.connect_db()
        cur = conn.cursor()
        try:
                cur.executemany("INSERT INTO t_order (Fremit_id, Fcur_type, Fcreate_time)"
                                                + " VALUES (%s, %s, now())", new_items)
                assert cur.rowcount == len(remit_ids), 'my error message'
                conn.commit()
        except Exception as e:
                conn.rollback()
                logging.exception('Insert operation error')
        finally:
                cur.close()
                conn.close()
```

## 更新

```python
 def update_refund_trans(self, remit_id):
        conn = mysql_api.connect_db()
        cur = conn.cursor()
        try:
            sql_str = ("SELECT Fremit_id"
                       + " FROM t_wxrefund_trans"
                       + " WHERE Fremit_id='%s'" % remit_id
                       + " FOR UPDATE")
            logging.info(sql_str)

            cur.execute(sql_str)
            assert cur.rowcount == 1, 'Fatal error: The wx-refund record be deleted!'

            sql_str = ("UPDATE t_wxrefund_trans"
                        + " SET Fcheck_amount_flag=1"
                        + ", Fmodify_time=now()"
                        + " WHERE Fremit_id='%s'" % remit_id
            logging.info(sql_str)
            cur.execute(sql_str)

            assert cur.rowcount == 1, 'The number of affected rows not equal to 1'
            conn.commit()
        except:
            conn.rollback()
            logging.exception('Update operation error')
            raise
        finally:
            cur.close()
            conn.close()
```

