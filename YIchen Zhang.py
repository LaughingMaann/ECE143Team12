
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#EU
df =pd. read_csv('vgsales.csv')
df_new=df.loc[:,['Platform','EU_Sales']]


#PS3
df_PS3=df_new.loc[df_new['Platform']=='PS3']
df_PS3_EU = df_PS3.sum()
df_PS3_EU1=df_PS3_EU.rename(columns={'EU_Sales': 'PS3'})

#X360
df_X360=df_new.loc[df_new['Platform']=='X360']
df_X360_EU = df_X360.sum()
df_X360_EU1=df_X360_EU.rename(columns={'EU_Sales': 'X360'})

#PS4
df_PS4=df_new.loc[df_new['Platform']=='PS4']
df_PS4_EU = df_PS4.sum()
df_PS4_EU1=df_PS4_EU.rename(columns={'EU_Sales': 'PS4'})

#DS
df_DS=df_new.loc[df_new['Platform']=='DS']
df_DS_EU = df_DS.sum()
df_DS_EU1=df_DS_EU.rename(columns={'EU_Sales': 'DS'})

#PSP
df_PSP=df_new.loc[df_new['Platform']=='PSP']
df_PSP_EU = df_PSP.sum()
df_PSP_EU1=df_PSP_EU.rename(columns={'EU_Sales': 'PSP'})

#PS2
df_PS2=df_new.loc[df_new['Platform']=='PS2']
df_PS2_EU = df_PS2.sum()
df_PS2_EU1=df_PS2_EU.rename(columns={'EU_Sales': 'PS2'})


#N64
df_N64=df_new.loc[df_new['Platform']=='N64']
df_N64_EU = df_N64.sum()
df_N64_EU1=df_N64_EU.rename(columns={'EU_Sales': 'N64'})

#Wii
df_Wii=df_new.loc[df_new['Platform']=='Wii']
df_Wii_EU = df_Wii.sum()
df_Wii_EU1=df_Wii_EU.rename(columns={'EU_Sales': 'Wii'})

#PC
df_PC=df_new.loc[df_new['Platform']=='PC']
df_PC_EU = df_PC.sum()
df_PC_EU1=df_PC_EU.rename(columns={'EU_Sales': 'PC'})

#GBA
df_GBA=df_new.loc[df_new['Platform']=='GBA']
df_GBA_EU = df_GBA.sum()
df_GBA_EU1=df_GBA_EU.rename(columns={'EU_Sales': 'GBA'})


#WiiU
df_WiiU=df_new.loc[df_new['Platform']=='WiiU']
df_WiiU_EU = df_WiiU.sum()
df_WiiU_EU1=df_WiiU_EU.rename(columns={'EU_Sales': 'WiiU'})


#PS
df_PS=df_new.loc[df_new['Platform']=='PS']
df_PS_EU = df_PS.sum()
df_PS_EU1=df_PS_EU.rename(columns={'EU_Sales': 'PS'})

#XB
df_XB=df_new.loc[df_new['Platform']=='XB']
df_XB_EU = df_XB.sum()
df_XB_EU1=df_XB_EU.rename(columns={'EU_Sales': 'XB'})



#XOne
df_XOne=df_new.loc[df_new['Platform']=='XOne']
df_XOne_EU = df_XOne.sum()
df_XOne_EU1=df_XOne_EU.rename(columns={'EU_Sales': 'XOne'})


#3DS
df_3DS=df_new.loc[df_new['Platform']=='3DS']
df_3DS_EU = df_3DS.sum()
df_3DS_EU1=df_3DS_EU.rename(columns={'EU_Sales': '3DS'})

#GC
df_GC=df_new.loc[df_new['Platform']=='GC']
df_GC_EU = df_GC.sum()
df_GC_EU1=df_GC_EU.rename(columns={'EU_Sales': 'GC'})

#PSV
df_PSV=df_new.loc[df_new['Platform']=='PSV']
df_PSV_EU = df_PSV.sum()
df_PSV_EU1=df_PSV_EU.rename(columns={'EU_Sales': 'PSV'})

#NES
df_NES=df_new.loc[df_new['Platform']=='NES']
df_NES_EU = df_NES.sum()
df_NES_EU1=df_NES_EU.rename(columns={'EU_Sales': 'NES'})

