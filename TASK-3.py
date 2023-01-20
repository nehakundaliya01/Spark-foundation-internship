#!/usr/bin/env python
# coding: utf-8

# # SPARK FOUNDATION
# # TASK-3
# Find out the weak areas where you can
# work to make more profit.
# What all business problems you can derive by exploring the data?
# 
# Done by : NEHA KUNDALIYA

# # Importing Libraries

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r'C:\Users\WIN 10\Downloads\SampleSuperstore.csv')


# In[2]:


data.head()


# # Treating Null Values

# In[3]:


data.isnull().sum()


# In[4]:


dir(data)


# In[5]:


data.nunique()


# In[6]:


#only one country is there
data.describe()


# In[7]:


y= data.groupby(['Segment'])['Profit'].sum().reset_index(name='Profits')
plt.bar(y.Segment,y.Profits,width=0.4,color='yellow')


# In[8]:


x= data.groupby(['Segment'])['Sales'].sum().reset_index(name='sales')
plt.bar(x.Segment,x.sales,width=0.4,color='green')


# In[35]:


x= data.groupby(['Segment'])['Quantity'].sum().reset_index(name='quantity')
plt.pie(x.quantity,labels=x.Segment)


# In[10]:


data.groupby(['Ship Mode'])[['Quantity','Discount','Profit']].sum().sort_values(by=['Profit'],ascending=False)


# In[11]:


data.groupby(['Region'])[['Quantity','Discount','Profit']].sum().sort_values(by='Profit',ascending=False)


# In[12]:


data.groupby(['Ship Mode','Region'])['Quantity'].sum().reset_index(name='QUANTITY').sort_values(by='QUANTITY',ascending=False)


# In[13]:


data.groupby(['Region','Segment'])['Profit'].sum().reset_index(name='Profit').sort_values(by='Profit',ascending=False)


# In[27]:


l1 = data.groupby(['City'])['Sales'].sum().reset_index(name='Sales').sort_values(by='Sales',ascending=False).tail()
sns.barplot(l1.City,l1.Sales,color='red')


# In[28]:


h1 = data.groupby(['City'])['Sales'].sum().reset_index(name='Sales').sort_values(by='Sales',ascending=False).head()
sns.barplot(h1.City,h1.Sales,color='green')


# # CONCLUSION

# 1.The same-day shipping technique needs improvement because it sells fewer items than other shipping methods.
# 
# 2.They must work in the South because there are less sales, particularly in the corporate and home office divisions.
# 
# 3.Sales in the consumer category are the highest, allowing companies to offer a wider range of consumable goods because customers will be prepared to pay more for them.
# 
# 4.The west region has the largest sales in the consumer and business segments.They can therefore benefit more from this area.
# 
# 5.The least quantity of sales are in cities like Elyria, Jupiter, and Abilene.
# Therefore, they are learning how to work in these cities.
# 
# 6.Sales are higher in New York.
# As a result, that city can produce more sales.
