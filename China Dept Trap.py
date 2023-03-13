#!/usr/bin/env python
# coding: utf-8

# ### importing Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


import plotly.express as px


# ### TO load the dataset

# In[3]:


china_data = pd.read_csv("china_dept_trap.csv")


# In[4]:


china_data.head()


# In[5]:


china_data.tail()


# In[6]:


china_data.shape


# In[7]:


china_data.columns


# In[8]:


china_data.duplicated().sum()


# In[9]:


china_data.isnull().sum()


# In[10]:


china_data.info()


# In[11]:


china_data.describe()


# In[12]:


china_data.dropna(inplace = True)


# In[13]:


china_data.nunique()


# In[14]:


china_data = china_data.rename(columns = {'Expand All | Collapse All' : 'Title'})


# In[15]:


china_data['YEAR'].unique()


# In[16]:


china_data['YEAR'].value_counts()


# ### Visualization of investment in each year

# In[17]:


plt.figure(figsize=(15,6))
sns.countplot('YEAR', data = china_data, palette='rocket')
plt.xticks(rotation = 90)
plt.show()


# In[18]:


plt.figure(figsize=(10,20)) 
plt.pie(china_data['YEAR'].value_counts(), labels=china_data['YEAR'].value_counts().index, autopct='%1.1f%%', textprops={ 'fontsize': 15,
                                           'color': 'black',
                                           'weight': 'bold',
                                           'family': 'serif' }) 
hfont = {'fontname':'serif', 'weight': 'bold'}
plt.title('YEAR', size=20, **hfont) 
plt.show()


# In[19]:


china_data['LENDER'].unique()


# In[20]:


china_data['LENDER'].value_counts()


# ### Visualization of Lenders

# In[21]:


plt.figure(figsize=(15,6))
sns.countplot('LENDER', data = china_data, palette='hls')
plt.xticks(rotation = 90)
plt.show()


# In[22]:


plt.figure(figsize=(30,20)) 
plt.pie(china_data['LENDER'].value_counts(), labels=china_data['LENDER'].value_counts().index, autopct='%1.1f%%', textprops={ 'fontsize': 25,
                                           'color': 'black',
                                           'weight': 'bold',
                                           'family': 'serif' }) 
hfont = {'fontname':'serif', 'weight': 'bold'}
plt.title('LENDER', size=20, **hfont) 
plt.show()


# ### According to the visualization we found out that the EXIMBANK has the higher lender percentage

# In[23]:


china_data['SECTOR'].unique()


# In[24]:


china_data['SECTOR'].value_counts()


# ### Visualization of  Sector of Investment

# In[25]:


plt.figure(figsize=(15,6))
sns.countplot('SECTOR', data = china_data, palette='hls')
plt.xticks(rotation = 90)
plt.show()


# In[26]:


plt.figure(figsize=(30,20)) 
plt.pie(china_data['SECTOR'].value_counts(), labels=china_data['SECTOR'].value_counts().index, autopct='%1.1f%%', textprops={ 'fontsize': 25,
                                           'color': 'black',
                                           'weight': 'bold',
                                           'family': 'serif' }) 
hfont = {'fontname':'serif', 'weight': 'bold'}
plt.title('SECTOR', size=20, **hfont) 
plt.show()


# #### According to visualization we found out that Transfortaion is the highest sector of investment

# In[27]:


china_data['SENSITIVE TERRITORY OVERLAP'].unique()


# In[28]:


china_data['SENSITIVE TERRITORY OVERLAP'].value_counts()


# ### Visualization of SENSITIVE TERRITORY OVERLAP

# In[29]:


plt.figure(figsize=(15,6))
sns.countplot('SENSITIVE TERRITORY OVERLAP', data = china_data, palette='hls')
plt.xticks(rotation = 90)
plt.show()


# In[30]:


plt.figure(figsize=(30,20)) 
plt.pie(china_data['SENSITIVE TERRITORY OVERLAP'].value_counts(), labels=china_data['SENSITIVE TERRITORY OVERLAP'].value_counts().index, autopct='%1.1f%%', textprops={ 'fontsize': 25,
                                           'color': 'black',
                                           'weight': 'bold',
                                           'family': 'serif' }) 
