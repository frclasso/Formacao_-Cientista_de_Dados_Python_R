# Amostragem estratificada
install.packages("sampling")
library(sampling)

proporcao = 25

# método srswor = amostra simples  sem reposição ,
# método srswr = com reposição
# outros métodos poisson, systematic


# strata = amostra estratificada
amostrairis2 = strata(data=iris, 
                    stratanames=c("Species"), size=c(rep(proporcao,3)),method="srswor")


print(summary(amostrairis2))

# Dados de infertilidade
infert
summary(infert)
amostra = strata(data = infert,
                 stratanames = c("education"),
                 size=c(5, 48, 47),
                 method = "srswor")

summary(amostra)
