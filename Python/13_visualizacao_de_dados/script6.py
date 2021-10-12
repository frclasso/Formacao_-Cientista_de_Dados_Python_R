# 87 Divisao da tela
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as srn
import os

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

base = pd.read_csv("./dados/trees.csv")
print(base.head())
print()

# comparando circunferencia com volume
# plt.scatter(base.Girth, base.Volume)
# plt.show()

# comparando circunferencia com altura
# plt.scatter(base.Girth, base.Height)
# plt.show()

# comparando altura com volume
# plt.scatter(base.Height, base.Volume)
# plt.show()

# Gerando histograma do volume
# plt.hist(base.Volume)
# plt.show()

# Unindo graficos em unico dashboard
plt.figure(1) # criando o quadro
plt.subplot(2,2,1) # duas linhas, duas colunas, posição 1
plt.scatter(base.Girth, base.Volume) # primeiro grafico
plt.subplot(2,2,2)
plt.scatter(base.Girth, base.Height)
plt.subplot(2,2,3)
plt.scatter(base.Height, base.Volume)
plt.subplot(2,2,4)
plt.hist(base.Volume)
plt.show()  