#2600
df_2600=df_new.loc[df_new['Platform']=='2600']
df_2600_EU = df_2600.sum()
df_2600_EU1=df_2600_EU.rename(columns={'EU_Sales': '2600'})

#SNES
df_SNES=df_new.loc[df_new['Platform']=='SNES']
df_SNES_EU = df_SNES.sum()
df_SNES_EU1=df_SNES_EU.rename(columns={'EU_Sales': 'SNES'})

#GEN
df_GEN=df_new.loc[df_new['Platform']=='GEN']
df_GEN_EU = df_GEN.sum()
df_GEN_EU1=df_GEN_EU.rename(columns={'EU_Sales': 'GEN'})

#SAT
df_SAT=df_new.loc[df_new['Platform']=='SAT']
df_SAT_EU = df_SAT.sum()
df_SAT_EU1=df_SAT_EU.rename(columns={'EU_Sales': 'SAT'})


# In[2]:


df_PS3_EU1


# In[3]:


df_X360_EU1


# In[4]:


df_PS4_EU1


# In[5]:


df_DS_EU1


# In[6]:


df_PSP_EU1


# In[7]:


df_PS2_EU1


# In[8]:


df_N64_EU1


# In[9]:


df_Wii_EU1


# In[10]:


df_PC_EU1


# In[11]:


df_GBA_EU1


# In[12]:


df_WiiU_EU1


# In[13]:


df_PS_EU1


# In[14]:


df_XB_EU1


# In[15]:


df_XOne_EU1


# In[16]:


df_3DS_EU1


# In[17]:


df_GC_EU1


# In[18]:


df_PSV_EU1


# In[19]:


df_NES_EU1


# In[20]:


df_2600_EU1


# In[21]:


df_SNES_EU1


# In[22]:


df_GEN_EU1


# In[23]:


df_SAT_EU1


# In[24]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

plt.figure(figsize=(6,9)) 


labels = ['PS3','PS2','X360','Wii','PS','DS','PC','PS4','GBA','PSP','XB','3DS','N64','XOne','GC','WiiU',
          'NES','2600','SNES','PSV','GEN','SAT']
sizes = [343.71,339.29,280.58,268.38,213.6,194.65,139.68,123.7,75.25,68.25,60.95,58.52,41.06,45.65,38.71,24.23,
         21.15,5.47,19.04,16.33,5.52,0.54] 
         
colors = ['salmon','yellowgreen','coral','yellow','c','purple','orange','pink','gray','orangered','lightcyan','salmon','mistyrose','sandybrown','orchid','mediumpurple','tan'] 
explode = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) 

patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', 
                      shadow = False, 
                      startangle =90, 
                      pctdistance = 0.6) 
plt.axis('equal')
plt.show()


# In[25]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#NA
df =pd. read_csv('vgsales.csv')
df_new=df.loc[:,['Platform','NA_Sales']]


#PS3
df_PS3=df_new.loc[df_new['Platform']=='PS3']
df_PS3_NA = df_PS3.sum()
df_PS3_NA1=df_PS3_NA.rename(columns={'NA_Sales': 'PS3'})

#X360
df_X360=df_new.loc[df_new['Platform']=='X360']
df_X360_NA = df_X360.sum()
df_X360_NA1=df_X360_NA.rename(columns={'NA_Sales': 'X360'})

#PS4
df_PS4=df_new.loc[df_new['Platform']=='PS4']
df_PS4_NA = df_PS4.sum()
df_PS4_NA1=df_PS4_NA.rename(columns={'NA_Sales': 'PS4'})

#DS
df_DS=df_new.loc[df_new['Platform']=='DS']
df_DS_NA = df_DS.sum()
df_DS_NA1=df_DS_NA.rename(columns={'NA_Sales': 'DS'})

#PSP
df_PSP=df_new.loc[df_new['Platform']=='PSP']
df_PSP_NA = df_PSP.sum()
df_PSP_NA1=df_PSP_NA.rename(columns={'NA_Sales': 'PSP'})

#PS2
df_PS2=df_new.loc[df_new['Platform']=='PS2']
df_PS2_NA = df_PS2.sum()
df_PS2_NA1=df_PS2_NA.rename(columns={'NA_Sales': 'PS2'})


#N64
df_N64=df_new.loc[df_new['Platform']=='N64']
df_N64_NA = df_N64.sum()
df_N64_NA1=df_N64_NA.rename(columns={'NA_Sales': 'N64'})

