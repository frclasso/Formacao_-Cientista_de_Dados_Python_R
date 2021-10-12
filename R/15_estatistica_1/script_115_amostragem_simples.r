# caso 1
# Gerando uma amostra de 150 valores 0 e 1, com reposição , prob. equivalentes
amostra = sample(c(0,1), 150, replace=T, prob=c(0.5, 0.5)) # mesma probabilidade
amostra
summary(as.factor(amostra))


# caso 2
# Gerando uma amostra de 150 valores 0 e 1, com reposição, maior probabilidade para 0
amostra = sample(c(0,1), 150, replace=T, prob=c(0.7, 0.3))
amostra
summary(as.factor(amostra))


# caso 3
# Gerando uma amostra de 150 valores 1 e 1000, SEM reposição
amostra = sample(c(1:1000), 150, replace=FALSE)
amostra


# seprando 30% dos registros de iris

# gerando uma amosta de conjunto de dados
amostra = sample(c(0,1), 150, replace = TRUE, prob = c(0.7,0.3))
amostra
summary(as.factor(amostra))

#Gera amostra iris
amostrairis = iris[amostra==1,]
amostrairis
dim(amostrairis)

# Repetir experimento (usar set.seed para pegar o mesmo valor aleatorio)
set.seed(2345)
sample(c(1000), 1)

set.seed(2345)
sample(c(1000), 1)




