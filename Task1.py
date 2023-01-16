#!/usr/bin/env python
# coding: utf-8

# # Spark Foundation
# # TASK: 1 
# Predict the percentage of a student based on the no. of study hours.
# 
# Done by: NEHA KUNDALIYA
# 

# # Importing libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


# # Loading data

# In[6]:


students = pd.read_csv("https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv")


# In[7]:


students.head()


# # Scatter Plot

# In[8]:


plt.xlabel('Hours')
plt.ylabel('Scores')
plt.scatter(students['Hours'],students['Scores'],color='r',marker='+')


# In[9]:


Hours = students.drop('Scores',axis=1)
Hours.head()


# In[10]:


Scores = students['Scores']
Scores.head()


# # Regression model will help to predict the scores

# In[11]:


reg = linear_model.LinearRegression()
reg.fit(Hours,Scores)


# # Predicting  score if a student studies for 9.25 hrs/ day

# In[12]:


reg.intercept_


# In[13]:


reg.coef_


# In[14]:


reg.predict([[9.25]])

