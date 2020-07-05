import cx_Oracle as orcl
import pandas as pd
from sqlalchemy import create_engine

# 数据库连接
db = create_engine('oracle://C##KING:1223456@192.168.1.150:1521/orcl')
data=pd.read_sql_table("test1",con=db)
print(data)