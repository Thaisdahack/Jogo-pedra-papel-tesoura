#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[ ]:


#importing libraries
import pandas as pd
import numpy as np
import re


# In[ ]:


#importing files
shark = pd.read_csv('attacks.csv')

#checking dataset structure
shark.head(5)
shark.shape #25723 linhas, 24 colunas
shark.size


# In[ ]:



shark.columns #checking columns names


# 
# Questions to be answered:
# 
# Question 1: Which hemisphere has more ocurrences?
# Question 2: Which hemisphere has more fatalities?
# Question 3: Which activity has more fatalities?
# Question 3: How Many ocurrences happens in Western Boundary Current areas?

# In[ ]:





# In[5]:


#checking null values on dataframe
import seaborn as sns
sns.set({'figure.figsize':(20,20)})
sns.heatmap(shark.isnull(),cbar=False)


# In[6]:


shark.info() #country has more than 6200 nulls/ year 6300/ activity 5758 out of a total of 25725


# In[7]:


shark.dtypes


# In[8]:


shark.head(10)


# In[37]:



#finding duplicate values
shark[shark.duplicated(keep='first')]


#deleting duplicate values

shark.drop_duplicates(subset=None, keep='first', inplace=True)


# In[38]:


shark.shape #sobraram 6312 ocorrencias sem as duplicatas


# In[39]:


shark.head(5)


# In[40]:


#selecting  subsets of the dataframe (series)
shark.columns
new_shark = shark[["Country", "Fatal (Y/N)", "Activity", "Area"]]

new_shark


# In[13]:


#checking null values of new dataset/ with columns: 'Country', 'Area', 'Activity', 'Fatal'
import seaborn as sns
sns.set({'figure.figsize':(20,20)})
sns.heatmap(new_shark.isnull(),cbar=False)


# In[14]:


new_shark.info()


# In[15]:



new_shark.dtypes


# In[16]:


new_shark.head(10)


# In[17]:


# checking the percentage of rows filled in the dataset
new_shark["Country"].isnull().value_counts(normalize=True) #99% dos paises esta preenchido
new_shark["Fatal (Y/N)"].isnull().value_counts(normalize=True) #91% esta preenchido
new_shark["Area"].isnull().value_counts(normalize=True) #92% preenchido
new_shark["Activity"].isnull().value_counts(normalize=True)#91% preenchido


# In[41]:


#removing special characters
new_shark.replace('\W',' ',regex=True)

#removing the decimal places from the year column
#pd.options.display.float_format = '{:.0f}'.format


new_shark.head(30)


# In[ ]:





# In[42]:


# count unique country values

new_shark.Country.unique


shark_top = new_shark.Country.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
shark_top
#USA where has the highest frequency of attacks
shark_mask= shark_top>100 #mask to get unique values from countries greater than 100 occurrences
shark_top.loc[shark_mask].index
list_top= shark_top.loc[shark_mask].index






# In[43]:


mask_top = new_shark['Country'].isin(list_top) # mask to check if list_top is inside the country column
new_shark =new_shark[mask_top] #applying the mask on the dataframe


# In[44]:


shark_top.loc[shark_mask].index #countries with more than 100 occurrences


# In[46]:


#ADDING ANOTHER COLUMN WITH THE HEMISPHERES N and S
new_shark.loc[(new_shark['Country'] == 'USA') | (new_shark['Country'] == 'BAHAMAS'), 'Hemisphere'] = 'North'
new_shark
new_shark.loc[(new_shark['Country'] == 'AUSTRALIA') | (new_shark['Country'] == 'SOUTH AFRICA') |  (new_shark['Country'] == 'NEW ZELAND') |  (new_shark['Country'] == 'BRAZIL') | (new_shark['Country'] == 'PAPUA NEW GUINEA'), 'Hemisphere'] = 'South'
new_shark


# In[47]:


#counting unique values from each hemisphere
count_hem = new_shark.Hemisphere.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True) #North    2338 / South    2163
count_hem


# The norht hemisphere has more ocurrences than south (north = 2338 / south = 2163)

# In[48]:


#counting unique values of each activity #surfing has more occurrences
new_shark.Activity.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)


# In[49]:


#renaming column "Fatal (Y/N) to Fatal"
new_shark.columns
new_shark.rename(columns={'Fatal (Y/N)': 'Fatal'}, inplace=True)
                       
new_shark


# In[50]:


#how many fatal incidents occurred? 
#3488 non-fatal and 703 fatal

#new_shark['Fatal'] = new_shark.loc[:,'Fatal'].str.strip()
import re
new_shark['Fatal'] = new_shark['Fatal'].str.replace('\s?N\s?','N') #usando regex (\s? pode ter espaço ou nao N(padrao) \s? pode ter espaço depois ou nao)
new_shark


new_shark.Fatal.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)


# In[ ]:





