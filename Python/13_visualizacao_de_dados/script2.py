# 83 - HISTOGRAMAS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)
#print(os.getcwd())


base = pd.read_csv("./dados/trees.csv")
print(base.shape)
print(base.head())

dados = np.histogram(base.iloc[:,1], bins=6)
print(dados)
print()
#Visualização do histograma com 6 divisões(bins)
plt.hist(base.iloc[:, 1], bins= 6)
plt.title("Àrvores")
plt.ylabel("Frequencia")
plt.xlabel("Altura")
plt.show()