#Wii
df_Wii=df_new.loc[df_new['Platform']=='Wii']
df_Wii_NA = df_Wii.sum()
df_Wii_NA1=df_Wii_NA.rename(columns={'NA_Sales': 'Wii'})

#PC
df_PC=df_new.loc[df_new['Platform']=='PC']
df_PC_NA = df_PC.sum()
df_PC_NA1=df_PC_NA.rename(columns={'NA_Sales': 'PC'})

#GBA
df_GBA=df_new.loc[df_new['Platform']=='GBA']
df_GBA_NA = df_GBA.sum()
df_GBA_NA1=df_GBA_NA.rename(columns={'NA_Sales': 'GBA'})


#WiiU
df_WiiU=df_new.loc[df_new['Platform']=='WiiU']
df_WiiU_NA = df_WiiU.sum()
df_WiiU_NA1=df_WiiU_NA.rename(columns={'NA_Sales': 'WiiU'})


#PS
df_PS=df_new.loc[df_new['Platform']=='PS']
df_PS_NA = df_PS.sum()
df_PS_NA1=df_PS_NA.rename(columns={'NA_Sales': 'PS'})

#XB
df_XB=df_new.loc[df_new['Platform']=='XB']
df_XB_NA = df_XB.sum()
df_XB_NA1=df_XB_NA.rename(columns={'NA_Sales': 'XB'})



#XOne
df_XOne=df_new.loc[df_new['Platform']=='XOne']
df_XOne_NA = df_XOne.sum()
df_XOne_NA1=df_XOne_NA.rename(columns={'NA_Sales': 'XOne'})


#3DS
df_3DS=df_new.loc[df_new['Platform']=='3DS']
df_3DS_NA = df_3DS.sum()
df_3DS_NA1=df_3DS_NA.rename(columns={'NA_Sales': '3DS'})

#GC
df_GC=df_new.loc[df_new['Platform']=='GC']
df_GC_NA = df_GC.sum()
df_GC_NA1=df_GC_NA.rename(columns={'NA_Sales': 'GC'})

#PSV
df_PSV=df_new.loc[df_new['Platform']=='PSV']
df_PSV_NA = df_PSV.sum()
df_PSV_NA1=df_PSV_NA.rename(columns={'NA_Sales': 'PSV'})

#NES
df_NES=df_new.loc[df_new['Platform']=='NES']
df_NES_NA = df_NES.sum()
df_NES_NA1=df_NES_NA.rename(columns={'NA_Sales': 'NES'})

#2600
df_2600=df_new.loc[df_new['Platform']=='2600']
df_2600_NA = df_2600.sum()
df_2600_NA1=df_2600_NA.rename(columns={'NA_Sales': '2600'})

#SNES
df_SNES=df_new.loc[df_new['Platform']=='SNES']
df_SNES_NA = df_SNES.sum()
df_SNES_NA1=df_SNES_NA.rename(columns={'NA_Sales': 'SNES'})

#GEN
df_GEN=df_new.loc[df_new['Platform']=='GEN']
df_GEN_NA = df_GEN.sum()
df_GEN_NA1=df_GEN_NA.rename(columns={'NA_Sales': 'GEN'})

#SAT
df_SAT=df_new.loc[df_new['Platform']=='SAT']
df_SAT_NA = df_SAT.sum()
df_SAT_NA1=df_SAT_NA.rename(columns={'NA_Sales': 'SAT'})


# In[26]:


df_PS3_NA1


# In[27]:


df_X360_NA1


# In[28]:


df_PS4_NA1


# In[29]:


df_DS_NA1


# In[30]:


df_PSP_NA1


# In[31]:


df_PS2_NA1


# In[32]:


df_N64_NA1


# In[33]:


df_Wii_NA1


# In[34]:


df_PC_NA1


# In[35]:


df_GBA_NA1


# In[36]:


df_WiiU_NA1


# In[37]:


df_PS_NA1


# In[38]:


df_XB_NA1


# In[39]:


df_XOne_NA1


# In[40]:


df_3DS_NA1


# In[41]:


df_GC_NA1


# In[42]:


df_PSV_NA1


# In[43]:


df_NES_NA1


# In[44]:


df_2600_NA1


# In[45]:


df_SNES_NA1


# In[46]:


df_GEN_NA1


# In[47]:


df_SAT_NA1


# In[48]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

plt.figure(figsize=(6,9)) 


