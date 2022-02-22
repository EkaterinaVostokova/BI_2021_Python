#!/usr/bin/env python
# coding: utf-8

# # 1. Построить гистограммы

# In[124]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[54]:


c = pd.read_csv('train.csv')


# In[52]:


c.head()


# In[ ]:


lst = pd.concat([c["A"], c["T"], c["G"], c["C"]]).dropna().tolist()
# concatenating necessary data, dropping NAs and converting to a list


# In[158]:


plt.figure(figsize=(15, 10))
plt.hist(lst, bins=100, edgecolor='black')
# plotting histogram
plt.title("Distribution of all 4 positions together")


# In[148]:


lstA = c["A"].dropna().tolist()
lstT = c["T"].dropna().tolist()
lstC = c["C"].dropna().tolist()
lstG = c["G"].dropna().tolist()


# In[159]:


plt.figure(figsize=(15, 10))
plt.hist(lstA, bins=50, color='green', label="A", edgecolor='black')
# plotting histogram
plt.hist(lstC, bins=50, color='red', label="C", edgecolor='black')
plt.hist(lstT, bins=50, color='blue', label="T", edgecolor='black')
plt.hist(lstG, bins=50, color='yellow', label="G", edgecolor='black')
plt.title("Distribution of all 4 positions")
plt.legend()


# # 2. Отбор необходимых данных

# In[125]:


train_part = c[c["matches"] > c["matches"].mean()]
# где matches больше чем среднее


# In[126]:


train_part = train_part[["pos", "reads_all", "mismatches", "deletions", "insertions"]]
# selecting specific columns


# In[128]:


train_part.to_csv('train_part.csv', index=False)


# In[ ]:


# In[ ]:


# # 3. Сделать небольшой EDA

# Moscow flat prices dataset: https://www.kaggle.com/hugoncosta/price-of-flats-in-moscow

# In[129]:


flat_df = pd.read_csv('flats_moscow.csv')


# In[130]:


flat_df.describe()


# The dataset contains columns such as Price, Total Space of Apartment, Living Space, Kitchen space, Distance to center,
# Distance to Metro, brick or not, floor.

# In[192]:


flat_df[flat_df["price"] < 100]
# checking the apartments from lower range of prices


# In[182]:


plt.figure(figsize=(15, 10))
plt.hist(flat_df["price"], bins=150, edgecolor='black', alpha=0.6)
plt.title("Distribution of prices")
plt.xlabel('price')
plt.axvline(flat_df["price"].mean(), color='k', linestyle='dashed', linewidth=2)


# In[189]:


plt.figure(figsize=(15, 10))
plt.title("Total space distribution")
sns.distplot(flat_df['totsp'], color='g', bins=100, hist_kws=dict(edgecolor="black", linewidth=2))


# In[136]:


plt.figure(figsize=(10, 10))
sns.heatmap(flat_df.corr(), cbar=True, annot=True, cmap='Blues').set_title('Correlations')


# Positive correlations with prices - total space, living space, kitchen space
# Slight negative correlations - distance from center, distance from metro

# In[179]:


plt.title("Correlations between price and total space")
sns.heatmap(pd.DataFrame(flat_df, columns=['price', 'totsp']).corr(), annot=True)
plt.show()


# In[214]:


cheap_flats = flat_df[flat_df["price"] < 95]
# 459 flats
exp_flats = flat_df[flat_df["price"] > 150]
# 395 flats
plt.figure(figsize=(15, 10))
plt.title("Comparison of kitchen space for cheap and expensive apartments")
sns.distplot(cheap_flats['kitsp'], color='g', hist_kws=dict(edgecolor="black", linewidth=2), label="cheap flats")
sns.distplot(exp_flats['kitsp'], color='b', hist_kws=dict(edgecolor="black", linewidth=2), label="exp flats")
plt.legend()


# In[ ]:


# As we see, cheaper flats have smaller kitchen spaces
