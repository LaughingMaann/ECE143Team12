
# coding: utf-8

# In[2]:


def mul_barchart(df):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import mpl_toolkits.mplot3d.art3d as art3d
    from numpy import pi, arange, linspace, sin
    min_year = int(df['Year'].dropna().min())
    max_year = int(df['Year'].dropna().max())
    year_range = range(min_year,max_year+1)
    year_saleNA = []
    year_saleEU = []
    year_saleJP = []
    year_saleO = []

    year_list = []
    for year in year_range:
        year_saleNA.append(df[df['Year'] == year].dropna()['NA_Sales'].sum())
        year_saleEU.append(df[df['Year'] == year].dropna()['EU_Sales'].sum())
        year_saleJP.append(df[df['Year'] == year].dropna()['JP_Sales'].sum())
        year_saleO.append(df[df['Year'] == year].dropna()['Other_Sales'].sum())
        year_list.append(year) 
    x = year_list
    plt.figure(figsize=(20,10))
    plt.fill_between(x,year_saleNA,alpha=0.4,step="pre",label = "North America")
    plt.fill_between(x,year_saleEU,alpha=0.4,step="pre",label = "Europ")
    plt.fill_between(x,year_saleJP,alpha=0.4,step="pre",label = "Japan")
    plt.fill_between(x,year_saleO,alpha=0.4,step="pre", label = "Other")
    plt.plot(x,year_saleNA,drawstyle="steps")
    plt.plot(x,year_saleEU,drawstyle="steps")
    plt.plot(x,year_saleJP,drawstyle="steps")
    plt.plot(x,year_saleO,drawstyle="steps")
    plt.legend(loc='upper right')
    plt.title('Total Sales on different region',fontsize=15 )
    plt.ylabel('Total Sales in millions',fontsize=15)
    plt.xlabel('Year',fontsize=15)
    plt.show()
    


# In[9]:


def Platf (c):
    if c['Platform'] in PlayStation:
        return 'PlayStation'
    elif c['Platform'] in Nintendo:
        return 'Nintendo'
    elif c['Platform'] in Microsoft:
        return 'Microsoft'
    elif c['Platform'] in Other:
        return 'Other'
    else:
        return 'Outflit'


# In[10]:


def bar_grid(df,x):
    import numpy as np
    import colorsys
    import pandas as pd 
    import seaborn as sns
    import matplotlib.pyplot as plt
    from collections import Counter
    get_ipython().run_line_magic('matplotlib', 'inline')
    sns.set_style("darkgrid")
    ax=df.set_index('Name')[['North America', 'Europe', 'Japan', 'Other']].plot(kind='barh',
    figsize=(18, 12), stacked=True)
    plt.title(x, fontsize=26)
    plt.xlabel("Total Sales(Million$)", fontsize=26)
    plt.ylabel("Name", fontsize=26)
    plt.yticks(fontsize=22)
    plt.xticks(fontsize=22)
    plt.legend(fontsize=22)


# In[11]:


def comp_bar(before,after,xx):
    import numpy as np
    import colorsys
    import pandas as pd 
    import seaborn as sns
    import matplotlib.pyplot as plt
    from collections import Counter
    get_ipython().run_line_magic('matplotlib', 'inline')
    
    combined=pd.merge(before, after, on="Platf")
    combined=combined.rename(index=str, columns={"Global_Sales_x": "2005-2010 Sales", "Global_Sales_y": "2011-2016 Sales"})
    sns.set_style("darkgrid")
    combined.set_index('Platf')[['2005-2010 Sales', '2011-2016 Sales']].plot(kind='bar',figsize=(18, 12))
    plt.xticks(rotation = 0)
    plt.title(xx, fontsize=26, y=1.01)
    plt.xlabel("Platform groups", fontsize=26)
    plt.ylabel("Total Sales in [Million $] ", fontsize=26)
    plt.yticks(fontsize = 24 )
    plt.xticks(fontsize = 24 )

    #ax = plt.gca()
    plt.legend(fontsize=20);