labels = ['X360','PS2','Wii','PS3','DS','PS','GBA','XB','N64','GC','NES','PSP','PS4','PC','2600','XOne',
          '3DS','SNES','WiiU','GEN','PSV','SAT']
sizes = [601.05, 583.84, 507.71, 392.26, 390.71, 336.51, 187.54, 186.69, 139.02, 133.46, 125.94, 108.99, 96.8, 93.28, 90.6, 83.19, 78.87, 
         61.23, 38.32, 19.27, 16.2, 0.72] 
         
colors = ['salmon','yellowgreen','coral','yellow','c','purple','orange','pink','gray','orangered','lightcyan','salmon','mistyrose','sandybrown','orchid','mediumpurple','tan'] 
explode = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) 

patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', 
                      shadow = False, 
                      startangle =90, 
                      pctdistance = 0.6) 
plt.axis('equal')
plt.show()


# In[49]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#JP
df =pd. read_csv('vgsales.csv')
df_new=df.loc[:,['Platform','JP_Sales']]


#PS3
df_PS3=df_new.loc[df_new['Platform']=='PS3']
df_PS3_JP = df_PS3.sum()
df_PS3_JP1=df_PS3_JP.rename(columns={'JP_Sales': 'PS3'})

#X360
df_X360=df_new.loc[df_new['Platform']=='X360']
df_X360_JP = df_X360.sum()
df_X360_JP1=df_X360_JP.rename(columns={'JP_Sales': 'X360'})

#PS4
df_PS4=df_new.loc[df_new['Platform']=='PS4']
df_PS4_JP = df_PS4.sum()
df_PS4_JP1=df_PS4_JP.rename(columns={'JP_Sales': 'PS4'})

#DS
df_DS=df_new.loc[df_new['Platform']=='DS']
df_DS_JP = df_DS.sum()
df_DS_JP1=df_DS_JP.rename(columns={'JP_Sales': 'DS'})

#PSP
df_PSP=df_new.loc[df_new['Platform']=='PSP']
df_PSP_JP = df_PSP.sum()
df_PSP_JP1=df_PSP_JP.rename(columns={'JP_Sales': 'PSP'})

#PS2
df_PS2=df_new.loc[df_new['Platform']=='PS2']
df_PS2_JP = df_PS2.sum()
df_PS2_JP1=df_PS2_JP.rename(columns={'JP_Sales': 'PS2'})


#N64
df_N64=df_new.loc[df_new['Platform']=='N64']
df_N64_JP = df_N64.sum()
df_N64_JP1=df_N64_JP.rename(columns={'JP_Sales': 'N64'})

#Wii
df_Wii=df_new.loc[df_new['Platform']=='Wii']
df_Wii_JP = df_Wii.sum()
df_Wii_JP1=df_Wii_JP.rename(columns={'JP_Sales': 'Wii'})

#PC
df_PC=df_new.loc[df_new['Platform']=='PC']
df_PC_JP = df_PC.sum()
df_PC_JP1=df_PC_JP.rename(columns={'JP_Sales': 'PC'})

#GBA
df_GBA=df_new.loc[df_new['Platform']=='GBA']
df_GBA_JP = df_GBA.sum()
df_GBA_JP1=df_GBA_JP.rename(columns={'JP_Sales': 'GBA'})


#WiiU
df_WiiU=df_new.loc[df_new['Platform']=='WiiU']
df_WiiU_JP = df_WiiU.sum()
df_WiiU_JP1=df_WiiU_JP.rename(columns={'JP_Sales': 'WiiU'})


#PS
df_PS=df_new.loc[df_new['Platform']=='PS']
df_PS_JP = df_PS.sum()
df_PS_JP1=df_PS_JP.rename(columns={'JP_Sales': 'PS'})

#XB
df_XB=df_new.loc[df_new['Platform']=='XB']
df_XB_JP = df_XB.sum()
df_XB_JP1=df_XB_JP.rename(columns={'JP_Sales': 'XB'})



#XOne
df_XOne=df_new.loc[df_new['Platform']=='XOne']
df_XOne_JP = df_XOne.sum()
df_XOne_JP1=df_XOne_JP.rename(columns={'JP_Sales': 'XOne'})


#3DS
df_3DS=df_new.loc[df_new['Platform']=='3DS']
df_3DS_JP = df_3DS.sum()
df_3DS_JP1=df_3DS_JP.rename(columns={'JP_Sales': '3DS'})

