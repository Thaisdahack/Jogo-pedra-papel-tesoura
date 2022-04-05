#!/usr/bin/env python
# coding: utf-8

# In[15]:


pwd


# In[1]:


#importando as bibliotecas
import pandas as pd
import numpy as np
import re


# In[2]:


#importando o arquivo
shark = pd.read_csv('attacks.csv')

#verificando a estrutura do dataset
shark.head(5)
shark.shape #25723 linhas, 24 colunas
shark.size


# In[18]:


shark


# Pergunta 1: qual país teve maior numero de ocorrencias? clear case number, country
# 
# variaveis interessantes: atividade, ano, pais, 

# In[19]:


shark.columns #chamando as colunas


# In[15]:


#verificando valores nulos
import seaborn as sns
sns.set({'figure.figsize':(20,20)})
sns.heatmap(shark.isnull(),cbar=False)


# In[3]:


shark.info() #country tem mais de 6200 nulos/ year 6300/ atividade 5758 de um total de 25725


# In[4]:


shark.dtypes


# In[5]:


shark.head(10)


# In[9]:


#ecnontrando valores duplicados
shark[shark.duplicated(keep='first')]


#apagando valores duplicados 

shark.drop_duplicates(subset=None, keep='first', inplace=True)


# In[10]:


shark.shape #sobraram 6312 ocorrencias sem as duplicatas


# In[25]:


shark.head(5)


# In[12]:


#selecionando um subset do dataframe (series)
shark.columns
shark= shark[["Case Number", "Year","Country", "Location",]]
shark


# In[16]:


#verificando valores nulos do novo dataset
import seaborn as sns
sns.set({'figure.figsize':(20,20)})
sns.heatmap(shark.isnull(),cbar=False)


# In[17]:


shark.info()


# In[18]:



shark.dtypes


# In[19]:


shark.head(40)


# In[21]:


# verificando a porcentagem de linhas preechidas no dataset
shark["Country"].isnull().value_counts(normalize=True) #99% dos paises esta preenchido
shark["Location"].isnull().value_counts(normalize=True) #91% esta preenchido
shark["Case Number"].isnull().value_counts(normalize=True) #99%
shark["Year"].isnull().value_counts(normalize=True) #99% preenchido


# In[54]:


#removendo caracteres especiais
shark= shark.replace('\W',' ',regex=True)



# In[26]:


shark.head(60)


# In[33]:


# contar valores unicos paises

shark_clean.Country.unique

shark_top = shark.Country.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True) >10
#Eua onde tem maior frequencia de ataques


# In[22]:


#abrindo arquivo paises
countries = pd.read_csv('countries.csv')
countries.size
countries.head(20)


# In[36]:


#pegar os top 20 paises do data shark_clean > 10
shark_top

