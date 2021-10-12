
# Amostra sistematica
install.packages("TechingSampling")
library(TechingSampling)

# Amostras sistemática de tamanho 150, 10 grupos
amostra = S.SY(150, 10)
amostra

# tamanho
dim(amostra)

amostrairis = iris[amostra,]
amostrairis

dim(amostrairis)