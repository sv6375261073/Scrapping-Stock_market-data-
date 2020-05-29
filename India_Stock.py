#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
import pandas
import requests
def getNSEStockLive(symbol):
    url='https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp?symbol='+symbol+'&series=EQ'
    refer='https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp?symbol='+symbol+'&illiquid=0&smeFlag=0&itpFlag=0'
    try:
        drill_down=requests.get(url,header={'referer':referer}).json()['data'][0]
        return [drill_down['open'],drill_down['dayHigh'],drill_down['dayLow'],drill_down['lastPrice'],
                drill_down['closePrice'],drill_down['previousClose'],drill_down['close'],
                drill_down['pChange']+'%',int(drill_down['totalTradeVolume'].replace(',',''))/1000000]
    except:
        return ['-','-','-','-','-','-','-','-','-']
symbols=['SBIN','RVNL','HDFCBANK','RCOM','RPOWER']
cNum=0 # stores list of filtered data
stockList=[]
for drill in symbols:
    cNum+=1
    print('Calculated : '+str(cNum)+' '+drill,end='\r')
    stockList.append(getNSEStockLive(drill))
    
print('This list is of '+str(sys.getsizeof(stockList))+' bits')
print(pandas.DataFrame(stockList,columns=['Open','High','Low','LTP','T Close','P Close','V Change','P Change','Volume(M)'],index=symbols))

