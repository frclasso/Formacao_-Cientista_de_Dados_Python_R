from script1_importando_dataset import create_dataset
import seaborn as sns

# ANALISE EXPLORATORIA
dataset = create_dataset()
#print(data.head())

# Estado
agrupado_estados = dataset.groupby(['Estado']).size()
print(agrupado_estados)

#agrupado_estados.plot.bar(color="gray")

#sns.barplot(x = agrupado_estados.index, y= agrupado_estados ,color="gray")
#sns.barplot(x= agrupado_estados.index, y = agrupado_estados)
print("=" * 40)

# Genero
agrupado_genero = dataset.groupby(['Genero']).size()
print(agrupado_genero)
print("=" * 40)
# VALORES NUMERICOS
#Score
score = dataset['Score'].describe()
print(score)
#sns.boxplot(dataset['Score']).set_title('Score')
#sns.displot(dataset['Score'])

print('Idade',"=" * 40)
# IDADE

idade = dataset['Idade'].describe()
print(idade)
#sns.boxplot(dataset['Idade']).set_title('Idade')
#sns.displot(dataset['Idade']).set_title('Idade')

print('Saldo',"=" * 40)
# SALDO
saldo = dataset['Saldo'].describe()
print(saldo)

#sns.boxplot(dataset['Saldo']).set_title('Saldo')
#sns.displot(dataset['Saldo']).set_title('Saldo')

print('Salario',"=" * 40)
# SALARIO
salario = dataset['Salario'].describe()
print(salario)

#sns.boxplot(dataset['Salario']).set_title('Salario')
#sns.displot(dataset['Salario']).set_title('Salario')

print('Valores NAN',"=" * 40)
# VERIFICANDO VALORES NULOS
nulos = dataset.isnull().sum()
print(nulos)
