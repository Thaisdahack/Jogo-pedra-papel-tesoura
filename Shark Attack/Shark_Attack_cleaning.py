#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[ ]:


#importando as bibliotecas
import pandas as pd
import numpy as np
import re


# In[ ]:


#importando o arquivo
shark = pd.read_csv('attacks.csv')

#verificando a estrutura do dataset
shark.head(5)
shark.shape #25723 linhas, 24 colunas
shark.size


# In[ ]:



shark.columns #chamando as colunas


# Question 1: Which hemisphere has more ocurrences?
# Question 2: Which hemisphere has more fatalities?
# Question 3: Which activity has more fatalities?
# Question 3: How Many ocurrences happens in Western Boundary Current areas?

# In[ ]:





# In[5]:


#verificando valores nulos
import seaborn as sns
sns.set({'figure.figsize':(20,20)})
sns.heatmap(shark.isnull(),cbar=False)


# In[6]:


shark.info() #country tem mais de 6200 nulos/ year 6300/ atividade 5758 de um total de 25725


# In[7]:


shark.dtypes


# In[8]:


shark.head(10)


# In[37]:


#ecnontrando valores duplicados
shark[shark.duplicated(keep='first')]


#apagando valores duplicados 

shark.drop_duplicates(subset=None, keep='first', inplace=True)


# In[38]:


shark.shape #sobraram 6312 ocorrencias sem as duplicatas


# In[39]:


shark.head(5)


# In[40]:


#selecionando um subset do dataframe (series)
shark.columns
new_shark = shark[["Country", "Fatal (Y/N)", "Activity", "Area"]]

new_shark


# In[13]:


#verificando valores nulos do novo dataset/ tirei o ano
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


# verificando a porcentagem de linhas preechidas no dataset
new_shark["Country"].isnull().value_counts(normalize=True) #99% dos paises esta preenchido
new_shark["Fatal (Y/N)"].isnull().value_counts(normalize=True) #91% esta preenchido
new_shark["Area"].isnull().value_counts(normalize=True) #92% preenchido
new_shark["Activity"].isnull().value_counts(normalize=True)#91% preenchido


# In[41]:


#removendo caracteres especiais
new_shark.replace('\W',' ',regex=True)

#retirando as casas decimais da coluna ano
#pd.options.display.float_format = '{:.0f}'.format


new_shark.head(30)


# In[ ]:





# In[42]:


# contar valores unicos paises

new_shark.Country.unique


shark_top = new_shark.Country.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
shark_top
#Eua onde tem maior frequencia de ataques
shark_mask= shark_top>100 #mascara para pegar valores unicos de paises maior que 100 ocorrencias
shark_top.loc[shark_mask].index
list_top= shark_top.loc[shark_mask].index






# In[43]:


mask_top = new_shark['Country'].isin(list_top) #isso é uma mascara para verificar se list_top esta dentro da coluna country

new_shark =new_shark[mask_top] #aplicando a mascara no dataframe


# In[44]:


shark_top.loc[shark_mask].index #paises com mais de 100 ocorrencias


# In[46]:


#ADICIONANDO OUTRA COLUNA COM OS HEMISFERIOS
new_shark.loc[(new_shark['Country'] == 'USA') | (new_shark['Country'] == 'BAHAMAS'), 'Hemisphere'] = 'North'
new_shark
new_shark.loc[(new_shark['Country'] == 'AUSTRALIA') | (new_shark['Country'] == 'SOUTH AFRICA') |  (new_shark['Country'] == 'NEW ZELAND') |  (new_shark['Country'] == 'BRAZIL') | (new_shark['Country'] == 'PAPUA NEW GUINEA'), 'Hemisphere'] = 'South'
new_shark


# In[47]:


#contando valores unicos de cada hemisferio
count_hem = new_shark.Hemisphere.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True) #North    2338 / South    2163
count_hem


# The norht hemisphere has more ocurrences than south (north = 2338 / south = 2163)

# In[48]:


#contando valores unicos de cada atividade #surfing tem mais ocorrencias
new_shark.Activity.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)


# In[49]:


#renomeando a coluna "Fatal (Y/N) para Fatal"
new_shark.columns
new_shark.rename(columns={'Fatal (Y/N)': 'Fatal'}, inplace=True)
                       
new_shark


# In[50]:


#quantos incidentes fatais ocorreram? 3488 nao fatais e 703  fatais

