
# Teorema central do limite

# omitir warnings
options(warn=1)

install.packages("semTools")
library(semTools)

# Inicializa um vetor
z = rep(0, 500)

# Gera amostras
for (i in 1:500){
         m = mvrnonnorm(1000, c(1, 2),matrix(c(10,2,2,5),2,2),
                        skewness = c(5,2), kurtosis = c(3,3))

         # grava média das amostras
         z[i] = mean(m)
         
        # imprime as 3 primeiras linhas
         if (i<4){
           hist(m, breaks = 50, main=paste("Histograma", i))
         }
         
}

# Imprime a distribuição média das amostras
hist(z)




