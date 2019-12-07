#Emre Can Özkaya - 2149292

#There is an increasing trend between 300th and 400th day
#There is a stationary trend after 400th day


import pandas as pd
import numpy as np
import scipy as corr
import stats
import matplotlib.pyplot as plt 
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.api import Holt 
from statsmodels.tsa.stattools import adfuller

df_brazil = pd.read_csv("df_brazil.csv", usecols =["temp", "date"])
df_brazil=df_brazil.rename(columns = {"temp": "temp-brazil"})
temp_brazil=df_brazil.groupby("date").mean()


df_madrid=pd.read_csv("df_madrid.csv", usecols =["CET", "Mean TemperatureC"])
df_madrid=df_madrid.rename(columns = {"CET" : "date"})
df_madrid=df_madrid.rename(columns = {"Mean TemperatureC": "temp-madrid"})
 

df_final=pd.merge(df_madrid, temp_brazil, on = "date")
#print(df_final)

corr=df_final.corr(method = 'pearson')
#print(corr)

def decomp(frame,name,f,mod='Additive'):
    series = frame[name]
    array = np.asarray(series, dtype=float)
    result = sm.tsa.seasonal_decompose(array,freq=f,model=mod,two_sided=False)
   
    result.plot()
    plt.show() 
    return result


def test_stationarity(timeseries):
    #Determing rolling statistics
    rolmean = pd.Series(timeseries).rolling(window=12).mean()
    rolstd = pd.Series(timeseries).rolling(window=12).std()
    #Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    #Perform Dickey-Fuller test:
    print("Results of Dickey-Fuller Test:")
    array = np.asarray(timeseries, dtype='float')
    np.nan_to_num(array,copy=False)
    dftest = adfuller(array, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)



df_final=pd.merge(df_madrid, temp_brazil, how = "inner", on = "date")
seriesname = 'temp-brazil'


import warnings
warnings.filterwarnings("ignore")


series = df_final[seriesname]
test_stationarity(series)

result = decomp(df_final,seriesname,f=52)
test_stationarity(result.trend)
#test_stationarity(result.seasonal)