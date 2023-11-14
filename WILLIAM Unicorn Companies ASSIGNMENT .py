#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[6]:


# import the necessary libraries
import numpy as np
import pandas as pd

# for visuals
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[7]:


# Load unicorn companies data
unicorn_data = pd.read_csv(r'C:\Users\user\Documents\Unicorn_Companies.csv',encoding='latin-1')
unicorn_data


# In[8]:


unicorn_data.info()


# In[9]:


missing_data = unicorn_data.isnull()
unicorn_data


# In[10]:


unicorn_data.isnull()


# In[11]:


# what are rows with NaN values
unicorn_data.isna().sum()


# In[12]:


unicorn_data.mean()


# In[13]:


unicorn_data['City'].value_counts()


# In[14]:


# Remove non-numeric characters and convert to float
unicorn_data['Valuation'] = unicorn_data['Valuation'].str.replace('$', '').str.replace('B', '').astype(float)

# Calculate the mean of the 'Valuation' column
mean_valuation = unicorn_data['Valuation'].mean()

print(mean_valuation)


# In[16]:


# Remove rows with 'Unknown' in the 'Funding' column
unicorn_data = unicorn_data[unicorn_data['Funding'] != 'Unknown']

# Convert the 'Funding' column to strings
unicorn_data['Funding'] = unicorn_data['Funding'].astype(str)

# Remove non-numeric characters and convert to float
unicorn_data['Funding'] = unicorn_data['Funding'].str.replace('[\$,MB]', '', regex=True).astype(float)

# Then convert to integer
unicorn_data['Funding'] = unicorn_data['Funding'].astype(int)





# In[ ]:





# In[ ]:





# In[17]:


unicorn_data.mean()


# In[18]:


unicorn_data['City'].value_counts()


# In[20]:


str(unicorn_data['City'])


# In[21]:


unicorn_data['City'].fillna(method='bfill', inplace=True)




# In[22]:


unicorn_data['Select Investors'].fillna(method='bfill', inplace=True)


# In[23]:


# what are rows with NaN values
unicorn_data.isna().sum()


# In[24]:


unicorn_data.mean()


# In[25]:


# view summary statistics
unicorn_data.describe()
  




# In[26]:


# visualize the missing values
plt.figure(figsize = (10, 6))
plt.title('Visualizing missing values')
sns.heatmap(unicorn_data.isnull(), cbar =True, cmap = 'magma_r')
plt.show()





# In[27]:


# statistical descriptive analysis of the numerical features
unicorn_data.describe()
unicorn_data


# In[ ]:





# In[28]:


# statistical descriptive analysis of the numerical features
unicorn_data.describe().astype('int')


# In[29]:


# Assuming you have a pandas dataframe called 'unicorn_data' with columns 'Company', 'Funding', and 'Valuation'
unicorn_data['Funding'] = pd.to_numeric(unicorn_data['Funding'], errors='coerce')
unicorn_data['Valuation'] = pd.to_numeric(unicorn_data['Valuation'], errors='coerce')
unicorn_data['ROI'] = (unicorn_data['Valuation'] - unicorn_data['Funding']) / unicorn_data['Funding']
unicorn_data_sorted = unicorn_data.sort_values('ROI', ascending=False)
top_10_unicorn = unicorn_data_sorted.head(10)['Company']
print(top_10_unicorn)


# In[ ]:





# In[31]:


import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a pandas dataframe called 'unicorn_data' with columns 'Company', 'Funding', and 'Valuation'
unicorn_data['Funding'] = pd.to_numeric(unicorn_data['Funding'], errors='coerce')
unicorn_data['Valuation'] = pd.to_numeric(unicorn_data['Valuation'], errors='coerce')
unicorn_data['ROI'] = (unicorn_data['Valuation'] - unicorn_data['Funding']) / unicorn_data['Funding']
unicorn_data_sorted = unicorn_data.sort_values('ROI', ascending=False)
top_10_unicorn = unicorn_data_sorted.head(10)

# Create a bar plot of 'ROI' for the top 10 companies
plt.figure(figsize=(12, 6))  # Set the figure size
sns.barplot(x='Company', y='ROI', data=top_10_unicorn, palette='viridis')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Add labels and a title
plt.xlabel('Company')
plt.ylabel('ROI')
plt.title('Bar Plot of ROI for Top 10 Companies')

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines
plt.tight_layout()  # Ensure labels are not cut off
plt.show()













# ## Observation: The chat shows that Otto Bock HealthCare made more money ,when compairing the company ROI using the bar chat above.

# In[32]:


import squarify

# Convert the 'Year Founded' column to numeric (assuming 'Year Founded' contains numeric values)
unicorn_data['Year Founded'] = pd.to_numeric(unicorn_data['Year Founded'], errors='coerce')

# Remove rows with NaN or non-numeric values in the 'Year Founded' column
unicorn_data = unicorn_data.dropna(subset=['Year Founded'])

# Sort the DataFrame by 'Year Founded' column in descending order and take the top 7 rows
top_7_unicorn_data = unicorn_data.sort_values(by='Year Founded', ascending=False).head(7)

# Define the treemap layout
fig, ax = plt.subplots(figsize=(8, 8))

# Plot a treemap using the 'Year Founded' values from the filtered top 7
squarify.plot(sizes=top_7_unicorn_data['Year Founded'], label=top_7_unicorn_data.index, alpha=0.8)

# Add labels and title to the plot
plt.axis('off')  # Turn off axis labels
plt.title('Top 7 Unicorn Companies by Year Founded')

# Show the plot
plt.show()






# ## Observation : According to Treemap chat,it indicate  the top 7 companys,they almost made the same level of income yearly.

# In[33]:


import matplotlib.pyplot as plt

# Sample data
unicorn_data = pd.DataFrame({
    'Funding': ['', '', ''],
    'Value': [166, 300, 491]
})

# Colors for the donut chart
colors = ['#FFC300', '#FF5733', '#C70039']

# Create the donut chart
plt.pie(unicorn_data['Value'], labels=unicorn_data['Funding'], colors=colors, autopct='%1.1f%%', startangle=90)

# Draw a white circle at the center to create the donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add a title to the chart
plt.title('Percentage of Funding Statistics')

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Show the donut chart
plt.show()







# ## Observation: it shows the percentage of the fund in the company,according to the data,it shows the company made more income when you check the statistics of the funding income.

# In[34]:


# visualize using bar chart
ax = unicorn_data.plot(kind = 'bar', figsize = (10, 6), title = 'unicorn_data',
                       xlabel = 'Year Founded ', ylabel = 'Funding',legend = False)

# annotate
ax.bar_label(ax.containers[0], label_type = 'edge')

# pad the spacing between the number and edge of the figure
ax.margins(y = 0.1)

# rotate the x-labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# show the visual
plt.show()



# 
# ## Observation: This data means ,the yearly income of this company in y-axis 2 ,the company have more profit more than other years on this data.
# 

# ## Observation
#       Give an overall recommendation to the stakeholders on how they can improve their business
#       and generate more revenue.
# --When you check the company ROI you will understand this company Otto BockHealthcare and  Shein ,they made more money that year due to the amount of income they use to manufacture more materials and it likely they have more  workers which help them to work and also take overtime to work,which can generate more income to the company. 
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




