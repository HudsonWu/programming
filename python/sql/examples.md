# pymysql操作实例

## 数据库连接

```python
#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行sql查询
cursor.execute("SELECT VERSION()")

# 使用fetchone()方法获取单条数据
data = cursor.fetchone()

print("Database version : %s" % data)

# 关闭数据库连接
db.close()
```

## 创建数据库表

```python

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

db.close()
```

## 数据库插入操作

```python

# sql插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
```

```python
//也可以使用这个sql插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES (%S, %S, %S, %S, %S )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
```

## 数据库查询操作

```python

sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)

try:
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s, lname=%s, age=%s, sex=%s, income=%s" % \
                (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

db.close()
```

## 数据库更新操作

```python
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%C'" % ('M')

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
```

## 删除操作

```python
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()
```

