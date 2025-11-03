import pandas as pd
import numpy as np 
import requests as rq

df=pd.read_csv('cars.csv')
grouppy=df.groupby(['brand','price']).max(numeric_only=True).mean()
agg=df.groupby(['brand']).agg(['min','max'])
print(agg)