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
plt.title('South Africa Daily Reporter New Cases')
plt.legend()
plt.show()

df['Japan'].plot()
plt.title('Israel Daily Reporter New Cases')
plt.plot (df['Israel'].rolling(window=21).mean(), label='MA 21 days')
plt.legend()
plt.show()
                          
                          
                          
            
                    