# In[ ]:





# In[51]:


# checking which hemisphere has the most fatal attacks

new_shark.groupby(by=['Hemisphere', 'Fatal']).count()[['Country']] # agrupou o hemisferio e o fatal como indices e contou pelo numero de paises que seria as ocorrencias/ colocar 2 parenteses para ficar com cara de parenteses 



# The south hemisphere has more fatal ocurrences then north hemisphere

# In[131]:


#Fazer uma funçao aqui
fatal_total=703
fatal_south= 483
(fatal_south*100)/fatal_total
#68¨% dos ataques sao no HS


# In[ ]:





# In[132]:


#checking the activity with the most fatalities
new_shark.Activity.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
#The most fatal activity is swimming
new_shark.groupby(by=["Activity", "Fatal"]).count()[['Country']].sort_values("Country",ascending=False)


# In[134]:


#checking which activity was most practiced during the occurrences
new_shark.Activity.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)


# In[133]:


fatal_total=703
fatal_swimming= 172
(fatal_swimming*100)/fatal_total #24% were fatal in swimming


# In[137]:


not_fatal=3488
(not_fatal*100)/total_ocurrences
#75% of incidents are non-fatal


# In[54]:


#Distinguishing western boundary currents

new_shark.head(10)

new_shark.Area.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True) #Florida é o estado com mais ocorrencias


# In[91]:


#putting the eastern states of the US that are on the route of the western boundary currents
new_shark.loc[new_shark['Area'].isin (['Connecticut','Delaware','Florida','Georgia','Maryland','New Hampshire','North Carolina','Pennsylvania','Rhode Island','South Carolina']), "Current"]="Warm Current"
new_shark


# In[32]:


#I used to put quotes around all the words
"Connecticut, Delaware, Florida, Georgia, Maryland, New Hampshire, North Carolina, Pennsylvania, Rhode Island, South Carolina".split(", ")


# In[56]:


#placing the Australian east coast states that are in the route of the western boundary current
new_shark.loc[new_shark['Area'].isin (['Victoria', 'New South Wales', 'Queensland']), "Current"]="Warm Current"

new_shark       


# In[34]:


# Countrys in dataframe: Index(['USA', 'AUSTRALIA', 'SOUTH AFRICA', 'PAPUA NEW GUINEA', 'NEW ZEALAND', 'BRAZIL', 'BAHAMAS']


# In[57]:


#setting the dataframe index for the "Country" column to be the new index and it will be possible to make the groupings
new_shark.set_index(['Country'], inplace = True)
new_shark


# In[58]:


new_shark.loc['SOUTH AFRICA']


# In[92]:


#placing the South Africa east coast states that are in the route of the western boundary current
new_shark.loc[new_shark['Area'].isin (['Eastern Cape Province', 'Western Cape Province', 'KwaZulu-Nata']), "Current"]="Warm Current"

new_shark  


# In[101]:


##placing the New Zealand east coast states that are in the route of the western boundary current
new_shark.loc[new_shark['Area'].isin (['North Island']), 'Current']="Warm Current"


# In[102]:


#splacing the Brazilian east coast states that are in the route of the western boundary current

new_shark.loc['BRAZIL', 'Current'] ="Warm Current"
new_shark.head(60)


# In[94]:


#placing the Bahamas  coast that are in the route of the western boundary current
new_shark.loc['BAHAMAS', 'Current'] ="Warm Current"


# In[73]:


new_shark.head(50)


# In[ ]:


#the countries ->Index(['USA', 'AUSTRALIA', 'SOUTH AFRICA', 'PAPUA NEW GUINEA', 'NEW ZEALAND','BRAZIL', 'BAHAMAS'])


# In[ ]:





# In[80]:


#droping current column
new_shark = new_shark.drop(columns=["current"]) 


# In[103]:


new_shark.head(60)


# In[122]:


#Counting values whith Warm Currents -> 2871 areas are in the western boundary current
total_warm_current = new_shark.Current.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)


# In[123]:


#Grouping warm currents by hemisphere counting by countries

new_shark.groupby(by=['Current', 'Hemisphere']).count()[['Country']]


# In[135]:


#chcking the total of ocurrences
total_ocurrences= len(new_shark)
total_ocurrences


# In[126]:


#62% of occurrences in locations with a western boundary current
(total_warm_current*100)/total_ocurrences


# In[128]:


#fazendo uma funçao para calcular as porcentagens
#def Percentage(total_var, total_ocurrence):
#    """Function to calculate the % of ocurrences on total of ocurrences
#    args: total_var is the value count of some variable in dataframe
#        total_ocurrences is the total lenght of datframe
#        Ex:(total_warm_current*100)/total_ocurrences """
#    (total_var*100)/total_ocurrence
#    
#    return (Percentage)


# In[130]:


#Percentage(total_warm_current, total_ocurrence)

