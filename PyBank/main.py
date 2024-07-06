#!/usr/bin/env python
# coding: utf-8

# In[28]:


import os
import csv
import pandas as pd

budget_csv = os.path.join(".", "Resources", "budget_data.csv")



# In[29]:


#create a data frame
budget_data_df = pd.read_csv(budget_csv)

#identify my data types that I am working with
budget_data_df.dtypes



# In[30]:


#I made the dateset into string data so it can handle different date formatting.
budget_data_df['Date'] = budget_data_df['Date'].astype(str)
budget_data_df


# In[34]:


#I then calculate the total number of months by creating a formula, listing the unique number of months, so I don't count the same month twice
total_months = budget_data_df['Date'].nunique()
total_months


# In[33]:


#next I added all the data in the Profit/Losses category to give me my net profit
net_profit = budget_data_df['Profit/Losses'].sum()
net_profit


# In[37]:


#I created a column change that would be based off the difference between each cell in the column profit/loss
budget_data_df['Change'] = budget_data_df['Profit/Losses'].diff()
##to get average change I use that change column and calculate the average of that column
average_change = budget_data_df['Change'].mean()
average_change


# In[38]:


greatest_increase = budget_data_df.loc[budget_data_df['Change'].idxmax()]
greatest_increase


# In[39]:


greatest_decrease = budget_data_df.loc[budget_data_df['Change'].idxmin()]
greatest_decrease


# In[75]:


#print everything out

print(f'Total Months: {total_months}')
print(f'Net Profit: ${net_profit}')
print(f'Average Change in Profit: ${average_change:.2f}')
print(f'Greatest Increase in Profit: {greatest_increase["Date"]} (${greatest_increase["Change"]:.2f})')
print(f'Greatest Decrease in Profit: {greatest_decrease["Date"]} (${greatest_decrease["Change"]:.2f})')


# In[ ]:




