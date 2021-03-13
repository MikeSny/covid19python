from influxdb import InfluxDBClient
import matplotlib.pyplot as plt
import numpy
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
#import kaggle
import zipfile

api = KaggleApi()
api.authenticate()

api.dataset_download_file('antgoldbloom/covid19-data-from-john-hopkins-university','CONVENIENT_global_confirmed_cases.csv')                          
df = pd.read_csv('CONVENIENT_global_confirmed_cases.csv')
print (df)
total = df['South Africa'].sum()

df_sa = df['South Africa']
print(df_sa)
print ('Total ',total)
df_sa_21 = df['South Africa'].rolling(window=21).mean()
df_sa_7 = df['South Africa'].rolling(window=7).mean()
##df_sa_21 = df_sa_21.dropna() trying to remove the null values
length = df_sa.count()
print("length: ",length)
#for i in range(length+1):
    #newcases = (df_sa_21[i+42])
    #print("newcase_date: ",newcases)
    #if newcases != "nan":
    #    print(newcases)
    
print(df_sa_21[length-1])
newcases = (df_sa_21[length])
differance = df_sa_21[length]-df_sa_21[length-1]
differance7 = df_sa_7[length]-df_sa_7[length-1]
newcasesnew = df_sa[length]
    
covid_data = [{
        "measurement": "covid_numbers",
                   "tags":{
                       "Host":"RaspberryPi"},
                   "fields":{
                       "new_cases": float(newcases),
                       "differance": float(differance),
                       "differance7": float(differance7),
                       "newcasesnew": float(newcasesnew),
                       }
                   }
                  ]
client = InfluxDBClient('localhost',8086,'coviduser','0Pel9321','coviddata')
client.write_points(covid_data)        
                            
    


#df['South Africa'].plot()

#plt.plot (df['South Africa'].rolling(window=21).mean(), label='MA 21 days')
#plt.plot (df['South Africa'].rolling(window=7).mean(), label='MA 7 days')
#plt.title('South Africa Daily Reporter New Cases')
#plt.legend()
#plt.show()

##df['Sweden'].plot()
#plt.title('Sweden Daily Reporter New Cases')
#plt.plot (df['Sweden'].rolling(window=21).mean(), label='MA 21 days')
#plt.legend()
#plt.show()

df_sa_21 = df['South Africa'].rolling(window=21).mean()
print(df_sa_21)
print("Day -1",df_sa_21[length-1])
print("Day 0",df_sa_21[length])
print("Day 0 - Day -1",df_sa_21[length]-df_sa_21[length-1])

      
#df_sa_21.plot
#plt.show()
                          
                          
                          
            
                    
