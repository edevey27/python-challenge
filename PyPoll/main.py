#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv
import pandas as pd

election_csv = os.path.join(".", "Resources", "election_data.csv")


# In[53]:


#create a data frame
election_df = pd.read_csv(election_csv)
election_df.columns




# In[54]:


#identify my data types that I am working with
election_df.dtypes


# In[55]:


#count the total number of votes in the Ballot ID column, we use nunique, to count the total number of unique ballots, since a person cannot vote twice
total_votes_df = election_df["Ballot ID"].nunique()
total_votes_df


# In[56]:


#candidates who received a vote, using unique in Candidate column
candidate_df = election_df["Candidate"].unique()
candidate_df


# In[57]:


#create variable vote counts for each candidate
vote_counts = election_df["Candidate"].value_counts()
vote_counts


# In[58]:


#calculate the total percent of votes each candidate receive using vote count and total votes
vote_percent = (vote_counts / total_votes_df) * 100
vote_percent


# In[59]:


winner = vote_counts[election_df["Candidate"]].idxmax()
winner 


# In[60]:


#print the results of each 'total votes cast, and the candidate, total votes they received, and % of votes won, followed by the winning cnadidate'
print(f"ELECTION RESULTS")
print("----------------------------------------")
print(f"Total Votes Cast: {total_votes_df}")
print("----------------------------------------")
for Candidate in vote_counts.index:
    print(f"{Candidate}: {vote_percent[Candidate]:.2f}% ({vote_counts[Candidate]})")
print("----------------------------------------")
print(f"Winning Candidate: {winner}")
print("----------------------------------------")


# In[ ]:





# In[ ]:




