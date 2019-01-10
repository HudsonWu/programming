#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import pymysql

# contracts projects
# tasks tasks_department tasks_executor
# reports report_editions 
# archives
# user_message_groups  user_message_groups_has_user 
# project_task_list

condition = "18"
table1 = "contracts"
table2 = "projects"
table2_1 = "tasks"
table2_1_1 = "tasks_department"
table2_1_2 = "tasks_executor"
table2_2 = "reports"
table2_2_1 = "report_editions"
table2_3 = "archives"
table2_4 = "user_message_groups"
table2_4_1 = "user_message_groups_has_user"
table2_5 = "project_task_list"

def mysql_connect(mysql_passwd, mysql_host="127.0.0.1", mysql_port=3306, mysql_user="root", mysql_db="parallel"):
    # 创建数据库连接
    conn = pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, \
                           password=mysql_passwd, db=mysql_db, charset='utf8')
    return conn
    
def get_contract_id():
    sql = "select id from {} where contract_number like '%{}%'".format(table1, condition)
    contract_nums = cur.execute(get_contract_id)
    print("共匹配到合同 %s 个" % (contract_nums))
    contracts = []
    for result in cur:
        contracts.append(result[0])
    return contracts

    
conn = mysql_connect(mysql_passwd="yfyunmysql")

# 创建游标
cur = conn.cursor()
    


contracts = to_list(datas)

if contract_nums < 50:
    print_column(cur, table1, "id", contracts, "contract_number")


cur.close()
