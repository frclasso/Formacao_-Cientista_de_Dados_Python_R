import os
import pandas as pd
from sklearn.model_selection import train_test_split

file_path = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/Python/13_visualizacao_de_dados/"
os.chdir(file_path)

iris = pd.read_csv('./dados/iris.csv')
print(iris.head())
print()
print(iris['variety'].value_counts())
print()

X_train, X_test, y_train,y_test = train_test_split(
    iris.iloc[:, 0:4],
    iris.iloc[:, 4],
    test_size=0.5,
    stratify=iris.iloc[:,4]
)

print(y_train.value_counts())
print()

infert = pd.read_csv("./dados/infert.csv")
print(infert)
print()

# varificando as faixas etárias , coluna "edication"
print(infert['education'].value_counts())
print()

# Gerando amostra extratificada com somente 40% dos registros( test_size=0.6)
X1_train, X1_test, y1_train, y1_test = train_test_split(
    infert.iloc[:, 2:9],
    infert.iloc[:, 1],
    test_size=0.6,
    stratify=infert.iloc[:, 1]
)
print(y1_train.value_counts())