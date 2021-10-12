import pandas as pd
import matplotlib.pyplot as plt
import seaborn as srn
import os

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

base = pd.read_csv("./dados/insect.csv")
print(base.shape)
print()
print(base.head())

#Agrupando dados baseados no atributo "spray", somando
agrupado = base.groupby(['spray'])['count'].sum()
print(agrupado)
print()

# Grafico de barras
# versoa 1
# agrupado.plot.bar(color='gray')
# plt.show()

#versao 2
# agrupado.plot.bar(color = ['blue', 'yellow','red', 'green','pink','orange'])
# plt.show()


# grafico de setor(pizza)
agrupado.plot.pie(legend=True)
plt.show()