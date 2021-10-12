# Testes de normalidade

set.seed(123) # para poder repetir experimento com mesmos dados

# rnorm geral mil linhas normalmente distribuidas
x = rnorm(1000)

# gera o grafico
qqnorm(x)
# geera a linha
qqline(x)

# Teste de shapiro
# Valor de p  acima de 0.5, não hpa indício para não confirmar a hipótese nula de
# normalmente distribuídos

shapiro.test(x)

#Histograma com linha de densidade

hist(x, main="")
par(new=TRUE)
plot(density(x), ylab="", xlab="",axes=F, lwd=2.5)


# Dados não normalmente distribuídos

install.packages("semTools")
library(semTools)
m = mvrnonnorm(1000, c(1,2), matrix(c(10, 2,2,5),2,2), 
               skewness = c(5,2), kurtosis = c(3,3))


qqnorm(m)
qqline(m)

shapiro.test(m)

hist(m, main="")
par(new=TRUE)
plot(density(m), ylab="", xlab="",axes=F, lwd=2.5)
