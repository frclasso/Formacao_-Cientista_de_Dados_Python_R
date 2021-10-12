# 91 Grafico de dispersão com Seaborn
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as srn

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

base = pd.read_csv('./dados/co2.csv')
print(base.head())
print()
# Grafico de dispersão utilizando os atributos conc e uptake, agrupamento pelo type (origem)
#srn.scatterplot(base.conc, base.uptake, hue = base.Type)
#plt.show()

# Seleção de registros especificos
q = base.loc[base['Type'] == 'Quebec']
m = base.loc[base['Type'] == 'Mississippi']

# separa em dois graficos pelo atributo Type(origem)
# plt.figure()
# plt.subplot(1,2,1)
# srn.scatterplot(q.conc, q.uptake).set_title('Quebec')
# plt.subplot(1,2,2)
# srn.scatterplot(m.conc, m.uptake).set_title('Mississippi')
# plt.show()
# plt.tight_layout()


# separar por refrigerado e  nao refrigerado
# ch = base.loc[base['Treatment'] == 'chilled']
# nc = base.loc[base['Treatment'] == 'nonchilled']

# plt.figure()
# plt.subplot(1,2,1)
# srn.scatterplot(ch.conc, ch.uptake).set_title('Chilled')
# plt.subplot(1,2,2)
# srn.scatterplot(nc.conc, nc.uptake).set_title('Non Chilled')
# plt.show()
# plt.tight_layout()


# CArregamento de outra base, cancer de esofago
base2 = pd.read_csv('./dados/esoph.csv')
#print(base2.head())

#Grafico entre os atributos 'alcgp' e 'ncontrols'
# srn.catplot(x = 'alcgp', y='ncontrols', data=base2, jitter=False)
# plt.show()


#Grafico entre os atributos 'alcgp' e 'ncontrols', com agrupamento
srn.catplot(x = 'alcgp', y='ncontrols', data=base2, col='tobgp')
plt.show()
