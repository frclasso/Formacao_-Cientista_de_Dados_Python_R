#90 Histograma e Densidade com Seaborn
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as srn

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

base = pd.read_csv("./dados/trees.csv")
print(base.head())
print()

#Histograma com 10 divisões (bins)  e com grafico de densidade
#srn.distplot(base.Volume, bins=10, axlabel='Volume').set_title("Arvores")
#plt.show()
#print()

# segunda base de  dados chicken.csv

base2 = pd.read_csv('./dados/chicken.csv')
print(base2.head())
print()

# Criando novo dataframe agrupando o atributo 'feed'
agrupado = base2.groupby(['feed'])['weight'].sum()
print(agrupado)
print()

# separando por feed = horsebean - TESTE
#horsebean_df = base2.loc[base2['feed'] == 'horsebean']
#print(horsebean_df)
#print()

def horsebean():
    #Histograma horsebean
    srn.distplot(base2.loc[base2['feed'] == 'horsebean'].weight, hist=False).set_title("Horsebean")
    #plt.show()

def casein():
    #Histograma casein
    srn.distplot(base2.loc[base2['feed'] == 'casein'].weight).set_title("Casein")
    #plt.show()

def linseed():
    #Histograma linseed
    srn.distplot(base2.loc[base2['feed'] == 'linseed'].weight).set_title("linseed")
    #plt.show()

def meatmeal():
    #Histograma meatmeal
    srn.distplot(base2.loc[base2['feed'] == 'meatmeal'].weight).set_title("meatmeal")
    #plt.show()

def soybean():
    #Histograma soybean
    srn.distplot(base2.loc[base2['feed'] == 'soybean'].weight).set_title("soybean")
    #plt.show()

def sunflower():
    #Histograma sunflower
    srn.distplot(base2.loc[base2['feed'] == 'sunflower'].weight).set_title("sunflower")
    #plt.show()


# impressao de todos graficos
plt.figure()
plt.subplot(3,2,1) # 3 linhas, 2 colunas , posição 1
horsebean()
plt.subplot(3,2,2)
casein()
plt.subplot(3,2,3)
linseed()
plt.subplot(3,2,4)
meatmeal()
plt.subplot(3,2,5)
soybean()
plt.subplot(3,2,6)
sunflower()
# ajuta layout para npa haver sobreposição
plt.show()
plt.tight_layout()