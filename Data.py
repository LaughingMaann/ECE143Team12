
# coding: utf-8

# In[6]:


def Data_form(df):
    '''
    Fromalizing data
    '''
    import numpy as np
    import colorsys
    import pandas as pd 
    import seaborn as sns
    import matplotlib.pyplot as plt
    import BarChart_plt
    get_ipython().run_line_magic('matplotlib', 'inline')
    assert isinstance(df, pd.core.frame.DataFrame)
    assert 'Year' in df
    #Cleaning data. only save data before 2016
    df=df[df['Year'] <= 2016]

    #rename Platform label
    df["Platform" ] = df["Platform"].replace(["GB", "NES", "DS", "X360", "SNES", "GBA", "3DS", "N64", "PS", "XB", "XOne", "PSV", "TG16", "3DO", "PCFX"],
        ["Game Boy", "Nintendo Entertainment System", "Nintendo DS", "Xbox 360","Super Nintendo Entertainment System","Nintendo Game Boy Advance", "Nintendo 3DS", "Nintendo 64","PlayStation","Xbox","Xbox One", "PlayStation Vita", "TurboGrafx-16","3DO Interactive Multiplayer", "NEC PC‑FX"])
    PlayStation = ['PS3', 'PS4', 'PS2', 'PlayStation', 'PSP', 'PlayStation Vita']
    Nintendo = ['Wii', 'Nintendo Entertainment System', 'Game Boy','Nintendo DS', 'Super Nintendo Entertainment System', 'Nintendo Game Boy Advance','Nintendo 3DS', 'Nintendo 64','WiiU']
    Microsoft = ['Xbox', 'Xbox One', 'Xbox 360']
    Other = ['PC', '2600', 'GC', 'GEN', 'DC', 'SAT', 'SCD', 'WS', 'NG', 'TurboGrafx-16', '3DO Interactive Multiplayer', 'GG', 'NEC PC‑FX']
    #plot total sales on different regions.
    return df


# In[9]:


def Data_a(df):
    '''
    Return a new datafram that have a Column "Ave"
    '''
    import numpy as np
    import colorsys
    import pandas as pd 
    import seaborn as sns
    import matplotlib.pyplot as plt
    import BarChart_plt
    get_ipython().run_line_magic('matplotlib', 'inline')
    assert isinstance(df, pd.core.frame.DataFrame)
    assert 'Year' in df
    #rename columns with understandable name tage
    df1=df.rename(index=str, columns={"NA_Sales": "North America", "EU_Sales": "Europe","JP_Sales": "Japan","Other_Sales": "Other"})
    df1=df1.loc[:, 'Name': 'Global_Sales'].sort_values(by="Global_Sales", ascending=True).tail(10)
    return df1


# In[2]:


def Data_ave(df):
    '''
    Return a new datafram that have a Column "Ave"
    '''
    import numpy as np
    import colorsys
    import pandas as pd 
    import seaborn as sns
    import matplotlib.pyplot as plt
    import BarChart_plt
    get_ipython().run_line_magic('matplotlib', 'inline')
    assert isinstance(df, pd.core.frame.DataFrame)
    assert 'Year' in df
    #rename columns with understandable name tage
    df2=df.rename(index=str, columns={"NA_Sales": "North America", "EU_Sales": "Europe","JP_Sales": "Japan","Other_Sales": "Other"})
    #only take top 1000 games sales into calculatoin
    df2=df2.loc[:, 'Name': 'Global_Sales'].sort_values(by="Global_Sales", ascending=False).head(1000)
    #calculate avergae salses of top 10 sale games
    df2['Ave'] = df2['Global_Sales']/(2017-df2['Year'])
    df2=df2.loc[:, 'Name': 'Ave'].sort_values(by="Ave", ascending=True).tail(10)
    return df2


# In[5]:


def plot_compare(df):
    '''
    deviede data to before 2011 and data after 2011,and plot the bar chart
    '''
    import numpy as np
    import colorsys
    import pandas as pd 
    import seaborn as sns
    import matplotlib.pyplot as plt
    import BarChart_plt
    get_ipython().run_line_magic('matplotlib', 'inline')
    assert isinstance(df, pd.core.frame.DataFrame)
    assert 'Year' in df
    PlayStation = ['PS3', 'PS4', 'PS2', 'PlayStation', 'PSP', 'PlayStation Vita']
    Nintendo = ['Wii', 'Nintendo Entertainment System', 'Game Boy','Nintendo DS', 'Super Nintendo Entertainment System', 'Nintendo Game Boy Advance','Nintendo 3DS', 'Nintendo 64','WiiU']
    Microsoft = ['Xbox', 'Xbox One', 'Xbox 360']
    Other = ['PC', '2600', 'GC', 'GEN', 'DC', 'SAT', 'SCD', 'WS', 'NG', 'TurboGrafx-16', '3DO Interactive Multiplayer', 'GG', 'NEC PC‑FX']
    def Platf (c):
        '''
        Merge platform into larger category
        input: Panda dataframe
        '''
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
    df['Platf'] = df.apply(Platf, axis=1)
    #deviede data to before 2011 and data after 2011
    before=df[(df["Year"]>=2005) & (df["Year"]<2011)].groupby("Platf")['Global_Sales'].sum().sort_values(ascending = False).reset_index()

    after=df[(df["Year"]>=2011) & (df["Year"]<2017)].groupby("Platf")['Global_Sales'].sum().sort_values(ascending = False).reset_index()
    return BarChart_plt.comp_bar(before,after,"c")

