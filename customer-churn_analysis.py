#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # read dataset

# In[5]:


df=pd.read_csv("customer churn.csv")


# In[6]:


df


# # understand dataset

# In[7]:


df.head()


# In[8]:


df.tail()


# In[9]:


df.info()


# In[ ]:


#replace blanks with 0 as tenure and no total charges are recorded


# In[18]:


df["TotalCharges"]=df["TotalCharges"].replace(" ","0")
df["TotalCharges"]=df["TotalCharges"].astype("float")


# In[19]:


df.info()


# In[20]:


df.isnull()


# In[21]:


df.isnull().sum()


# In[25]:


df.duplicated().sum()


# In[26]:


df["customerID"].duplicated().sum()


# In[22]:


df.describe()


# In[23]:


df.columns


# In[ ]:


#convert in columns SeniorCitizen 1= yes and 0 = no


# In[28]:


def conv(value):
    if value==1:
        return "yes"
    else:
        return "no"
df["SeniorCitizen"]=df['SeniorCitizen'].apply(conv)


# In[29]:


df


# # EDA perform

# In[45]:


plt.figure(figsize=(10,7
                   ))
ax=sns.countplot(x=df['Churn'],data=df)
ax.bar_label(ax.containers[0])
plt.title("count of coustmers by churns")
plt.show()


# In[46]:


gb=df.groupby("Churn").agg({"Churn":"count"})
gb


# In[50]:


plt.figure(figsize=(10,7))

plt.pie(gb["Churn"],labels=gb.index,autopct="%1.2f%%")
plt.title('% of churned  coustmers ',fontsize=20)

plt.show()


# #from the given pie charts we can conclude that 26.54% of our custmers have churnesd out .

#  explore on the basis of gender 

# In[77]:


plt.figure(figsize=(9,7
                   ))
ax=sns.countplot(x='gender',data=df,hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("count of coustmers churned out  on the basis of gender")
plt.show()


# no major impacts on the basis of gender 

# In[59]:


data = df.groupby(['SeniorCitizen', 'Churn']).size().unstack(fill_value=0)

# Create a percentage version of the data
percentage_data = data.div(data.sum(axis=1), axis=0) * 100

# Plot stacked bar chart
fig, ax = plt.subplots(figsize=(9, 7))
percentage_data.plot(kind='bar', stacked=True, ax=ax)

# Add percentage labels to each section of the stacked bar
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='center')

# Add labels and title
plt.title("Percentage of Customers Churned Based on Senior Citizen Status")
plt.xlabel("Senior Citizen")
plt.ylabel("Percentage")
plt.legend(title="Churn")
plt.show()


#  comparatively a greater % of people in senior ciitzens category have churned

# In[68]:


plt.figure(figsize=(9,7))
                   
sns.histplot(x="tenure",data=df,bins=30,hue='Churn')
plt.show()


# people who have used our services  for a long time have stayed and people who haved  used services 
# 1 or 2 months have churned out

# In[76]:


plt.figure(figsize=(9,7
                   ))
ax=sns.countplot(x='Contract',data=df,hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("count of coustmers churned out  on the basis of contract ")
plt.show()
                


# people who haved month to month  contract are likely  to churn thenf rom those who have 1 or 2 years or contracts

# In[70]:


df.columns.values


# In[73]:


columns = ['PhoneService', 'MultipleLines', 'InternetService', 
           'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
           'TechSupport', 'StreamingTV', 'StreamingMovies']

# Set the number of rows and columns for the subplot grid
n_cols = 3  # Number of columns in the grid
n_rows = len(columns) // n_cols + (len(columns) % n_cols > 0)  # Dynamically set rows based on the number of plots

# Create a figure and axes for the subplots
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 10))
axes = axes.flatten()  # Flatten the axes array for easy iteration

# Plot each count plot
for i, col in enumerate(columns):
    sns.countplot(x=col, data=df, ax=axes[i],hue="Churn")  # Plot countplot on each axis
    axes[i].set_title(f'Count Plot of {col}')  # Set title for each subplot
    axes[i].set_xlabel("")  # Remove x-axis label for cleaner look
    axes[i].set_ylabel("Count")  # Set y-axis label for all plots

# Remove any empty subplots if the number of columns is not divisible by n_cols
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()  # Adjust the layout so that subplots don't overlap
plt.show()


# the majority of coustmers who do not churn tend to hav e sevrices like phoneservoices,internet services (particurally dsl,)
# and online security enables for services like online backup,techsupport,and streaming tv,churnrates are noticeably higher when
# there services are not used or are unavilable .

# In[81]:


plt.figure(figsize=(9,7
                   ))
ax=sns.countplot(x='PaymentMethod',data=df,hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("count of coustmers churned out  on the basis of PaymentMethod ")
plt.xticks(rotation=40)
plt.show()


# coustmer is likely to churned when he is using electronic check as apayment methods
