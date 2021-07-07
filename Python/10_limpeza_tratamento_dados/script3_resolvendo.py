from script1_importando_dataset import create_dataset
import seaborn as sns
import statistics as sts

dataset = create_dataset()

# Estado ##############################################################
agrupado_estados = dataset.groupby(['Estado']).size()
print(agrupado_estados)
#agrupado_estados.plot.bar(color="gray")
#sns.barplot(x = agrupado_estados.index, y= agrupado_estados ,color="gray")
#sns.barplot(x= agrupado_estados.index, y = agrupado_estados)

# atribuimos a moda(valor mais comum) a RS
dataset.loc[dataset['Estado'].isin(['RP','SP','TD']), 'Estado'] = 'RS'
agrupado_estados_2 = dataset.groupby(['Estado']).size()
print(agrupado_estados_2)

# Genero ##############################################################
print("Genereo","=" * 40)
agrupado_genero = dataset.groupby(['Genero']).size()
print(agrupado_genero)
#verificando valores nulos
print(f"Valores nulos para genero: {dataset['Genero'].isnull().sum()}")
# PREENCHER OS NAN COM MASCULINO (CRITERIO: MODA, VALOR QU MAI OCORRE)
dataset['Genero'].fillna('Masculino', inplace=True)
#verificando valores nulos novamente
print(f"Valores nulos para genero: {dataset['Genero'].isnull().sum()}")

# PADRONIZANDO COLUNAS DE ACORCO COM DOMINIO
dataset.loc[dataset['Genero'] == 'M', 'Genero'] = "Masculino"
dataset.loc[dataset['Genero'].isin(['Fem', 'F']), 'Genero'] = "Feminino"

# visualizando o resultado da padronização
print()
agrupado_genero = dataset.groupby(['Genero']).size()
print(agrupado_genero)
print()


print("Score","=" * 40)
# VALORES NUMERICOS ##############################################################
#Score
score = dataset['Score'].describe()
print(score)
#sns.boxplot(dataset['Score']).set_title('Score')
#sns.displot(dataset['Score'])
print()

# IDADE ##############################################################
print('Idade',"=" * 40)
idade = dataset['Idade'].describe()
print(idade)
#sns.boxplot(dataset['Idade']).set_title('Idade')
#sns.displot(dataset['Idade']).set_title('Idade')
print()
# visulizar possuveis outliers
print("Outliers: ",dataset.loc[(dataset['Idade'] < 0 | (dataset['Idade'] > 120))])
print()
# calculando a mediana
idade_mediana = sts.median(dataset['Idade'])
print(f"Mediana das idades: {idade_mediana}")
# substituindo os valores outliers pela mediana (menos suscetivel a outliers)
dataset.loc[(dataset['Idade'] < 0 | (dataset['Idade'] > 120))] = idade_mediana
#checkando resultado
print("Checkando resultado: ",dataset.loc[(dataset['Idade'] < 0 | (dataset['Idade'] > 120))])
print()


print('Saldo',"=" * 40)
# SALDO ##############################################################
saldo = dataset['Saldo'].describe()
print(saldo)

#sns.boxplot(dataset['Saldo']).set_title('Saldo')
#sns.displot(dataset['Saldo']).set_title('Saldo')

# SALARIO ##############################################################
print('Salario',"=" * 40)
salario = dataset['Salario'].describe()
print(salario)

mediana_salario = sts.median(dataset['Salario'])
print(f'Mediana Salario: {mediana_salario}')

# substituindo os valores de salario nulo pela mediana
dataset['Salario'].fillna(mediana_salario, inplace=True)
print(f"Campo salario nulos: {dataset['Salario'].isnull().sum()}")
print()
# buscando outliers para salario, vamos considerar duas vezes o desvio padrao
salario_desv  = sts.stdev(dataset['Salario'])
print(f"Desvio padrao em salario: {salario_desv}")

# atribuir a media aos valores outliers
dataset.loc[dataset['Salario'] >= 2 * salario_desv ] = mediana_salario

# checar se temos salarios em desvio padrao
print("Salarios acima do desvio padrao")
print(dataset.loc[dataset['Salario'] >= 2 * salario_desv ])
print()



#sns.boxplot(dataset['Salario']).set_title('Salario')
#sns.displot(dataset['Salario']).set_title('Salario')
print()

# VERIFICANDO VALORES NULOS ##############################################################
print('Valores NAN',"=" * 40)
nulos = dataset.isnull().sum()
print(nulos)
print()

# VALORES DUPLICADOS ##############################################################
print(dataset.duplicated(['Id'], keep=False))
print()
dataset.drop_duplicates(subset='Id', keep='first', inplace=True)
print(dataset.duplicated(['Id'], keep=False))
print()

# VERIFICANDO MAIS UMA VEZ A ESTRUTURA DO D.F
print(dataset.head())
print(dataset.shape)
print(dataset.tail())