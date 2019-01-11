#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import pymysql

# contracts projects
# tasks tasks_department tasks_executor
# reports report_editions 
# archives
# user_message_groups  user_message_groups_has_user 
# project_task_list

def mysql_connect(mysql_passwd, mysql_host="127.0.0.1", mysql_port=3306, mysql_user="root", mysql_db="parallel"):
    # 创建数据库连接
    conn = pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, \
                           password=mysql_passwd, db=mysql_db, charset='utf8')
    return conn
    

conn = mysql_connect(mysql_passwd="yfyunmysql")

# 创建游标
cur = conn.cursor()
    
def get_contract_id(condition):
    sql = "select id from contracts where contract_number like '%{}%'".format(condition)
    try:
        contract_nums = cur.execute(sql)
        print("共匹配到合同 %s 个" % (contract_nums))
        contracts = []
        for result in cur:
            contracts.append(result[0])
        return tuple(contracts)
    except:
        print("Error: Unable to fetch datas")

def get_project_id(contracts):
    sql = "select id from projects where contract_id in {}".format(contracts)
    try:
        project_nums = cur.execute(sql)
        print("共匹配到项目 %s 个" % (project_nums))
        projects = []
        for result in cur:
            projects.append(result[0])
        return tuple(projects)
    except:
        print("Error: Unable to fetch datas")

def get_table_id(table, projects):
    sql = "select id from {} where project_id in {}".format(table, projects)
    try:
        data_nums = cur.execute(sql)
        print("共匹配到%s %s 个" % (table, data_nums))
        datas = []
        for result in cur:
            datas.append(result[0])
        return tuple(datas)
    except:
        print("Error: Unable to fetch datas")

def delete_table_datas(table, column, datas):
    print("删除%s表中%s列在 %s范围内的数据" % (datas,))
    sql = "delete from {} where {} in {}".format(table, column, datas)
    try:
        data_nums = cur.execute(sql)
        conn.commit()
        print("共删除%s条数据" % (data_nums))
    except:
        conn.rollback()
        print("Error: Unable to delete datas")
    
contracts = get_contract_id("18")
projects = get_project_id(contracts)
tasks = get_table_id("tasks", projects)
reports = get_table_id("reports", projects)
user_message_groups = get_table_id("get_table_id", projects)

# 删除表数据
delete_table_datas("user_message_groups_has_user", "group_id", user_message_groups)
delete_table_datas("user_message_groups", "project_id", projects)
delete_table_datas("tasks_department", "task_id", tasks)
delete_table_datas("tasks_executor", "task_id", tasks)
delete_table_datas("report_editions", "report_id", reports)
delete_table_datas("archives", "project_id", projects)
delete_table_datas("project_task_list", "project_id", projects)


if contract_nums < 50:
    print_column(cur, table1, "id", contracts, "contract_number")


cur.close()
conn.close()
