# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 01:36:51 2020

@author: jacob
"""




#########################################
#                                       #
#              READING DATA             #
#                                       #
#########################################
import pandas_datareader.data as web
import pandas as pd
import time
import matplotlib.pyplot as plt
import pandas_datareader
pd.core.common.is_list_like = pd.api.types.is_list_like

from pandas_datareader import data as pdr

ticker_tesla =  'TSLA' # tesla
ticker_ford = 'F'  # Ford Motor Company (F), nyse
ticker_renault = 'RNL.DE' #Renault SA Frankfur
ticker_NIO = 'NIO'


#YAHOO is very unstable lately, so it is a good idea to insist until it reads. Actually, t can be a good idea to put a
# loop to insist in the job of grabbing the data and waiting 5 seccounds for next try.
run_ok = 0
numb_tries = 0 
while(run_ok == 0) and (numb_tries < 10):
    try:        
        numb_tries += 1
        df_index_ticker_tesla = pdr.get_data_yahoo(ticker_tesla, start='2012-01-01', end='2020-07-25')
        df_index_ticker_ford = pdr.get_data_yahoo(ticker_ford, start='2012-01-01', end='2020-07-25')
        df_index_ticker_renault = pdr.get_data_yahoo(ticker_renault, start='2012-01-01', end='2020-07-25') 
        df_index_ticker_NIO = pdr.get_data_yahoo(ticker_NIO, start='2012-01-01', end='2020-07-25') 
        
        
        run_ok = 1
    except:
        print ("-> PROBLEM WITH YAHOO - SLEEPING 5 seconds")
        time.sleep(5)
        run_ok = 0

df_merged = pd.DataFrame({ 'adj_close_ticker_tesla': df_index_ticker_tesla['Adj Close'],
                            'adj_close_ticker_ford': df_index_ticker_ford['Adj Close'],
                            'adj_close_ticker_renault': df_index_ticker_renault['Adj Close'],
                            'adj_close_ticker_NIO': df_index_ticker_NIO['Adj Close']},
                         
                        index=sorted(set(df_index_ticker_tesla.index).union(df_index_ticker_ford.index).union(df_index_ticker_renault.index))) 
  

print(df_merged)

print(df_merged.isnull().sum())
df_merged = df_merged.fillna(method='ffill')
df_merged.head()

#########################################
#       Pandas Built-in Matplotlib      #
#########################################
%matplotlib inline
ax = df_merged[['adj_close_ticker_tesla','adj_close_ticker_ford','adj_close_ticker_renault','adj_close_ticker_NIO']].plot()
ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price')
ax.legend()

df_merged['norm_adj_close_ticker_tesla'] = df_merged['adj_close_ticker_tesla'] / df_merged['adj_close_ticker_tesla'].max()
df_merged['norm_adj_close_ticker_ford'] = df_merged['adj_close_ticker_ford'] / \
    df_merged['adj_close_ticker_ford'].max()
df_merged['norm_adj_close_ticker_renault'] = df_merged['adj_close_ticker_renault'] / df_merged['adj_close_ticker_renault'].max()
df_merged['norm_adj_close_ticker_NIO'] = df_merged['adj_close_ticker_NIO'] / df_merged['adj_close_ticker_NIO'].max()


%matplotlib inline
ax = df_merged[['norm_adj_close_ticker_tesla','norm_adj_close_ticker_ford','norm_adj_close_ticker_renault','norm_adj_close_ticker_NIO']].plot()
ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price (1 as maximum)')
ax.legend()


df_merged['norm_adj_close_ticker_tesla'] = df_merged['adj_close_ticker_tesla'] / df_merged['adj_close_ticker_tesla'].max()
df_merged['norm_adj_close_ticker_ford'] = df_merged['adj_close_ticker_ford'] / \
    df_merged['adj_close_ticker_ford'].max()
df_merged['norm_adj_close_ticker_renault'] = df_merged['adj_close_ticker_renault'] / df_merged['adj_close_ticker_renault'].max()
df_merged['norm_adj_close_ticker_NIO'] = df_merged['adj_close_ticker_NIO'] / df_merged['adj_close_ticker_NIO'].max()


%matplotlib inline
ax = df_merged[['norm_adj_close_ticker_tesla','norm_adj_close_ticker_ford','norm_adj_close_ticker_renault','norm_adj_close_ticker_NIO']].plot()
ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price (1 as maximum)')
ax.legend(bbox_to_anchor=(1,0), loc="lower left") 






