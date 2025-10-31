import pandas as pd
import numpy as np
import requests as rq
df=pd.read_csv('cars.csv')
duplicate=df.duplicated(['color']).sum()
drop_dublicates=df.drop_duplicates(['color']).sum()
print(duplicate)
print(drop_dublicates)