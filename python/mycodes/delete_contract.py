#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# contracts projects
# tasks tasks_department tasks_executor external_tasks
# reports report_editions 
# archives
# performances
# archives_apply
# project_files
# user_message_groups  user_message_group_has_user 
# project_task_list

import pymysql
import os.path
import traceback

def print_help():
    fn = os.path.basename(__file__)
    print('\n'
          'Usage:\n'
          ' $ python3 {} "your-matching-text"     # (1)\n'.format(fn) +
          ' $ python3 {} -l "your-matching-text"  # (2)\n'.format(fn) +
          ' $ python3 {} -d "your-matching-text"  # (2)\n'.format(fn) +
          '\n\n'
          '(1) List matching counts.\n'
          '(2) List contracts_numbers where contract_number like the your-matching-text.\n'
          '(3) Delete contracts where contract_number like the your-matching-text'
          '\n')

        
def mysql_connect(mysql_passwd, mysql_host="127.0.0.1", mysql_port=3306, mysql_user="root", mysql_db="parallel"):
    # 创建数据库连接
    conn = pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, \
                           password=mysql_passwd, db=mysql_db, charset='utf8')
    return conn
    

def get_contract_id(condition):
    sql = "select id from contracts where contract_number like '%{}%'".format(condition)
    try:
        contract_nums = cur.execute(sql)
        if contract_nums == 0:
            print("匹配到的合同数目为0")
            return ()
        print("共匹配到合同 %s 个" % (contract_nums))
        contracts = []
        for result in cur:
            contracts.append(result[0])
        return tuple(contracts)
    except Exception:
        traceback.print_exec()
        print("Error: Unable to fetch datas (get_contract_id)")

def get_project_id(contracts):
    if len(contracts) == 1:
        sql = "select id from projects where contract_id = {}".format(contracts[0])
    else:
        sql = "select id from projects where contract_id in {}".format(contracts)
    try:
        project_nums = cur.execute(sql)
        if project_nums == 0:
            print("匹配到的项目数目为0")
            return ()
        print("共匹配到项目 %s 个" % (project_nums))
        projects = []
        for result in cur:
            projects.append(result[0])
        return tuple(projects)
    except Exception:
        traceback.print_exec()
        print("Error: Unable to fetch datas (get_project_id)")

def get_table_id(table, projects):
    if len(projects) == 1:
        sql = "select id from {} where project_id = {}".format(table, projects[0])
    else:
        sql = "select id from {} where project_id in {}".format(table, projects)
    try:
        data_nums = cur.execute(sql)
        if data_nums == 0:
            print("%s表匹配为空" % (table))
            return ()
        print("共匹配到%s表%s条数据" % (table, data_nums))
        datas = []
        for result in cur:
            datas.append(result[0])
        return tuple(datas)
    except Exception:
        traceback.print_exec()
        print("Error: Unable to fetch datas (get_table_id)")

def print_contracts_numbers(contracts):
    print("\n下面是匹配到的合同的合同编号:")
    print("----------")
    if len(contracts) == 1:
        sql = "select contract_number from contracts where id = {}".format(contracts[0])
    else:
        sql = "select contract_number from contracts where id in {}".format(contracts)
    try:
        cur.execute(sql)
        i = 0
        for contract_number in cur:
            i += 1
            if i % 3 == 0:
                print(contract_number[0])
            else:
                print(contract_number[0], end='  ')
        print("\n----------")
    except Exception:
        traceback.print_exec()
        print("Error: Unable to print datas (print_contracts_numbers)")


def delete_table_datas(table, column, datas):
    print("删除%s表中%s列在以下范围内的数据:\n %s" % (table, column, str(datas)))
    if len(datas) == 1:
        sql = "delete from {} where {} = {}".format(table, column, datas[0])
    else:
        sql = "delete from {} where {} in {}".format(table, column, datas)
    try:
        data_nums = cur.execute(sql)
        conn.commit()
        print("共删除%s条数据" % (data_nums))
    except Exception:
        traceback.print_exec()
        conn.rollback()
        print("Error: Unable to delete datas (delete_table_datas)")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) == 1:
        print_help()
    elif (len(sys.argv) in (2, 3)):
        if len(sys.argv) == 2:
            condition = sys.argv[1]
        else:
            condition = sys.argv[2]

        conn = mysql_connect(mysql_passwd="yfyunmysql")
        # 创建游标
        cur = conn.cursor()
        
        contracts = get_contract_id(condition)
        if len(contracts) == 0:
            raise SystemExit('匹配到的合同为空')
        
        projects = get_project_id(contracts)
        if len(projects) != 0:
            tasks = get_table_id("tasks", projects)
            reports = get_table_id("reports", projects)
            user_message_groups = get_table_id("user_message_groups", projects)
            
        if (len(sys.argv) == 3 and sys.argv[1] == '-d'):
            # 删除表数据
            if len(projects) != 0:
                if len(user_message_groups) != 0:
                    delete_table_datas("user_message_group_has_user", "group_id", user_message_groups)
                    delete_table_datas("user_message_groups", "id", user_message_groups)
                if len(tasks) != 0:
                    delete_table_datas("tasks_department", "task_id", tasks)
                    delete_table_datas("tasks_executor", "task_id", tasks)
                    delete_table_datas("external_tasks", "task_id", tasks)
                    delete_table_datas("tasks", "id", tasks)
                if len(reports) != 0:
                    delete_table_datas("report_editions", "report_id", reports)
                    delete_table_datas("reports", "id", reports)
                delete_table_datas("archives", "project_id", projects)
                delete_table_datas("performances", "project_id", projects)
                delete_table_datas("archives_apply", "project_id", projects)
                delete_table_datas("project_files", "project_id", projects)
                delete_table_datas("project_task_list", "project_id", projects)
                delete_table_datas("projects", "id", projects)
            delete_table_datas("contracts", "id", contracts)
        elif (len(sys.argv) == 3 and sys.argv[1] == '-l'):
            print_contracts_numbers(contracts)
        else:
            pass
        cur.close()
        conn.close()
    else:
        print_help()
