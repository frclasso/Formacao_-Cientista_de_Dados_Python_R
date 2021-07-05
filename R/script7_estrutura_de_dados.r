#numeros
delta= 9
print(class(delta))
print(delta)

gama = 8L
print(class(gama))

verdadeiro = TRUE
falso = F

print(class(verdadeiro))
print(class(falso))

nome = "FABIO"
print(class(nome))

print(sqrt(25))

#vetores
x = c(1,2,3,4,5,6)
print(x)
x[1]=10
print(x[1])
print("----------------------------")
y = c('a', 'b', 'c')
print(y)
print("----------------------------")
z = c(1L, 2L, 3L)
print(z)
print(class(z))
print("----------------------------")
print(colnames(VADeaths))
print(rownames(VADeaths))
print("----------------------------")
print(VADeaths)
print("----------------------------")
print(VADeaths[1:3,])
print("----------------------------")
print(VADeaths[c(1,3,5),])
print("----------------------------")
print(longley)
print("----------------------------")
print(longley[,1:3]) # colunas de 1 a 3
print("----------------------------")
print(longley[1:4,1:3]) # linhas de 1 a 4 e colunas de 1 a 3
print("----------------------------")
print(longley$Unemployed)
print("----------------------------")
print(longley['Unemployed'])
print("----------------------------")
print(ability.cov)
print("----------------------------")
print(ability.cov$cov)
print("----------------------------")
print(ability.cov[1])
print(class(ability.cov$cov))
print(class(ability.cov$center))
print("----------------------------")
print(ability.cov$cov)
print("----------------------------")
print(ability.cov$cov[, 1:3])
print("----------------------------")
# FATORES
print(state.region)