# 85 Graficos de dispersão
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as srn
import os

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

base = pd.read_csv("./dados/trees.csv")
print(base.head())

# grafico de dispersão considerando volume e a dispersão
# plt.scatter(base.Girth, base.Volume, color='blue', facecolors=None)
# plt.title("Arvores")
# plt.xlabel("Volume")
# plt.ylabel("Circunferencia")
# plt.show()

# versão 2
#plt.scatter(base.Girth, base.Volume)
# plt.plot(base.Girth, base.Volume)
# plt.title("Arvores")
# plt.xlabel("Volume")
# plt.ylabel("Circunferencia")
# plt.show()

# grafico de dispersão com seaborn
srn.regplot(base.Girth, base.Volume, data = base, x_jitter=0.3, fit_reg=False)
plt.show()