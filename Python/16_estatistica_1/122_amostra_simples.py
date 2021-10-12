import os
import pandas as pd
import numpy as np

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

base = pd.read_csv('./dados/iris.csv')
print(base.head())
print() 
print(base.shape)
print()

# gerando uma amostra aleatória de semente
np.random.seed(2345)

#150 amostras de 0 a 1, com reposição
amostra = np.random.choice(
    a = [0,1],
    size = 150,
    replace=True,
    p = [0.7, 0.3]
    )

# verifica o tamanho da amostra
print(len(amostra))
print()
# verifica o tamanho da amostra, separados por 0 e 1
print(len(amostra[amostra == 1]))
print(len(amostra[amostra == 0]))
print()
print(amostra)
print()

base_final  = base.loc[amostra == 0]
print(base_final.shape)
print()

base_final2  = base.loc[amostra == 1]
print(base_final2.shape)
