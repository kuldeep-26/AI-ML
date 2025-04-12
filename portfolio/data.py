#import mysql.connector as mc
#mc.connect(host='localhost',user='root',password='1234567')

import sqlite3
conn = sqlite3.connect("usercontact.db")
create_table_query = """
create table userrecord (name varchar(25),email varchar(35),message varchar(120))
"""

cur = conn.cursor()
cur.execute(create_table_query)

print("you have successfully created table in database!")

cur.close
conn.close