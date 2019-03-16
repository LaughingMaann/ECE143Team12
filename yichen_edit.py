# coding: utf-8

# In[19]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df =pd. read_csv('vgsales.csv')
import matplotlib.dates as mdates

class plots(object):
    """
    author:Yichen Zhang
    compute EU_Sales grouped by genre and plot pie charts
    """
    def __init__(self, df):
        assert isinstance (df, pd.core.frame.DataFrame)
        assert 'Platform' in df
        #EU_Sales
        new =df.groupby('Genre')['EU_Sales'].sum().sort_values(ascending=False).reset_index()
        plt.figure(figsize=(6,6)) 
        labels = ['Sports','Action','Shooter','Racing','Misc','Role-Playing','Simulation','Platform','Fighting','Strategy','Puzzle','Adventure'] #定义标签
        sizes = [376.85,525,313.27,238.39,215.98,188.06,113.38,201.63,101.32,45.34,50.78,64.13] 
        sizes = 100*np.array(sizes)/np.sum(sizes)
        legend_labels = ['{} ({:4.1f} %)'.format(lbl,siz) for lbl,siz in zip(labels,sizes)]
        colors = ['red','yellowgreen','lightskyblue','yellow','green','purple','orange','pink','gray','blue','magenta','cyan'] #每块颜色定义
        explode = (0,0,0,0,0,0,0,0,0,0,0,0) 

        patches,text1= plt.pie(sizes,
                              explode=explode,
                              #labels=labels,
                              colors=colors,
                              #autopct = '%3.2f%%', 
                              shadow = True, 
                              startangle =90, 
                              #pctdistance = 1.6
                                     ) 
        plt.legend(legend_labels, bbox_to_anchor=(1.2,0) , loc="lower right", bbox_transform=plt.gcf().transFigure)
        plt.axis('equal')
        plt.title('Genre sales in Europe')
        plt.show()
