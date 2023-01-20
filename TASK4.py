#!/usr/bin/env python
# coding: utf-8

# # The Spark Foundation
# # TASK-4
# Find out the hot zone of terrorism.
# What all security issues and insights you can derive by EDA?
# 
# Done by: Neha Kundaliya

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv(r'C:\Users\WIN 10\Desktop\globalterrorismdb_0718dist.csv' , encoding='latin1')


# In[3]:


data.head()


# In[4]:


data.columns


# In[5]:


d1 = data[['iyear','imonth','country_txt',"region_txt",'city','attacktype1_txt','targtype1_txt','weaptype1_txt']]
d1.head()


# In[6]:


d1.shape


# In[7]:


d1.isnull().sum()


# In[8]:


d1.columns


# In[9]:


d1=d1.rename(columns={'iyear':'year', 'imonth':'month', 'country_txt':'country', 'region_txt':'region', 'city':'city','attacktype1_txt':'attack type', 'targtype1_txt':'target type', 'weaptype1_txt':'weapon type'})


# In[10]:


d1.head()


# In[11]:


d1 = d1.drop_duplicates()
d1.shape


# In[13]:


y1 = d1.groupby(['year'])['year'].count().reset_index(name='year_count')
sns.lineplot(y1.year,y1.year_count).set(title='Terriosim happening each year')


# In[14]:


t1=d1.groupby(['target type'])['target type'].count().reset_index(name='target_count').sort_values(by='target_count',ascending=False).head(3)
sns.barplot(t1['target type'],t1['target_count']).set(title='Most Target Groups')


# In[15]:


c1 = d1.groupby(['country'])['country'].count().reset_index(name='count').sort_values(by='count',ascending=False).head(5)
sns.barplot(c1['country'],c1['count']).set(title='Top 5 countries with most terrorism')


# In[16]:


d1['weapon type'].unique()


# In[17]:


d1['attack type'].unique()


# In[20]:


w1 = d1.groupby(['weapon type'])['weapon type'].count().reset_index(name='count')
plt.pie(w1['count'],labels=w1['weapon type'])
plt.legend()
plt.title('Weapon Types')


# In[22]:


a1 = d1.groupby(['attack type'])['attack type'].count().reset_index(name='count')
plt.pie(a1['count'],labels=a1['attack type'])
plt.legend()
plt.title('Attack Type')


# In[126]:


d1[(d1['country']=='Iraq')|(d1['country']=='Pakistan')|(d1['country']=='Iraq')|(d1['country']=='Afghanistan')|(d1['country']=='India')].groupby(['country','city'])['city'].count().reset_index(name='count').sort_values(by='count',ascending=False).head(5)


# In[23]:


d1[d1['country']=='Iraq'].groupby(['target type','attack type'])['target type'].count().reset_index(name='count').sort_values(by='count',ascending=False).head(3)


# In[24]:


d1.groupby(['region'])['region'].count().reset_index(name='count').sort_values(by='count',ascending=False).head(5)


# # Conclusion

# 1.Baghdad in particular is a terrorist hotspot in Iraq.
# 
# 2.The heat zone regions are South Asia and the Middle East and North Africa.
# 
# 3.The three target categories for terrorism are private citizens and property, the military, and the police. As a result, security can be tightened in these locations.
# 
# 4.The bombing or explosion completes the first half of the attack.
# 
# 5.Firearms and explosives are the most often utilised weapons.
# As a result, it is possible to create the necessary equipment and safety precautions for these weapons.
# 
# 6.Iraq,Pakistan,Afghanisthan,India and Colombia are the top 5 countries for terrorism.