#GC
df_GC=df_new.loc[df_new['Platform']=='GC']
df_GC_JP = df_GC.sum()
df_GC_JP1=df_GC_JP.rename(columns={'JP_Sales': 'GC'})

#PSV
df_PSV=df_new.loc[df_new['Platform']=='PSV']
df_PSV_JP = df_PSV.sum()
df_PSV_JP1=df_PSV_JP.rename(columns={'JP_Sales': 'PSV'})

#NES
df_NES=df_new.loc[df_new['Platform']=='NES']
df_NES_JP = df_NES.sum()
df_NES_JP1=df_NES_JP.rename(columns={'JP_Sales': 'NES'})

#2600
df_2600=df_new.loc[df_new['Platform']=='2600']
df_2600_JP = df_2600.sum()
df_2600_JP1=df_2600_NA.rename(columns={'NA_Sales': '2600'})

#SNES
df_SNES=df_new.loc[df_new['Platform']=='SNES']
df_SNES_JP = df_SNES.sum()
df_SNES_JP1=df_SNES_JP.rename(columns={'JP_Sales': 'SNES'})

#GEN
df_GEN=df_new.loc[df_new['Platform']=='GEN']
df_GEN_JP = df_GEN.sum()
df_GEN_JP1=df_GEN_JP.rename(columns={'JP_Sales': 'GEN'})

#SAT
df_SAT=df_new.loc[df_new['Platform']=='SAT']
df_SAT_JP = df_SAT.sum()
df_SAT_JP1=df_SAT_JP.rename(columns={'JP_Sales': 'SAT'})


# In[50]:


df_PS3_JP1


# In[51]:


df_X360_JP1


# In[52]:


df_PS4_JP1


# In[53]:


df_DS_JP1


# In[54]:


df_PSP_JP1


# In[55]:


df_PS2_JP1


# In[56]:


df_N64_JP1


# In[57]:


df_Wii_JP1


# In[58]:


df_PC_JP1


# In[59]:


df_GBA_JP1


# In[60]:


df_WiiU_JP1


# In[61]:


df_PS_JP1


# In[62]:


df_XB_JP1


# In[63]:


df_XOne_JP1


# In[64]:


df_3DS_JP1


# In[65]:


df_GC_JP1


# In[66]:


df_PSV_JP1


# In[67]:


df_NES_JP1


# In[68]:


df_2600_JP1


# In[69]:


df_SNES_JP1


# In[70]:


df_GEN_JP1


# In[71]:


df_SAT_JP1


# In[72]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

plt.figure(figsize=(6,9)) 


labels = ['DS','PS','PS2','SNES','NES','3DS','2600','PS3','PSP','Wii','GBA','N64','SAT','GC','PSV','PS4',
          'WiiU','X360','GEN','XB','XOne','PC']
sizes = [175.57, 139.82, 139.2, 116.55, 98.65, 97.35, 90.6, 79.99, 76.79, 69.35, 47.33, 34.22, 32.26, 21.58, 20.96, 14.3, 12.79, 12.43, 
         2.67, 1.38, 0.34, 0.17] 
         
colors = ['salmon','yellowgreen','coral','yellow','c','purple','orange','pink','gray','orangered','lightcyan','salmon','mistyrose','sandybrown','orchid','mediumpurple','tan'] 
explode = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) 

patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', 
                      shadow = False, 
                      startangle =90, 
                      pctdistance = 0.6) 
plt.axis('equal')
plt.show()


# In[73]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Other
df =pd. read_csv('vgsales.csv')
df_new=df.loc[:,['Platform','Other_Sales']]


#PS3
df_PS3=df_new.loc[df_new['Platform']=='PS3']
df_PS3_Other = df_PS3.sum()
df_PS3_Other1=df_PS3_Other.rename(columns={'Other_Sales': 'PS3'})

#X360
df_X360=df_new.loc[df_new['Platform']=='X360']
df_X360_Other = df_X360.sum()
df_X360_Other1=df_X360_Other.rename(columns={'Other_Sales': 'X360'})

#PS4
df_PS4=df_new.loc[df_new['Platform']=='PS4']
df_PS4_Other = df_PS4.sum()
df_PS4_Other1=df_PS4_Other.rename(columns={'Other_Sales': 'PS4'})

