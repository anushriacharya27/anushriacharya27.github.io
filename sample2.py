import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("headbrain.csv")
x=data.iloc[:,2].values
y=data.iloc[:,3].values
xmean=np.mean(x)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
ymean=np.mean(y)
upper=0
lower=0
for i in range(0,len(x)):
    upper=upper+((x[i]-xmean)*(y[i]-ymean)) 
    lower=lower+((x[i]-xmean)**2)
b1=upper/lower
print(b1)
b0=ymean-(b1*xmean)
print(b0)
x1=data.iloc[:,2:3]
from sklearn.linear_model import LinearRegression   #it is a class
regressor=LinearRegression()
regressor.fit(x1,y)
m=regressor.coef_
c=regressor.intercept_
print(m)
print(c)