hfont = {'fontname':'serif', 'weight': 'bold'}
plt.title('SENSITIVE TERRITORY OVERLAP', size=20, **hfont) 
plt.show()


# In[31]:


china_data['Country'].unique()


# In[32]:


china_data['Country'].value_counts()


# ### Visualization of contries Invested

# In[33]:


plt.figure(figsize=(20,8))
sns.countplot('Country', data = china_data, palette='hls')
plt.xticks(rotation = 90)
plt.show()


# #### To wraggel the amount data column  into the interger format

# In[34]:


def amount(a):
    y=a
    if ',' in a:
        a=a.replace(',','')
    a=float(a[1:-1])
    if y[-1]=='M':
        return a*1000000
    elif y[-1]=='B':
        return a*1000000000
    else:
        return 'Please check'


# In[35]:


china_data['AMOUNT']=china_data['AMOUNT'].apply(amount)


# In[36]:


china_data.head()


# In[37]:


plt.figure(figsize=(20,8))
sns.barplot(x = 'Country',y = 'AMOUNT', ci = None, data = china_data.head(500))
plt.xticks(rotation = 90)
plt.show()


# In[38]:


plt.figure(figsize=(20,8))
sns.lineplot(x = 'Country',y = 'YEAR', data = china_data)
plt.xticks(rotation = 90)
plt.show()


# In[39]:


fig6 = px.histogram(china_data, 
                    x = "Country", color = "SECTOR")
fig6.show()


# In[41]:


plt.figure(figsize=(15,10))
plt.suptitle('top 25 countries on which china invested the most(world wide)',size=20,weight='bold')
data=china_data.groupby('Country').sum().reset_index().sort_values('AMOUNT',ascending=False)[['Country','AMOUNT']]
plt.subplot(1,2,1)
plt.xticks(rotation=90)
sns.barplot(data=data.head(25),x='Country',y='AMOUNT')
plt.subplot(1,2,2)
plt.axis('off')
plt.tight_layout()
plt.table(cellText=data.head(25).values, colLabels=data.columns, loc='center')


# In[45]:


plt.figure(figsize=(15,10))
plt.suptitle("top 25 countrie's Government to which china Lended the most(world wide)",size=20,weight='bold')
data=china_data[china_data['BORROWER']=='Government'].groupby('Country').sum().reset_index().sort_values('AMOUNT',ascending=False)[['Country','AMOUNT']]
plt.subplot(1,2,1)
plt.xticks(rotation=90)
sns.barplot(data=data.head(25),x='Country',y='AMOUNT')
plt.subplot(1,2,2)
plt.axis('off')
plt.tight_layout()
plt.table(cellText=data.head(25).values, colLabels=data.columns, loc='center')
plt.show()


# In[43]:


import textwrap


# In[44]:


country='Pakistan'
data=china_data[china_data['Country']==country]
ax=plt.figure(figsize=(15,10))
plt.suptitle(f"China's investments on {country}",weight='bold',size=20)
plt.subplot(2,2,1)
plt.title('Year-wise Investment')
sns.lineplot(data=data.groupby('YEAR').sum().reset_index(),x='YEAR',y='AMOUNT',color='r')
plt.subplot(2,2,2)
plt.title('Sector-wise Investment')
data['SECTOR'].value_counts().plot.pie(autopct='%.2f%%')
plt.subplot(2,2,3)
plt.title('Borrower-wise Amount invested')
plt.xticks(rotation=90)
ax=sns.barplot(data=data.groupby('BORROWER').sum().reset_index(),x='BORROWER',y='AMOUNT')
labels = [textwrap.fill(label.get_text(), 12) for label in ax.get_xticklabels()]
ax.set_xticklabels(labels)
plt.subplot(2,2,4)
plt.title('YEAR-wise Amount invested')
ax=sns.barplot(data=data,x='YEAR',y='AMOUNT',hue='SECTOR',ci=False)
labels = [textwrap.fill(label.get_text(), 12) for label in ax.get_xticklabels()]
display(data.sort_values('AMOUNT',ascending=False)[['YEAR','AMOUNT']].reset_index(drop=True))