#DS
df_DS=df_new.loc[df_new['Platform']=='DS']
df_DS_Other = df_DS.sum()
df_DS_Other1=df_DS_Other.rename(columns={'Other_Sales': 'DS'})

#PSP
df_PSP=df_new.loc[df_new['Platform']=='PSP']
df_PSP_Other = df_PSP.sum()
df_PSP_Other1=df_PSP_Other.rename(columns={'Other_Sales': 'PSP'})

#PS2
df_PS2=df_new.loc[df_new['Platform']=='PS2']
df_PS2_Other = df_PS2.sum()
df_PS2_Other1=df_PS2_Other.rename(columns={'Other_Sales': 'PS2'})


#N64
df_N64=df_new.loc[df_new['Platform']=='N64']
df_N64_Other = df_N64.sum()
df_N64_Other1=df_N64_Other.rename(columns={'Other_Sales': 'N64'})

#Wii
df_Wii=df_new.loc[df_new['Platform']=='Wii']
df_Wii_Other = df_Wii.sum()
df_Wii_Other1=df_Wii_Other.rename(columns={'Other_Sales': 'Wii'})

#PC
df_PC=df_new.loc[df_new['Platform']=='PC']
df_PC_Other = df_PC.sum()
df_PC_Other1=df_PC_Other.rename(columns={'Other_Sales': 'PC'})

#GBA
df_GBA=df_new.loc[df_new['Platform']=='GBA']
df_GBA_Other = df_GBA.sum()
df_GBA_Other1=df_GBA_Other.rename(columns={'Other_Sales': 'GBA'})


#WiiU
df_WiiU=df_new.loc[df_new['Platform']=='WiiU']
df_WiiU_Other = df_WiiU.sum()
df_WiiU_Other1=df_WiiU_Other.rename(columns={'Other_Sales': 'WiiU'})


#PS
df_PS=df_new.loc[df_new['Platform']=='PS']
df_PS_Other = df_PS.sum()
df_PS_Other1=df_PS_Other.rename(columns={'Other_Sales': 'PS'})

#XB
df_XB=df_new.loc[df_new['Platform']=='XB']
df_XB_Other = df_XB.sum()
df_XB_Other1=df_XB_Other.rename(columns={'Other_Sales': 'XB'})



#XOne
df_XOne=df_new.loc[df_new['Platform']=='XOne']
df_XOne_Other = df_XOne.sum()
df_XOne_Other1=df_XOne_Other.rename(columns={'Other_Sales': 'XOne'})


#3DS
df_3DS=df_new.loc[df_new['Platform']=='3DS']
df_3DS_Other = df_3DS.sum()
df_3DS_Other1=df_3DS_Other.rename(columns={'Other_Sales': '3DS'})

#GC
df_GC=df_new.loc[df_new['Platform']=='GC']
df_GC_Other = df_GC.sum()
df_GC_Other1=df_GC_Other.rename(columns={'Other_Sales': 'GC'})

#PSV
df_PSV=df_new.loc[df_new['Platform']=='PSV']
df_PSV_Other = df_PSV.sum()
df_PSV_Other1=df_PSV_Other.rename(columns={'Other_Sales': 'PSV'})

#NES
df_NES=df_new.loc[df_new['Platform']=='NES']
df_NES_Other = df_NES.sum()
df_NES_Other1=df_NES_Other.rename(columns={'Other_Sales': 'NES'})

#2600
df_2600=df_new.loc[df_new['Platform']=='2600']
df_2600_Other = df_2600.sum()
df_2600_Other1=df_2600_Other.rename(columns={'Other_Sales': '2600'})

#SNES
df_SNES=df_new.loc[df_new['Platform']=='SNES']
df_SNES_Other = df_SNES.sum()
df_SNES_Other1=df_SNES_Other.rename(columns={'Other_Sales': 'SNES'})

#GEN
df_GEN=df_new.loc[df_new['Platform']=='GEN']
df_GEN_Other = df_GEN.sum()
df_GEN_Other1=df_GEN_Other.rename(columns={'Other_Sales': 'GEN'})

#SAT
df_SAT=df_new.loc[df_new['Platform']=='SAT']
df_SAT_Other = df_SAT.sum()
df_SAT_Other1=df_SAT_Other.rename(columns={'Other_Sales': 'SAT'})


# In[74]:


df_PS3_Other1


# In[75]:


df_X360_Other1


# In[76]:


df_PS4_Other1


