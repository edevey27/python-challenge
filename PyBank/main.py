#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import csv
import pandas as pd

budget_csv = os.path.join(".", "Resources", "budget_data.csv")



# In[8]:


#create a data frame, identify headers
budget_data_df = pd.read_csv(budget_csv)
header = budget_data_df.columns
header




# In[9]:


#identify my data types that I am working with
budget_data_df.dtypes


# In[10]:


#I made the dateset into string data so it can handle different date formatting.
budget_data_df['Date'] = budget_data_df['Date'].astype(str)
budget_data_df


# In[11]:


#I then calculate the total number of months by creating a formula, listing the unique number of months, so I don't count the same month twice
total_months = budget_data_df['Date'].nunique()
total_months


# In[12]:


#next I added all the data in the Profit/Losses category to give me my net profit
net_profit = budget_data_df['Profit/Losses'].sum()
net_profit


# In[13]:


#I created a column change that would be based off the difference between each cell in the column profit/loss
budget_data_df['Change'] = budget_data_df['Profit/Losses'].diff()
##to get average change I use that change column and calculate the average of that column
average_change = budget_data_df['Change'].mean()
average_change


# In[14]:


greatest_increase = budget_data_df.loc[budget_data_df['Change'].idxmax()]
greatest_increase


# In[15]:


greatest_decrease = budget_data_df.loc[budget_data_df['Change'].idxmin()]
greatest_decrease


# In[16]:


#print everything out

print(f'Total Months: {total_months}')
print("----------------------------------------")
print(f'Net Profit: ${net_profit}')
print("----------------------------------------")
print(f'Average Change in Profit: ${average_change:.2f}')
print("----------------------------------------")
print(f'Greatest Increase in Profit: {greatest_increase["Date"]} (${greatest_increase["Change"]:.2f})')
print("----------------------------------------")
print(f'Greatest Decrease in Profit: {greatest_decrease["Date"]} (${greatest_decrease["Change"]:.2f})')
print("----------------------------------------")


# In[ ]:




