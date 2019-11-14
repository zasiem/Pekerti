#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#read csv
data = pd.read_csv('pekerti.csv')
data.head()


# In[45]:


#
data_selection = data[['RPB','APSI','EA','Basdat']]
data_selection.head()


# In[46]:


#clustering 1 adalah yang cocok dengan EA yang 0 tidak cocok
cluster = KMeans(n_clusters=2).fit(data_selection)
cluster.labels_
cluster_label = cluster.predict(data_selection)
cluster_label


# In[57]:


#menambahkan label ke data
NewData = pd.DataFrame()
NewData['NIM'] = data['NIM']
NewData['Label'] = cluster_label
NewData.head()
