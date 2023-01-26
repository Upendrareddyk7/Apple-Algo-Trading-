#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use("dark_background")


# In[28]:


data = pd.read_csv("C:\\Users\\Admin\\Downloads\\AAPL (1).csv")


# In[29]:


data.head()


# In[30]:


data.isnull().sum()


# In[31]:


data.describe()


# In[32]:


data.shape


# In[42]:


import seaborn as sns
sns.pairplot(data)


# In[45]:


plt.figure(figsize=(12, 5))
plt.plot(data['Adj Close Price'], label='Apple')
plt.title('Apple Adj Close Price History')
plt.xlabel("May 27,2014 - May 25,2020 ")
plt.ylabel("Adj Close Price USD ($)")
plt.legend(loc="upper left")
plt.show()


# In[46]:


sma30=pd.DataFrame()


# In[47]:


sma30["Adj Close Price"]=data["Adj Close Price"].rolling(window=30).mean()


# In[48]:


sma30


# In[49]:


sma100=pd.DataFrame()


# In[50]:


sma100["Adj Close Price"]= data["Adj Close Price"].rolling(window=100).mean()


# In[51]:


sma100


# In[54]:


plt.figure(figsize=(12,5))
plt.plot(data['Adj Close Price'], label='Apple')
plt.plot(sma30['Adj Close Price'], label='SMA30')
plt.plot(sma100['Adj Close Price'], label='SMA100')
plt.title("Apple Adj. Close Price History")
plt.xlabel('May 27,2014 - May 25,2020')
plt.ylabel('Adj. Close Price USD($)')
plt.legend(loc='upper left')
plt.show()


# In[55]:


data2=pd.DataFrame()


# In[56]:


data2["apple"]=data["Adj Close Price"]


# In[57]:


data2["SMA30"]=sma30["Adj Close Price"]


# In[58]:


data2["SMA100"]=sma100["Adj Close Price"]


# In[59]:


data2


# In[61]:


#Create a function to signal when to buy or sell stock


# In[62]:


def buySell(data2):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1
    for i in range(len(data2)):
        if data2 ['SMA30'][i] > data2['SMA100'][i]:
            if flag != 1:
                sigPriceBuy.append(data2['apple'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data2['SMA30'][i] < data2['SMA100'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data2['apple'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
    return(sigPriceBuy, sigPriceSell)


# In[63]:


#To store the buy and sell data into a variable
buySell=buySell(data2)


# In[64]:


data2['Buy Signal Price'] = buySell[0]
data2['Sell Signal Price'] = buySell[1]


# In[65]:


data2


# In[66]:


plt.style.use('classic')
plt.figure(figsize=(12,5))
plt.plot(data2['apple'], label='Apple', alpha=0.35)
plt.plot(data2['SMA30'], label='SMA30', alpha=0.35)
plt.plot(data2['SMA100'],label='SMA100', alpha=0.35)
plt.scatter(data2.index, data2['Buy Signal Price'], label ='Buy', marker='^',color='green')
plt.scatter(data2.index, data2['Sell Signal Price'],label='Sell', marker='v', color='red')
plt.title('Apple Adj. Close Price History Buy and Sell Signals')
plt.xlabel("May 27,2014 - May 25,2020")
plt.ylabel("Adj Close Price USD($)")
plt.legend(loc='upper left')
plt.show()


# In[ ]:




