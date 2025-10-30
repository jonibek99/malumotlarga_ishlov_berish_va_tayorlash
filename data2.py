import pandas as pd
import numpy as np
df=pd.read_csv('cars.csv')
df.fillna(0)
print(df)