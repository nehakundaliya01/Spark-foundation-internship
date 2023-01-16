#!/usr/bin/env python
# coding: utf-8

# # Spark Foundation 
# # TASK: 6
# 
# Predict the right class using Decision Tree Algorithm
# 
# Done by: NEHA KUNDALIYA

# # Importing Libraries

# In[16]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree


# # Loading Data

# In[17]:


data = pd.read_csv(r'C:\Users\WIN 10\Downloads\iris.csv')


# In[18]:


data.head()


# # Label encoders

# In[19]:


le = LabelEncoder()


# In[20]:


data['le_species'] = le.fit_transform(data['Species'])
target = data['le_species']
data


# In[21]:


data['Species'].unique()


# Therefore, by seeing the above data we can conclude: Iris_setosa = 0 Iris-versicolor = 1 Iris-virginica = 2

# In[22]:


inp = data[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
inp.head()


# # Decision Tree 

# In[23]:


dectree = tree.DecisionTreeClassifier()
dectree.fit(inp,target)


# In[24]:


dectree.score(inp,target)


# # CHECKING

# In[25]:


dectree.predict([[4.9,3.0,1.4,0.2]])

