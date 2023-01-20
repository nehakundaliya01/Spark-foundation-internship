#!/usr/bin/env python
# coding: utf-8

# # Spark Foundation
# # Task - 2
# # K-MEAN clustering algorithm
# 
# Done by- Neha Kundaliya

# In[1]:


from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt


# In[2]:


iris = pd.read_csv(r'C:\Users\WIN 10\Downloads\Iris.csv',encoding='unicode_escape')
iris.head()


# In[3]:


plt.xlabel('Sepal Length(in cm)')
plt.ylabel('Sepal Width(in cm)')
plt.scatter(iris.SepalLengthCm,iris.SepalWidthCm)


# In[4]:


scale = MinMaxScaler()
scale.fit(iris[['SepalLengthCm']])
iris.SepalLengthCm = scale.transform(iris[['SepalLengthCm']])
scale.fit(iris[['SepalWidthCm']])
iris.SepalWidthCm = scale.transform(iris[['SepalWidthCm']])


# In[5]:


iris


# In[6]:


plt.xlabel('Sepal Length(in cm)')
plt.ylabel('Sepal Width(in cm)')
plt.scatter(iris.SepalLengthCm,iris.SepalWidthCm)


# In[7]:


dir(KMeans)


# In[8]:


K = KMeans(n_clusters=2)


# In[9]:


cluster = K.fit_predict(iris[['SepalLengthCm','SepalWidthCm']])


# In[10]:


iris['sepal_cluster'] = cluster


# In[11]:


iris


# In[12]:


K.cluster_centers_


# In[13]:


df1 = iris[iris['sepal_cluster']==0]
df2 = iris[iris['sepal_cluster']==1]
plt.scatter(df1.SepalLengthCm,df1.SepalWidthCm,color='red')
plt.scatter(0.20402299, 0.54813218,color='black',marker="+")
plt.scatter(df2.SepalLengthCm,df2.SepalWidthCm)
plt.scatter(0.57035024, 0.37047101,color='black',marker="+")


# # optimum no. of clusters

# In[14]:


sse = []
k_range = range(1,10)
for k in k_range:
    K = KMeans(n_clusters = k)
    cluster=K.fit_predict(iris[['SepalLengthCm','SepalWidthCm']])
    sse.append(K.inertia_)


# In[15]:


plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_range,sse)


# # Therefore, from elbow plot we can conclude 3 is the optimum no. of clusters in sepal

# In[ ]:




