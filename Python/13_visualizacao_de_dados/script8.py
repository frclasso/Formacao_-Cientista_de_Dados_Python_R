#89 Boxplot com Seaboarn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as srn
import os

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

base = pd.read_csv("./dados/trees.csv")
print(base.head())
print()

#boxplot
srn.boxplot(base.Volume).set_title("Arvores")
#plt.show()

#Boxplot de toda a base
sns.boxplot(data=base)
plt.show()