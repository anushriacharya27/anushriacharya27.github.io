import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("headbrain.csv")
x=data.iloc[:,2].values
y=data.iloc[:,3].values
#xmean=np.mean(x)   
from sklearn.linear_model import LinearRegression   #it is a class
regressor=LinearRegression()
regressor.fit(x1,y)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
ymean=np.mean(y)
for i in range(0,len(x)):
    sst=sst+((y[i]-ymean)**2) 
    ssr=ssr+((y[i]-)


x1=data.iloc[:,2:3]

m=regressor.coef_
c=regressor.intercept_
print(m)
print(c)
