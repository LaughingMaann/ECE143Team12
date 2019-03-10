
# coding: utf-8

# In[69]:

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
    


# In[70]:

x1


# In[71]:

count(x1)


# In[72]:

EU_Sales


# In[ ]:



