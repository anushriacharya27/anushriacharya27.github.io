#a=["delhi","bangalore","chennai","mumbai"]
#from sklearn.preprocessing import LabelEncoder
#lEncoder=LabelEncoder()
#lEncoder.fit(a)
#b=lEncoder.transform(a)
#c=["chennai"]
#lEncoder.fit(c)
#lEncoder.transform(c)
#lEncoder.inverse_transform([1])

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("50_Startups.csv")
data.columns
x=data.iloc[:,:4].values
y=data.iloc[:,4].values

from sklearn.preprocessing import LabelEncoder
lEncoder=LabelEncoder()
x[:,3]=lEncoder.fit_transform(x[:,3])

from sklearn.preprocessing import OneHotEncoder
ohEncoder=OneHotEncoder(categorical_features=[3])
x=ohEncoder.fit_transform(x).toarray()
x=x[:,1:]
a=["california","florida","newyork"]
from sklearn.preprocessing import LabelEncoder
lEncoder=LabelEncoder()
lEncoder.fit(a)
b=lEncoder.transform(a)
