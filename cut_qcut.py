import pandas as pd
import numpy as np
#df =pd.read_csv('country.csv')
#population = df.pop('Population')
# bins=[0,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000,10000000000000]
# groups=pd.cut(population,bins)
# df['group']=groups
# print(df)
##cut
# df=pd.read_csv('people.csv')
# age=df['Yoshi']
# mean=[0,20,40,120]
# cut=pd.cut(age,mean)
# labels=['yosh','urtacha,','katta']
# a=pd.cut(age,bins=mean,labels=labels)
# df['yosh_toifa']=a
# print(df)
##qcut
df=pd.read_csv('people.csv')
qcut=pd.qcut(df.Yoshi,3)
print(qcut)