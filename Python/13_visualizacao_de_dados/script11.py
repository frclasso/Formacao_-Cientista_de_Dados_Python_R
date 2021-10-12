# 93 GRaficos 3D
import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import seaborn as srn

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

base = pd.read_csv('./dados/orchard.csv')
print(base.head())
print()

# Criação do gráfico 3D, indicando o atributo projection = '3D', 
# passando tres atributos (decrease, rowpass e colpos)
figure = plt.figure()
eixo = figure.add_subplot(1,1,1, projection = '3d')
eixo.scatter(base.decrease, base.rowpos, base.colpos)
eixo.set_xlabel('decrease')
eixo.set_ylabel('rowpos')
eixo.set_zlabel('colpos')
plt.show()