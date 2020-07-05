#二维数组类似于excel表格，列表list=[1,2,3]
#字典dirctory={"姓名":["琳达","贾丽莉"],"性别":["男","女"]}

import pandas as pd
table1=pd.DataFrame([[1001,1],[1002,2],[1003,3],[1004,4]],
                    columns=['科目代码','金额'],
                    index=[1,2,3,4]
                                )
print(table1)

table2=pd.DataFrame({"姓名":["琳达","贾丽莉"],"性别":["男","女"]},index=[1,2])
print(table2)
print(table2.columns)
print(table2.index)