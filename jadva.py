import numpy as np
import pandas as pd
import requests as rq

df=pd.read_csv('people.csv')
# permunation=np.random.permutation(15)
# a=df.take(permunation)
sample=df.sample(10)
print(sample)
