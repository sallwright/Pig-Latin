
# coding: utf-8

# In[9]:


import pandas as pd
df = pd.DataFrame(pd.read_csv('Pandas Exercises/Ecommerce Purchases'))


# # Finding some interesting data from the CSV file

# In[11]:


df.head()


# In[17]:


df['Purchase Price'].mean()


# In[18]:


df['Purchase Price'].max()


# In[19]:


df['Purchase Price'].min()


# In[25]:


df['Language'].value_counts().head(3)


# How many people in the data set spoke English and also ordered their product in the evening?

# In[29]:


len(df[(df['Language'] == 'en') & (df['AM or PM'] == 'PM')])


# What is the most popular email address domain?

# In[31]:


df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)


# How many different types of browser are there?

# In[33]:


df['Browser Info'].value_counts()


# How many people are using Mastercard as their card provider?

# In[34]:


len(df[df['CC Provider'] == 'Mastercard'])


# How many people have a credit card that will expire next year, 2019?

# In[42]:


len(df[df['CC Exp Date'].apply(lambda x: x[3:]) == '19'])

