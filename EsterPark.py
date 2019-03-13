
# coding: utf-8

# In[1]:



# In[80]:

import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
fname = 'vgsales.csv'
x1 = pd.read_csv(fname)

def count(x1):
    """
    this will count() method will take in x1 which was the csv file given in week8 (not the new one)
    is has to parse the following series columns in order to project sales vs year
    Rank	Name	Platform	Year	Genre	Publisher	NA_Sales	EU_Sales	JP_Sales	Other_Sales	Global_Sales
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


# In[2]:

#call the count method to plot sales vs. year
count(x1)


# In[156]:

#what does the dataframe look like
x1


# In[6]:

def foo(x1):
    """
    y axis = Revenue
    x axis = number of games sold
    this function will take that same csv file and plot total revenue vs. number of games sold per company
    the blue dots represent the other comapnies that are part of the lower half of the outliers
    """
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


# In[7]:

# call fn to find total revenue vs. number of games sold
foo(x1)


# In[8]:

def fubar(x1): 
    """
    y axis = Revenue
    x axis = number of games sold
    this function will take that same csv file and plot total revenue vs. number of games sold per company
    however, we also want all the dots, such that ea dot represents the number of games sold that year
    """
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


# In[9]:

#fn call to see the number of games sold per year
fubar(x1)


# In[14]:

x= x1[(x1['Publisher']=='Nintendo') & (x1['Year']==2006)]; 
y= np.sum(x1[(x1['Publisher']=='Nintendo') & ( x1['Year']==2006)]['Global_Sales'])
print(y)


# In[47]:



#this was yichen's new code, i moved the legend becuase it looks messy/squished

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#EU
df =pd. read_csv('vgsales.csv')
df_new=df.loc[:,['Genre','EU_Sales']]

#sports
df_sports=df_new.loc[df_new['Genre']=='Sports']
df_sports_EU = df_sports.sum()
df_sports_EU1=df_sports_EU.rename(columns={'EU_Sales': 'sports'})

#action
df_ac=df_new.loc[df_new['Genre']=='Action']
df_ac_EU = df_ac.sum()
df_ac_EU1=df_ac_EU.rename(columns={'EU_Sales': 'action'})

#adventure
df_ad=df_new.loc[df_new['Genre']=='Adventure']
df_ad_EU = df_ad.sum()
df_ad_EU1=df_ad_EU.rename(columns={'EU_Sales': 'adventure'})

#fighting
df_fi=df_new.loc[df_new['Genre']=='Fighting']
df_fi_EU = df_fi.sum()
df_fi_EU1=df_fi_EU.rename(columns={'EU_Sales': 'fighting'})

#misc
df_mi=df_new.loc[df_new['Genre']=='Misc']
df_mi_EU = df_mi.sum()
df_mi_EU1=df_mi_EU.rename(columns={'EU_Sales': 'misc'})

#platform
df_pl=df_new.loc[df_new['Genre']=='Platform']
df_pl_EU = df_pl.sum()
df_pl_EU1=df_pl_EU.rename(columns={'EU_Sales': 'platform'})


#puzzle
df_pu=df_new.loc[df_new['Genre']=='Puzzle']
df_pu_EU = df_pu.sum()
df_pu_EU1=df_pu_EU.rename(columns={'EU_Sales': 'puzzle'})

#racing
df_ra=df_new.loc[df_new['Genre']=='Racing']
df_ra_EU = df_ra.sum()
df_ra_EU1=df_ra_EU.rename(columns={'EU_Sales': 'racing'})

#role_playing
df_ro=df_new.loc[df_new['Genre']=='Role-Playing']
df_ro_EU = df_ro.sum()
df_ro_EU1=df_ro_EU.rename(columns={'EU_Sales': 'role-playing'})

#shooter
df_sh=df_new.loc[df_new['Genre']=='Shooter']
df_sh_EU = df_sh.sum()
df_sh_EU1=df_sh_EU.rename(columns={'EU_Sales': 'shooter'})


#simmulation
df_si=df_new.loc[df_new['Genre']=='Simulation']
df_si_EU = df_si.sum()
df_si_EU1=df_si_EU.rename(columns={'EU_Sales': 'Simmulation'})


#strategy
df_st=df_new.loc[df_new['Genre']=='Strategy']
df_st_EU = df_st.sum()
df_st_EU1=df_st_EU.rename(columns={'EU_Sales': 'Strategy'})


# In[20]:


df_sports_EU1


# In[21]:


df_ac_EU1


# In[22]:


df_ad_EU1


# In[23]:


df_fi_EU1


# In[24]:


df_mi_EU1


# In[25]:


df_pl_EU1


# In[26]:


df_pu_EU1


# In[27]:


df_ra_EU1


# In[28]:


df_ro_EU1


# In[29]:


df_sh_EU1


# In[30]:


df_si_EU1


# In[31]:


df_st_EU1


# In[33]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

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


# In[67]:

def fuboo(x1): 
    """
    this fn will show for each top 10 companies, what their avg revenue per year is
    thus signifying that even though nintendo made a lot more money than the rest,
    that on a yearly rate, they dont make the same rate as the other ones on avg
    which can be hurtful for quarterly investments/dividends
    """
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
            #x = len(x1[(x1['Publisher']==p) & (x1['Year']==yr)])
            yearly_revenue = np.sum(x1[(x1['Publisher']==p) & ( x1['Year']==yr)]['Global_Sales'])
            publisher_data[p].append(yearly_revenue)
    
    data = [publisher_data[p] for p in top_10]
    
    plt.figure(figsize=(8,10))
    plt.boxplot(data)
    plt.xticks(np.array(range(len(top_10)))+1,top_10, rotation=90)
    plt.xlabel("Top 10 Companies")
    plt.ylabel("Yearly Global Revenue in millions $")
    plt.title('Yearly Global Revenue for Top 10 Companies')
    plt.show()

#function call to see box/whisker plot
fuboo(x1)


# 
# 
# 
# 

# In[72]:


import matplotlib.pyplot as plt
import pandas as pd
from math import pi
get_ipython().magic('matplotlib inline')
"""
this was a radar chart example that i used from 
https://python-graph-gallery.com/390-basic-radar-chart/
https://www.kaggle.com/typewind/draw-a-radar-chart-with-python-in-a-simple-way
"""

# Set data
df = pd.DataFrame({
'group': ['A','B','C','D'],
'var1': [38, 1.5, 30, 4],
'var2': [29, 10, 9, 34],
'var3': [8, 39, 23, 24],
'var4': [7, 31, 33, 14],
'var5': [28, 15, 32, 14]
})
 
# number of variable
categories=list(df)[1:]
N = len(categories)
 
# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='grey', size=8)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,40)
 
# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')
 
# Fill area
ax.fill(angles, values, 'b', alpha=0.1)
plt.show()


# In[113]:

#need a dictionary key pair for the various game consoles and their number of games sold
platforms = np.unique(x1['Platform'])
genres = np.unique(x1['Genre'])

platform_genres_rev = {}

plt_counts = []
for p in platforms: 
    count = len(x1[x1['Platform'] == p])
    #print('{} = {}'.format(p, count))
    plt_counts.append((p, count))
    
    platform_genres_rev[p] = []
    for g in genres: 
        rev = np.sum(x1[(x1['Platform'] == p) & (x1['Genre'] == g)]['Global_Sales'])
        platform_genres_rev[p].append(rev)

plt_counts.sort(key= lambda tup:tup[1], reverse=True)
print(plt_counts)
print(platform_genres_rev['DS'])







# In[131]:

platform_revs = []
for plt, revs in platform_genres_rev.items(): 
    platform_revs.append((plt,np.sum(revs)))
    
platform_revs.sort(key = lambda tup:tup[1], reverse=True)
print(platform_revs)


# In[143]:


# ------- PART 1: Create background
# number of games sold radar chart
# number of variable
#categories=list(df)[1:]
categories = np.unique(x1['Genre'])
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
plt.figure(figsize=(10,10))
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
y_ticks = np.array(list(range(10,250,40)))

plt.yticks(y_ticks, y_ticks.astype('str'), color="grey", size=15)
plt.ylim(0,250)
 
 
# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't do a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
#values=df.loc[0].drop('group').values.flatten().tolist()
values = platform_genres_rev['DS'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="DS")
ax.fill(angles, values, 'b', alpha=0.1)
 
# Ind2
#values=df.loc[1].drop('group').values.flatten().tolist()
values = platform_genres_rev['PS2'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="PS2")
ax.fill(angles, values, 'r', alpha=0.1)


#values=df.loc[2].drop('group').values.flatten().tolist()
values = platform_genres_rev['PS3'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="PS3")
ax.fill(angles, values, 'y', alpha=0.1)
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title("Top 3 by # of games", y=1.08)
plt.show()



# In[144]:


# ------- PART 1: Create background
# num games sold 4-6 radar
# number of variable
#categories=list(df)[1:]
categories = np.unique(x1['Genre'])
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
y_ticks = np.array(list(range(10,250,40)))

plt.yticks(y_ticks, y_ticks.astype('str'), color="grey", size=15)
plt.ylim(0,250)
 
 
# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't do a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
#values=df.loc[0].drop('group').values.flatten().tolist()
values = platform_genres_rev['Wii'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Wii")
ax.fill(angles, values, 'b', alpha=0.1)
 
# Ind2
#values=df.loc[1].drop('group').values.flatten().tolist()
values = platform_genres_rev['X360'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="X360")
ax.fill(angles, values, 'r', alpha=0.1)


#values=df.loc[2].drop('group').values.flatten().tolist()
values = platform_genres_rev['PSP'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="PSP")
ax.fill(angles, values, 'y', alpha=0.1)
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title("Top 4-6 by # of games", y=1.08)

plt.show()


# In[152]:


# ------- PART 1: Create background
 #num games sold 7-9/genre
# number of variable
#categories=list(df)[1:]
categories = np.unique(x1['Genre'])
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
y_ticks = np.array(list(range(10,250,40)))

plt.yticks(y_ticks, y_ticks.astype('str'), color="grey", size=15)
plt.ylim(0,250)
 
 
# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't do a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
#values=df.loc[0].drop('group').values.flatten().tolist()
values = platform_genres_rev['PS'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="PS")
ax.fill(angles, values, 'b', alpha=0.1)
 
# Ind2
#values=df.loc[1].drop('group').values.flatten().tolist()
values = platform_genres_rev['PC'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="PC")
ax.fill(angles, values, 'r', alpha=0.1)


#values=df.loc[2].drop('group').values.flatten().tolist()
values = platform_genres_rev['XB'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="XB")
ax.fill(angles, values, 'y', alpha=0.1)
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title("Top 7-9 by # of games", y=1.08)

plt.show()


# In[142]:

# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 #amt of sales/genre/platform
# ------- PART 1: Create background
 
# number of variable
#categories=list(df)[1:]
categories = np.unique(x1['Genre'])
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
y_ticks = np.array(list(range(0,300,50)))

plt.yticks(y_ticks, y_ticks.astype('str'), color="grey", size=15)
plt.ylim(0,300)
 
 
# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't do a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
#values=df.loc[0].drop('group').values.flatten().tolist()
values = platform_genres_rev['PS2'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="PS2")
ax.fill(angles, values, 'b', alpha=0.1)
 
# Ind2
#values=df.loc[1].drop('group').values.flatten().tolist()
values = platform_genres_rev['X360'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="X360")
ax.fill(angles, values, 'r', alpha=0.1)


#values=df.loc[2].drop('group').values.flatten().tolist()
values = platform_genres_rev['PS3'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="PS3")
ax.fill(angles, values, 'y', alpha=0.1)
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title("Top 1-3 by sales", y=1.08)

plt.show()


# In[147]:

#amt of sales/genre/platform
# number of variable
#categories=list(df)[1:]
categories = np.unique(x1['Genre'])
N = len(categories)

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)

# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)

# Draw ylabels
ax.set_rlabel_position(0)
y_ticks = np.array(list(range(0,300,50)))

plt.yticks(y_ticks, y_ticks.astype('str'), color="grey", size=15)
plt.ylim(0,300)


# ------- PART 2: Add plots

# Plot each individual = each line of the data
# I don't do a loop, because plotting more than 3 groups makes the chart unreadable

# Ind1
#values=df.loc[0].drop('group').values.flatten().tolist()
values = platform_genres_rev['Wii'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Wii")
ax.fill(angles, values, 'b', alpha=0.1)

# Ind2
#values=df.loc[1].drop('group').values.flatten().tolist()
values = platform_genres_rev['DS'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="DS")
ax.fill(angles, values, 'r', alpha=0.1)


#values=df.loc[2].drop('group').values.flatten().tolist()
values = platform_genres_rev['PS'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="PS")
ax.fill(angles, values, 'y', alpha=0.1)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title("Top 4-6 by sales", y=1.08)

plt.show()


# In[155]:


 #amt of sales/genre/platform
# number of variable
#categories=list(df)[1:]
categories = np.unique(x1['Genre'])
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
y_ticks = np.array(list(range(0,300,50)))

plt.yticks(y_ticks, y_ticks.astype('str'), color="grey", size=15)
plt.ylim(0,300)
 
 
# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't do a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
#values=df.loc[0].drop('group').values.flatten().tolist()
values = platform_genres_rev['GBA'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="GBA")
ax.fill(angles, values, 'b', alpha=0.1)
 
# Ind2
#values=df.loc[1].drop('group').values.flatten().tolist()
values = platform_genres_rev['PSP'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="PSP")
ax.fill(angles, values, 'r', alpha=0.1)


#values=df.loc[2].drop('group').values.flatten().tolist()
values = platform_genres_rev['PS4'].copy()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="PS4")
ax.fill(angles, values, 'y', alpha=0.1)
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title("Top 7-9 by sales", y=1.08)

plt.show()


# In[ ]:



