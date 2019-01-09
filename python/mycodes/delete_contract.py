#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import pymysql

# 创建数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='yfyunmysql', db='parallel', charset='utf8')

# 创建游标
cursor = conn.cursor()

table1 = "contracts"
table2 = "projects"

contract_ids_sql = "select id from %s where contract_number like %s" % (table1, condition)
project_ids_sql = "select id from %s" % (table2)



# contracts projects
# tasks tasks_department tasks_executor
# reports report_editions 
# archives
# user_message_groups  user_message_groups_has_user 
# project_task_list