# In[77]:


df_DS_Other1


# In[78]:


df_PSP_Other1


# In[79]:


df_PS2_Other1


# In[80]:


df_N64_Other1


# In[81]:


df_Wii_Other1


# In[82]:


df_PC_Other1


# In[83]:


df_GBA_Other1


# In[84]:


df_WiiU_Other1


# In[85]:


df_PS_Other1


# In[86]:


df_XB_Other1


# In[87]:


df_XOne_Other1


# In[88]:


df_3DS_Other1


# In[89]:


df_GC_Other1


# In[90]:


df_PSV_Other1


# In[91]:


df_NES_Other1


# In[92]:


df_2600_Other1


# In[93]:


df_SNES_Other1


# In[94]:


df_GEN_Other1


# In[95]:


df_SAT_Other1


# In[96]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

plt.figure(figsize=(6,9)) 


labels = ['PS2','PS3','X360','Wii','DS','PS4','PSP','PS','PC','3DS','XOne','XB','PSV','GBA','WiiU','NES',
          'GC','N64','SNES','2600','GEN','SAT']
sizes = [193.44, 141.93, 85.54, 80.61, 60.53, 43.36, 42.19, 40.91, 24.86, 12.63, 11.92, 8.72, 8.45, 7.73, 6.45, 5.31, 5.18, 4.38, 3.22,
         0.91, 0.89, 0.07] 
         
colors = ['salmon','yellowgreen','coral','yellow','c','purple','orange','pink','gray','orangered','lightcyan','salmon','mistyrose','sandybrown','orchid','mediumpurple','tan'] 
explode = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) 

patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', 
                      shadow = False, 
                      startangle =90, 
                      pctdistance = 0.6) 
plt.axis('equal')
plt.show()


# In[97]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Global
df =pd. read_csv('vgsales.csv')
df_new=df.loc[:,['Platform','Global_Sales']]


#PS3
df_PS3=df_new.loc[df_new['Platform']=='PS3']
df_PS3_Global = df_PS3.sum()
df_PS3_Global1=df_PS3_Global.rename(columns={'Global_Sales': 'PS3'})

#X360
df_X360=df_new.loc[df_new['Platform']=='X360']
df_X360_Global = df_X360.sum()
df_X360_Global1=df_X360_Global.rename(columns={'Global_Sales': 'X360'})

#PS4
df_PS4=df_new.loc[df_new['Platform']=='PS4']
df_PS4_Global = df_PS4.sum()
df_PS4_Global1=df_PS4_Global.rename(columns={'Global_Sales': 'PS4'})

#DS
df_DS=df_new.loc[df_new['Platform']=='DS']
df_DS_Global = df_DS.sum()
df_DS_Global1=df_DS_Global.rename(columns={'Global_Sales': 'DS'})

#PSP
df_PSP=df_new.loc[df_new['Platform']=='PSP']
df_PSP_Global = df_PSP.sum()
df_PSP_Global1=df_PSP_Global.rename(columns={'Global_Sales': 'PSP'})

#PS2
df_PS2=df_new.loc[df_new['Platform']=='PS2']
df_PS2_Global = df_PS2.sum()
df_PS2_Global1=df_PS2_Global.rename(columns={'Global_Sales': 'PS2'})


#N64
df_N64=df_new.loc[df_new['Platform']=='N64']
df_N64_Global = df_N64.sum()
df_N64_Global1=df_N64_Global.rename(columns={'Global_Sales': 'N64'})

#Wii
df_Wii=df_new.loc[df_new['Platform']=='Wii']
df_Wii_Global = df_Wii.sum()
df_Wii_Global1=df_Wii_Global.rename(columns={'Global_Sales': 'Wii'})

#PC
df_PC=df_new.loc[df_new['Platform']=='PC']
df_PC_Global = df_PC.sum()
df_PC_Global1=df_PC_Global.rename(columns={'Global_Sales': 'PC'})

#GBA
df_GBA=df_new.loc[df_new['Platform']=='GBA']
df_GBA_Global = df_GBA.sum()
df_GBA_Global1=df_GBA_Global.rename(columns={'Global_Sales': 'GBA'})


#WiiU
df_WiiU=df_new.loc[df_new['Platform']=='WiiU']
df_WiiU_Global = df_WiiU.sum()
df_WiiU_Global1=df_WiiU_Global.rename(columns={'Global_Sales': 'WiiU'})


