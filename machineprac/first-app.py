import pandas as pd
import quandl,math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

quandl.ApiConfig.api_key="8TwE1AABp1Ssx-Yx-Dnj"
df = quandl.get('DCE/JDK2019')
df=df[['Open','High','Low','Close','Volume']]
df['HL_PCT']=(df['High']-df['Close'])/df['Close']*100.0
df['PCT_change']=(df['Close']-df['Open'])/df['Open']*100.0

df=df[['Close','HL_PCT','PCT_change','Volume']]

forecast_col='Close'
df.fillna(-99999, inplace=True)

forecast_out=int(math.ceil(0.01*len(df)))
print(forecast_out)

df['label']=df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)


x=np.array(df.drop(['label'],1))
y=np.array(df['label'])
x=preprocessing.scale(x)
y=np.array(df['label'])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

clf= LinearRegression(n_jobs=-1)
clf.fit(x_train,y_train)

accuracy=clf.score(x_test,y_test)

print(accuracy)

