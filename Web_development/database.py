#import mysql.connector as mc
#mc.connect(host='localhost',user='root',password='1234567')

import sqlite3
conn = sqlite3.connect("userdata.db")
create_table_query = """
create table userrecord (name varchar(25),age integer,address varchar(25),college varchar(25),branch varchar(25),roll_no integer,query_sub varchar(60))
"""

cur = conn.cursor()
cur.execute(create_table_query)

print("you have successfully created table in database!")

cur.close
conn.close