
from pandas import Series,DataFrame

data={
    "name":["ss","dd","ss"],
    "sex":["famale","male","male"],
    "year":[2001,2002,2022]
}
df=DataFrame(data)
print(df)
data1=[{"name":"ss","sex":"famale", "year":2001},
    {"name": "dd", "sex": "male", "year": 2002}]

df1=DataFrame(data1)
print(df1)