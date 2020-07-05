#descrebe(),info(),head(),shape,fillna(0)
import pymysql
import pandas as pd
sql="select * from student"
conn=pymysql.connect(
    "localhost",
    "root",
    "123456",
    "chendan",
    charset="utf8"
)
pf=pd.read_sql(sql,conn)
print(pf)