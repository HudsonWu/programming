#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import MySQLdb

def connectdb(db_host, db_username, db_passwd, db_database):
    print('连接到mysql服务器...')

    db = MySQLdb.connect(db_host, db_username, db_passwd, db_database, charset='utf-8')

    return db

def createtable():

# contracts projects
# tasks tasks_department tasks_executor
# reports report_editions 
# archives
# user_message_groups  user_message_groups_has_user 
# project_task_list
# https://blog.csdn.net/Oscer2016/article/details/70257024
# http://www.runoob.com/python/python-mysql.html

