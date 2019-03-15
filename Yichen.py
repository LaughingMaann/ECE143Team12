Yichen
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df =pd. read_csv('vgsales.csv')
import matplotlib.dates as mdates

class plots1(object):
    """
    author:Yichen Zhang
    compute different regions_Sales grouped by platform and choose the top 4
    plot pie charts for the top 4
    """
    def __init__(self, df):
        assert isinstance (df, pd.core.frame.DataFrame)
        assert 'Platform' in df
        #EU_Sales
        new =df.groupby('Platform')['EU_Sales'].sum().sort_values(ascending=False).reset_index()
        #NA_Sales
        new=df.groupby('Platform')['NA_Sales'].sum().sort_values(ascending=False).reset_index()
        #JP_Sales
        new=df.groupby('Platform')['JP_Sales'].sum().sort_values(ascending=False).reset_index()
        #Other_Sales
        new=df.groupby('Platform')['Other_Sales'].sum().sort_values(ascending=False).reset_index()
        #Global_Sales
        new=df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).reset_index()        
        #pie chart for top4 platform EU_Sales
        plt.figure(figsize=(6,9)) 
        labels = ['PS3','PS2','X360','Wii','Other']
        sizes = [343.71,339.29,280.58,268.38,213.6+194.65+139.68+123.7+75.25+68.25+60.95+58.52+41.06+45.65+38.71+24.23+
                 21.15+5.47+19.04+16.33+5.52+0.54] 
        sizes = 100*np.array(sizes)/np.sum(sizes)
        legend_labels = ['{} ({:4.1f} %)'.format(lbl,siz) for lbl,siz in zip(labels,sizes)] 
        colors = ['royalblue','deepskyblue','skyblue','lightcyan','aliceblue'] 
        explode = (0,0,0,0,0) 
        patches,text1= plt.pie(sizes,
                              explode=explode,
                              #labels=labels,
                              colors=colors,
                              #autopct = '%3.2f%%', 
                              shadow = True, 
                              startangle =90, 
                              ) 
        # Add legend
        plt.legend(legend_labels,loc='upper right', bbox_to_anchor=(0.2,0.75), bbox_transform=plt.gcf().transFigure)
        plt.axis('equal')
        plt.title('Top 4 Platform sales in Europe',fontsize=20)
        plt.show()
    
        #pie chart for top4 platform NA_Sales
        plt.figure(figsize=(6,9)) 
        labels = ['X360','PS2','Wii','PS3','Other']
        sizes = [601.05, 583.84, 507.71, 392.26, 390.71+336.51+187.54+186.69+139.02+133.46+125.94+108.99+96.8+93.28+90.6+83.19+78.87+ 
                 61.23+ 38.32+19.27+16.2+0.72] 

        sizes = 100*np.array(sizes)/np.sum(sizes)
        legend_labels = ['{} ({:4.1f} %)'.format(lbl,siz) for lbl,siz in zip(labels,sizes)] 
        colors = ['royalblue','deepskyblue','skyblue','lightcyan','aliceblue'] 
        explode = (0,0,0,0,0) 


        patches,text1= plt.pie(sizes,
                              explode=explode,
                              #labels=labels,
                              colors=colors,
                              #autopct = '%3.2f%%', 
                              shadow = True, 
                              startangle =90, 
                              #pctdistance = 0.6
                                     ) 
        # Add legend
        plt.legend(legend_labels,loc='upper right', bbox_to_anchor=(0.2,0.75), bbox_transform=plt.gcf().transFigure)
        plt.axis('equal')
        plt.title('Top 4 Platform sales in NorthAmerica',fontsize=20)
        plt.show()
        
        #pie chart for top4 platform JP_Sales
        plt.figure(figsize=(6,9)) 
        labels = ['DS','PS','PS2','SNES','Other']
        sizes = [175.57, 139.82, 139.2, 116.55, 98.65+97.35+90.6+79.99+76.79+69.35+47.33+34.22+32.26+21.58+20.96+14.3+12.79+12.43+ 
                 2.67+1.38+0.34+0.17] 

        sizes = 100*np.array(sizes)/np.sum(sizes)
        legend_labels = ['{} ({:4.1f} %)'.format(lbl,siz) for lbl,siz in zip(labels,sizes)] 
        colors = ['royalblue','deepskyblue','skyblue','lightcyan','aliceblue'] 
        explode = (0,0,0,0,0) 


        patches,text1= plt.pie(sizes,
                              explode=explode,
                              #labels=labels,
                              colors=colors,
                              #autopct = '%3.2f%%', 
                              shadow = True, 
                              startangle =90, 
                              #pctdistance = 0.6
                                     ) 
        # Add legend
        plt.legend(legend_labels,loc='upper right', bbox_to_anchor=(0.2,0.75), bbox_transform=plt.gcf().transFigure)
        plt.axis('equal')
        plt.title('Top 4 Platform sales in Japan',fontsize=20)
        plt.show()
        