#PS
df_PS=df_new.loc[df_new['Platform']=='PS']
df_PS_Global = df_PS.sum()
df_PS_Global1=df_PS_Global.rename(columns={'Global_Sales': 'PS'})

#XB
df_XB=df_new.loc[df_new['Platform']=='XB']
df_XB_Global = df_XB.sum()
df_XB_Global1=df_XB_Global.rename(columns={'Global_Sales': 'XB'})



#XOne
df_XOne=df_new.loc[df_new['Platform']=='XOne']
df_XOne_Global = df_XOne.sum()
df_XOne_Global1=df_XOne_Global.rename(columns={'Global_Sales': 'XOne'})


#3DS
df_3DS=df_new.loc[df_new['Platform']=='3DS']
df_3DS_Global = df_3DS.sum()
df_3DS_Global1=df_3DS_Global.rename(columns={'Global_Sales': '3DS'})

#GC
df_GC=df_new.loc[df_new['Platform']=='GC']
df_GC_Global = df_GC.sum()
df_GC_Global1=df_GC_Global.rename(columns={'Global_Sales': 'GC'})

#PSV
df_PSV=df_new.loc[df_new['Platform']=='PSV']
df_PSV_Global = df_PSV.sum()
df_PSV_Global1=df_PSV_Global.rename(columns={'Global_Sales': 'PSV'})

#NES
df_NES=df_new.loc[df_new['Platform']=='NES']
df_NES_Global = df_NES.sum()
df_NES_Global1=df_NES_Global.rename(columns={'Global_Sales': 'NES'})

#2600
df_2600=df_new.loc[df_new['Platform']=='2600']
df_2600_Global = df_2600.sum()
df_2600_Global1=df_2600_Global.rename(columns={'Global_Sales': '2600'})

#SNES
df_SNES=df_new.loc[df_new['Platform']=='SNES']
df_SNES_Global = df_SNES.sum()
df_SNES_Global1=df_SNES_Global.rename(columns={'Global_Sales': 'SNES'})

#GEN
df_GEN=df_new.loc[df_new['Platform']=='GEN']
df_GEN_Global = df_GEN.sum()
df_GEN_Global1=df_GEN_Global.rename(columns={'Global_Sales': 'GEN'})

#SAT
df_SAT=df_new.loc[df_new['Platform']=='SAT']
df_SAT_Global = df_SAT.sum()
df_SAT_Global1=df_SAT_Global.rename(columns={'Global_Sales': 'SAT'})


# In[98]:


df_PS3_Global1


# In[99]:


df_X360_Global1


# In[100]:


df_PS4_Global1


# In[101]:


df_DS_Global1


# In[102]:


df_PSP_Global1


# In[103]:


df_PS2_Global1


# In[104]:


df_N64_Global1


# In[105]:


df_Wii_Global1


# In[106]:


df_PC_Global1


# In[107]:


df_GBA_Global1


# In[108]:


df_WiiU_Global1


# In[109]:


df_PS_Global1


# In[110]:


df_XB_Global1


# In[111]:


df_XOne_Global1


# In[112]:


df_3DS_Global1


# In[113]:


df_GC_Global1


# In[114]:


df_PSV_Global1


# In[115]:


df_NES_Global1


# In[116]:


df_2600_Global1


# In[117]:


df_SNES_Global1


# In[118]:


df_GEN_Global1


# In[119]:


df_SAT_Global1


# In[120]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

plt.figure(figsize=(6,9)) 


labels = ['PS2','X360','PS3','Wii','DS','PS','GBA','PSP','PS4','PC','XB','NES','3DS','N64','SNES',
          'GC','XOne','2600','WiiU','PSV','SAT','GEN']
sizes = [1255.64, 979.96, 957.84, 926.71, 822.49, 730.66, 318.5, 296.28, 278.1, 258.82, 258.26, 251.07, 247.46, 218.88, 200.05, 199.36, 
         141.06, 97.08, 81.86, 61.93, 33.59, 28.36] 
         
colors = ['salmon','yellowgreen','coral','yellow','c','purple','orange','pink','gray','orangered','lightcyan','salmon','mistyrose','sandybrown','orchid','mediumpurple','tan'] 
explode = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) 

patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', 
                      shadow = False, 
                      startangle =90, 
                      pctdistance = 0.6) 
plt.axis('equal')
plt.show()

