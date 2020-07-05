#利用python导入数据库 python--excel--SQL
import pandas as pd
from sqlalchemy import create_engine
engine=create_engine('mysql+pymysql://root:123456@localhost/chendan')
df=pd.read_excel("D:/chendan/123.xlsx",sheet_name="Sheet1")#路径最好手输入
df.to_sql(name="ff",con=engine)
sqldata=pd.read_sql_table('ff',engine)
print(sqldata)

#利用python从数据库导出文件 python--SQL--excel
import pandas as pd
from sqlalchemy import create_engine
engine=create_engine('mysql+pymysql://root:123456@localhost/chendan')
df=pd.read_sql_table('ff',engine)
df.to_excel('D:/chendan/123.xlsx')
sqldata=pd.read_excel('D:/chendan/123.xlsx')
print(sqldata)
#python写入excel(xlswriter)--生成图表
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/chendan'