#new_shark['Fatal'] = new_shark.loc[:,'Fatal'].str.strip()
import re
new_shark['Fatal'] = new_shark['Fatal'].str.replace('\s?N\s?','N') #usando regex (\s? pode ter espaço ou nao N(padrao) \s? pode ter espaço depois ou nao)
new_shark

#quantos incidentes fatais ocorreram? 3488 nao fatais e 703  fatais
new_shark.Fatal.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)


# In[ ]:





# In[ ]:





# In[51]:


# verificando qual hemisferio tem mais ataques fatais

new_shark.groupby(by=['Hemisphere', 'Fatal']).count()[['Country']] # agrupou o hemisferio e o fatal como indices e contou pelo numero de paises que seria as ocorrencias/ colocar 2 parenteses para ficar com cara de parenteses 



# The south hemisphere has more fatal ocurrences then north hemisphere

# In[131]:


fatal_total=703
fatal_south= 483
(fatal_south*100)/fatal_total
#68¨% dos ataques sao no HS


# In[ ]:





# In[132]:



new_shark.Activity.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
#A atividade com mais fatalidade é a nataçao
new_shark.groupby(by=["Activity", "Fatal"]).count()[['Country']].sort_values("Country",ascending=False)


# In[134]:


new_shark.Activity.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)


# In[133]:


fatal_total=703
fatal_swimming= 172
(fatal_swimming*100)/fatal_total #24% foi fatal na natacao


# In[137]:


nao_fatal=3488
(nao_fatal*100)/total_ocurrences
#75% das ocorrencias sao nao fatais


# In[54]:


# Distinguindo correntes de contorno Oeste

new_shark.head(10)

new_shark.Area.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True) #Florida é o estado com mais ocorrencias


# In[91]:


#colocando os estados dos EUA no corrente de contorno oeste(estados do leste do EUA)
new_shark.loc[new_shark['Area'].isin (['Connecticut','Delaware','Florida','Georgia','Maryland','New Hampshire','North Carolina','Pennsylvania','Rhode Island','South Carolina']), "Current"]="Warm Current"
new_shark


# In[32]:


#usei para colocar aspas em todas as palavras
"Connecticut, Delaware, Florida, Georgia, Maryland, New Hampshire, North Carolina, Pennsylvania, Rhode Island, South Carolina".split(", ")


# In[56]:


#colocando os estados da australia no corrente de contorno oeste(estados do leste da Australia)
new_shark.loc[new_shark['Area'].isin (['Victoria', 'New South Wales', 'Queensland']), "Current"]="Warm Current"

new_shark       


# In[34]:


# Paises que estao na tabela: Index(['USA', 'AUSTRALIA', 'SOUTH AFRICA', 'PAPUA NEW GUINEA', 'NEW ZEALAND', 'BRAZIL', 'BAHAMAS']


# In[57]:


#setando o indice para o Country ser o novo indice
new_shark.set_index(['Country'], inplace = True)
new_shark


# In[58]:


new_shark.loc['SOUTH AFRICA']


# In[92]:


#mudando as correntes para Africa do Sul
new_shark.loc[new_shark['Area'].isin (['Eastern Cape Province', 'Western Cape Province', 'KwaZulu-Nata']), "Current"]="Warm Current"

new_shark  


# In[101]:


##mudando as correntes para New Zealand
new_shark.loc[new_shark['Area'].isin (['North Island']), 'Current']="Warm Current"


# In[102]:


#substituindo valores de brazil na coluna Current para warm current

new_shark.loc['BRAZIL', 'Current'] ="Warm Current"
new_shark.head(60)


# In[94]:


new_shark.loc['BAHAMAS', 'Current'] ="Warm Current"


# In[73]:


new_shark.head(50)


# In[ ]:


#esses sao os paises ->Index(['USA', 'AUSTRALIA', 'SOUTH AFRICA', 'PAPUA NEW GUINEA', 'NEW ZEALAND','BRAZIL', 'BAHAMAS'])


# In[ ]:





# In[80]:


#dropar a coluna current
new_shark = new_shark.drop(columns=["current"]) 


# In[103]:


new_shark.head(60)


# In[122]:


#Contand valores para Warm Current -> 2871 locais estao em areas de contorno oeste
total_warm_current = new_shark.Current.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)


# In[123]:


#Agrupando correntes quentes por paises
#new_shark.groupby(by=['Current']).count()[['Country']]
new_shark.groupby(by=['Current', 'Hemisphere']).count()[['Country']]


# In[135]:


total_ocurrences= len(new_shark)
total_ocurrences


# In[126]:


#62% das ocorrencias ocorreram em locais com corrente de contorno oeste
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

