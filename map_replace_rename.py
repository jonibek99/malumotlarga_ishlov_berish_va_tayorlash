import pandas as pd
import numpy as np
import requests as rq
# # map
df=pd.read_csv('cars.csv')
# a=2
# print(df.map(lambda x: x*a))
##replace
# a='kor_farmondagi'
# replace=df.replace('used',a)
# print(replace)
#rename
df.rename(columns={'model':'models','year':'solo'},inplace=True)
print(df)