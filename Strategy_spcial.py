
# coding: utf-8

# In[80]:

import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
fname = 'vgsales.csv'
x1 = pd.read_csv(fname)

def count(x1):
    """
    this will count the 
    """
    assert isinstance(x1, pd.core.frame.DataFrame)
    assert 'Year' in x1
    yr = x1['Year']
    years = np.unique(x1['Year'][~np.isnan(x1['Year'])]).astype(int)
    NA_Sales = []
    EU_Sales = []
    JP_Sales = []
    Other_Sales = []
    
    for y in years: 
        NA_Sales.append(np.sum(x1[x1['Year'] == y]['NA_Sales']))
        EU_Sales.append(np.sum(x1[x1['Year'] == y]['EU_Sales']))
        JP_Sales.append(np.sum(x1[x1['Year'] == y]['JP_Sales']))
        Other_Sales.append(np.sum(x1[x1['Year'] == y]['Other_Sales']))
        
    plt.figure(figsize=(10,5))
    xaxis = range(len(years))
    plt.grid(True)
    plt.plot(NA_Sales, 'bo', label="NA sales")
    plt.plot(EU_Sales, 'ro', label="EU sales")
    plt.plot(JP_Sales, 'go', label="JP sales")
    plt.plot(Other_Sales, 'co', label="other sales")
    plt.ylabel("Sales in millions $")
    plt.legend(loc="upper left")
    plt.xticks(xaxis,years, rotation=70)
    plt.show()
    


# In[81]:

x1


# In[71]:

count(x1)


# In[72]:

EU_Sales


# In[112]:



    


# In[108]:

x1


# In[118]:


def foo(x1): 
    # y axis = Revenue
    # x axis = number of games sold

    publishers = x1.Publisher.unique()

    data = []

    max_pub = ''
    max_rev = 0 

    max_games_pub = ''
    max_games = 0
    for pub in publishers: 
        x = len(x1[x1['Publisher']==pub])
        y = np.sum(x1[x1['Publisher']==pub]['Global_Sales'])

        data.append((x,y, pub))

        if y > max_rev: 
            max_rev = y
            max_pub = pub

        if x > max_games: 
            max_games = x
            max_games_pub = pub

    plt.figure(figsize=(10,5))
    for x,y,pub in data: 
        if x>600: 
            plt.plot(x,y,'o', label=pub)
        else: 
            plt.plot(x,y,'bo')
    plt.legend(loc="upper left")
    plt.xlabel("Number of games sold")
    plt.ylabel("Total Revenue")
    plt.grid(True)
    plt.show()
    
foo(x1)


# In[138]:

def fubar(x1): 
    # y axis = Revenue
    # x axis = number of games sold

    publishers = x1.Publisher.unique()

    data = []


    for pub in publishers: 
        x = len(x1[x1['Publisher']==pub])
        y = np.sum(x1[x1['Publisher']==pub]['Global_Sales'])

        data.append((x,y, pub))

        
    data.sort(key=lambda tup: tup[1], reverse=True)
    
    top_10 = [d[2] for d in data[:10]]
    
    
    years = np.unique(x1['Year'][~np.isnan(x1['Year'])]).astype(int)
    
    publisher_data = {}
    for p in top_10: 
        publisher_data[p] = []
        for yr in years: 
            x = len(x1[(x1['Publisher']==p) & (x1['Year']==yr)])
            y = np.sum(x1[(x1['Publisher']==p) & ( x1['Year']==yr)]['Global_Sales'])
            publisher_data[p].append((x,y))
    
    
    
    plt.figure(figsize=(12,10))
    for p in publisher_data:
        x,y = map(list, zip(*publisher_data[p]))
        plt.plot(x,y, 'o', label=p)
    plt.legend(loc="upper left")
    plt.xlabel("Number of games sold")
    plt.ylabel("Total Revenue")
    plt.grid(True)
    plt.show()
    
    
fubar(x1)


# In[126]:

x1[(x1['Publisher']=='Nintendo') & (x1['Year']==2006)]


# In[134]:

np.sum(x1[(x1['Publisher']=='Nintendo') & ( x1['Year']==2006)]['Global_Sales'])


# In[ ]:



