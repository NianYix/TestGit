import pandas as pd
import numpy as np

# print( pd.__version__)

# df = pd.read_csv('data/table.csv')
# print(df.head())

# df_txt = pd.read_table('data/table.txt') #可设置sep分隔符参数
# print(df_txt)
# df_txt

#需要安装xlrd包
# df_excel = pd.read_excel('data/table.xlsx')
# print(df_excel.head())

# df.to_csv('data/new_table1.csv')
# df.to_csv('data/new_table666.csv', index=False) #保存时除去行索引

#需要安装openpyxl
# df.to_excel('data/new_table666.xlsx', sheet_name='Jerry')

# s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'],name='这是一个Series',dtype='float64')
# print(s)
# print('a:',s['a'])
# print(s.mean())

# print([attr for attr in dir(s) if not attr.startswith('_')])

# df = pd.DataFrame({'col1':list('abcde'),'col2':range(5,10),'col3':[1.3,2.5,3.6,4.6,5.8]},
#                  index=list('一二三四五'))
# print(df)
# print(df['col2'])
# print(type(df))
# print(df.rename(index={'一':'one'},columns={'col2':'new_col2'}))
# print(df.index)
# print(df.columns)
# print(df.values)
# print(df.shape)

df1 = pd.DataFrame({'A':[1,2,3]},index=[1,2,3])
df2 = pd.DataFrame({'A':[1,2,3]},index=[3,1,2])

