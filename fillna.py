import pandas as pd
import numpy as np
import requests as rq
a=np.arange(1,10)
df=pd.read_csv('cars.csv')
#df.fillna({'mileage': 99,'price':"i'm king "},inplace=True)
# print(df.iloc[a].head(10))
df.fillna(method='ffill')
print(df)
