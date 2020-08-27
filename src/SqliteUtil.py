import sqlite3

conn = None
cursor = None

# 在未连接之前,先创建一个表,用于存放数据
def creat_table():
    global conn
    if conn == None:
        conn = sqlite3.connect('test.db')
        global cursor
        cursor = conn.cursor()
        cursor.execute('create table if not exists block(id varchar(20) primary key,name varchar(20))')
    return cursor,conn

# 关闭资源
def close_sources():
    if cursor != None:
        cursor.close()
    if conn != None:
        conn.close()


