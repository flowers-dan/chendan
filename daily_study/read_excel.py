#读取excel表--read_excel
#sheet_name=0,表示传入Sheet的顺序，从0开始
#sheet_name='学习目录',表示传入名称为学习目录的sheet表
#usecols=[2,5，6],2代表要传入第2列，第5列，第6列
#主要原因是我们复制路径时带着特殊字符，所以手动输入即可避免，同学们get到了吗？
import pandas as pd
a=pd.read_excel(r"C:\Users\91640\Desktop\学习表.xlsx",sheet_name=1,
                usecols=[2,3,5])
print(a)