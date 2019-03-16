#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def plot(x,title):
    """
    author: Jiawei Song
    the function to plot sales vs.time of game type
    """
    assert isinstance(title, str)
        

    #sports
    df_sp=x.loc[x['Genre']=='Sports']
    df_sp = df_sp.groupby('Year').sum()


    #action
    df_ac=x.loc[x['Genre']=='Action']
    df_ac = df_ac.groupby('Year').sum()


    #adventure
    df_ad=x.loc[x['Genre']=='Adventure']
    df_ad = df_ad.groupby('Year').sum()



    #fighting
    df_fi=x.loc[x['Genre']=='Fighting']
    df_fi= df_fi.groupby('Year').sum()


    #misc
    df_mi=x.loc[x['Genre']=='Misc']
    df_mi = df_mi.groupby('Year').sum()


    #platform
    df_pl=x.loc[x['Genre']=='Platform']
    df_pl = df_pl.groupby('Year').sum()


    #puzzle
    df_pu=x.loc[x['Genre']=='Puzzle']
    df_pu = df_pu.groupby('Year').sum()


    #racing
    df_ra=x.loc[x['Genre']=='Racing']
    df_ra = df_ra.groupby('Year').sum()

    #role_playing
    df_ro=x.loc[x['Genre']=='Role-Playing']
    df_ro = df_ro.groupby('Year').sum()


    #shooter
    df_sh=x.loc[x['Genre']=='Shooter']
    df_sh= df_sh.groupby('Year').sum()



    #simmulation
    df_si=x.loc[x['Genre']=='Simulation']
    df_si= df_si.groupby('Year').sum()



    #strategy
    df_st=x.loc[x['Genre']=='Strategy']
    df_st = df_st.groupby('Year').sum()



    res = pd.concat([df_st, df_si,df_sh,df_ro, df_ra, df_pu,df_pl, df_mi, df_fi, df_ad, df_ac, df_sp,], axis=1, join_axes=[df_st.index])
    res.columns = ['Strategy','Simulation','Shooter','Role-Playing', 'Racing', 'Puzzle','Platform','Misc','Fighting','Adventure','Action','Sports']

    plt.figure(figsize=(10,5))
    plt.grid(True)
    plt.plot(df_st, 'b', label="Strategy")
    plt.plot(df_si, 'r', label="Simmulation")
    plt.plot(df_sh, 'g', label="Shooter")
    plt.plot(df_ro, 'c', label="Role-playing")
    plt.plot(df_ra, 'y', label="Racing")
    plt.legend(loc="upper left")
    plt.xlabel("Year")
    plt.ylabel("Sale  [million $] ")
    plt.title(title)


    return plt.show()



    


# In[ ]:


def compare(x):
    """
    author: Jiawei Song
    this funciton is to compare sale for genre in two time spans
    """
    
    before2011=x[(x["Year"]>=2005) & (x["Year"]<2011)].groupby('Genre')['Global_Sales'].sum().sort_values(ascending = False).reset_index()

    after2011=x[(x["Year"]>=2011) & (x["Year"]<2017)].groupby('Genre')['Global_Sales'].sum().sort_values(ascending = False).reset_index()




    df_ = pd.merge(before2011, after2011, how='left', on='Genre')
    df_.columns = ['Genre','2005-2010 Sales','2011-2016 Sales']

    df_.set_index('Genre')[['2005-2010 Sales', '2011-2016 Sales']].plot(kind='bar', 
                                                                            figsize=(18, 12))

    plt.xticks(rotation=0)
    plt.title("Comparison of Global Sales for Genre in Two Time Spans", fontsize=26, y=1.01)
    plt.xlabel("Genre", fontsize=26, labelpad=15)
    plt.ylabel("Total Sales  [million $] ", fontsize=26, labelpad=15)
    plt.yticks(fontsize = 15 )
    plt.xticks(fontsize = 15 )
    return plt.show()



    

