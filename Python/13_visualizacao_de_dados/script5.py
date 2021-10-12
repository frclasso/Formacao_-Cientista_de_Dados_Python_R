# 86.BoxPlot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as srn
import os

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

base = pd.read_csv("./dados/trees.csv")
print(base.head())
print()

# Geração de Boxplot
# showfliers = False , esconde o outlier
#patch_artist = True, preenche o grafico
# plt.boxplot(base.Volume, vert =False, showfliers=False, notch=True, patch_artist=True)
# plt.title("Arvores")
# plt.xlabel("Volume")
# plt.show()

# Dados por linha
plt.boxplot(base)
plt.title("Arvores")
plt.xlabel("Dados")
plt.show()

# Geração de 3 boxplots
# plt.boxplot(base.Volume, vert=False)
# plt.boxplot(base.Girth, vert=False)
# plt.boxplot(base.Height, vert=False)
# plt.title("Arvores")
# plt.xlabel("Dados")
# plt.show()