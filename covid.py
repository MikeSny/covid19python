import matplotlib.pyplot as plt
import numpy
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
#import kaggle
import zipfile

api = KaggleApi()
api.authenticate()

api.dataset_download_file('antgoldbloom/covid19-data-from-john-hopkins-university','CONVENIENT_global_confirmed_cases.csv')





#api.dataset_download_file('antgoldbloom/covid19-data-from-john-hopkins-university','CONVENIENT_global_confirm_cases.csv')
                          
df = pd.read_csv('CONVENIENT_global_confirmed_cases.csv')

print (df)

total = df['South Africa'].sum()

df_sa = df['South Africa']
print(df_sa)
print ('Total ',total)

df['South Africa'].plot()

plt.plot (df['South Africa'].rolling(window=21).mean(), label='MA 21 days')
plt.plot (df['South Africa'].rolling(window=7).mean(), label='MA 7 days')
plt.title('South Africa Daily Reporter New Cases')
plt.legend()
plt.show()

##df['Sweden'].plot()
plt.title('Sweden Daily Reporter New Cases')
plt.plot (df['Sweden'].rolling(window=21).mean(), label='MA 21 days')
plt.legend()
plt.show()


df_sa_7 = df['South Africa'].rolling(window=7).mean()
df_sa_21 = df['South Africa'].rolling(window=21).mean()
print("7 day ",df_sa_7)
print(df_sa_21)
df_sa_21.plot
plt.show()
                          
                          
                          
            
                    