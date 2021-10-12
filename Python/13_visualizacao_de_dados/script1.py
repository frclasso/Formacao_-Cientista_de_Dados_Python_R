# GRAFICO DE DENSIDADE
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)
#print(os.getcwd())


base = pd.read_csv("./dados/trees.csv")
print(base.head())

#Histograma com 6 divisões (bins)
#plt.hist(base.iloc[:,1], bins= 6)
#plt.show()

# GERANDO O MESMO HISTOGRAMA COM A BIBLIOTECA SEABORN
# sns.distplot(
#     base.iloc[:,1], 
#     hist=True, 
#     kde=False, 
#     bins = 6, 
#     color='blue', 
#     hist_kws={'edgecolor': 'black'}
#     )
# plt.show()

# GRAFICO DE LINHA DE DENSIDADE
# sns.distplot(
#     base.iloc[:,1], 
#     hist=False, 
#     kde=True, 
#     bins = 6, 
#     color='blue', 
#     hist_kws={'edgecolor': 'black'}
#     )
# plt.show()

# HISTOGRAMA + GRAFICO DE DENSIDADE
sns.distplot(
    base.iloc[:,1], 
    hist=True, 
    kde=True, 
    bins = 6, 
    color='blue', 
    hist_kws={'edgecolor': 'black'}
    )
plt.show()