import pandas as pd
import quandl,math, datetime
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

quandl.ApiConfig.api_key="8TwE1AABp1Ssx-Yx-Dnj"
df = quandl.get('DCE/JDK2019')
df=df[['Open','High','Low','Close','Volume']]
df['HL_PCT']=(df['High']-df['Close'])/df['Close']*100.0
df['PCT_change']=(df['Close']-df['Open'])/df['Open']*100.0

df=df[['Close','HL_PCT','PCT_change','Volume']]

forecast_col='Close'
df.fillna(value=-99999, inplace=True)

forecast_out=int(math.ceil(0.01*len(df)))
#print(forecast_out)

df['label']=df[forecast_col].shift(-forecast_out)



x=np.array(df.drop(['label'],1))
x=preprocessing.scale(x)
x_lately=x[-forecast_out:]
x=x[:-forecast_out]


df.dropna(inplace=True)
y=np.array(df['label'])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

clf= LinearRegression(n_jobs=-1)
clf.fit(x_train,y_train)

accuracy=clf.score(x_test,y_test)

#print(accuracy)

forecast_set=clf.predict(x_lately)
#print(forecast_set,accuracy,forecast_out)

df['Forecast']=np.nan

last_date=df.iloc[-1].name
last_unix = last_date.timestamp()
one_day=86400
next_unix=last_unix+one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date]=[np.nan for _ in range(len(df.columns)-1)]+[i]

print(df.tail())

df['Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()