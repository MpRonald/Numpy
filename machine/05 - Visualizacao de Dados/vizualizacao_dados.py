# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:47:18 2020

@author: USER

Aula 5 machine learning
"""
import pandas as pd
import numpy as np

data = pd.read_csv("train.csv")

data.columns

data.columns = ['IdPassageiro', 'Sobreviveu', 'Classe', 'Nome', 'Sexo',
                'Idade', 'IrmaosConjuge','PaisFilhos', 'Bilhete', 'Tarifa',
                'Cabine', 'Embarque']

data['Sexo'].replace({'male': 'homem', 'female': 'mulher'}, inplace=True)

data['Cabine'] = data['Cabine'].apply(lambda x: x[0] if pd.notna(x) 
                                      else np.nan)

data['Cabine']

import matplotlib.pyplot as plt
%matplotlib inline 

plt.hist(data['Idade'].dropna(), bins=20) 
plt.title('Distribuição das idades')
plt.ylabel('Pessoas')
plt.xlabel('Idade')
plt.show()

data['Classe'].unique()

plt.hist(data['Classe']) 
plt.title('Distribuição das classes')
plt.ylabel('Pessoas')
plt.xlabel('Classes')
plt.show()

plt.subplot(1,2,1)
plt.hist(data['Idade'].dropna())
plt.title('Distribuição de Idades')

plt.subplot(1,2,2)
plt.hist(data['Classe'])
plt.title('Distribuição de Classes')

plt.tight_layout()
plt.show()

# SubPLots 
f, ax = plt.subplots(1, 2), figsize=(10, 5) # f = figura / ax = eixo
len(ax)  # ax é uma lista com dois elementos;
ax[0].hist(data['Idade'].dropna())
ax[0].set_title('Distribuição das Idades')
ax[1].hist(data['Classe'].dropna())
ax[1].set_title('Distribuição das Classes')

plt.tight_layout()
show()












