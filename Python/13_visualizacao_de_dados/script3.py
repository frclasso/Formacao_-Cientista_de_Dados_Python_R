# grafico de diospersao com legendas
import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

base = pd.read_csv('./dados/co2.csv')
print(base.head())
print()

# separa as duas variaveis continuas "conc" e "uptake"
x = base.conc
y = base.uptake

#retorna os valores unicos  do atributo treatment
unicos = list(set(base.Treatment))
print(unicos)
print()

for i in range(len(unicos)):
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice], y[indice], label= unicos[i])
plt.legend(loc='lower right')
plt.show()