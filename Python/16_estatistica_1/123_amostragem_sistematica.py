import os
import numpy as np
import pandas as pd
from math import ceil

# criacao das variaveis para representar a população
populacao = 150
amostra =15
k = ceil(populacao/amostra)
print(k)
print()

# Definição do valor randomico para inicializer a amostra, iniciando de 1 até k + 1
r = np.random.randint(low = 1, high= k+1, size =1)
print(r)

# Criamos um loop ára somar os proximos valores, baseado no primeiro valor r que 
# foi definido anteriormente

acumulador = r[0]
sorteados= []
for i in range(amostra):
    sorteados.append(acumulador)
    acumulador += k
print(sorteados)
print(len(sorteados))
print()

# Carregamos a base de dados e criamos a base_final somente com os valores sorteados
file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

base = pd.read_csv('./dados/iris.csv')
base_final = base.loc[sorteados]
print(base_final)