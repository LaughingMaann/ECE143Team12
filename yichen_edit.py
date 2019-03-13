# coding: utf-8

# In[19]:


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