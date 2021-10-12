# Medidas de centralidade e variabilidade

# salario dos jogadores
jogadores= c(40000,18000, 12000, 250000,30000,140000,300000, 40000,800000)

# Media
mean(jogadores)

# Mediana
median(jogadores)

# Quartis
quartis=  quantile(jogadores)
quartis

# Acessar apenas um quartil, utilizamdo o indice
# terceiro quartil
quartis[4]

# Desvio padrao
sd(jogadores)

# Resumo
summary(jogadores)