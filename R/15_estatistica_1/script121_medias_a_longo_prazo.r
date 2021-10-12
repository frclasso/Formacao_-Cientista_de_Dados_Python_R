# Pequenas e grandes amostras
# espera-se uma media  de 3.5 

# Amostra pequena

x = sample(1:6,6, replace=T)
mean(x)

# Amostra grande
y = sample(1:6,10000, replace=T)  # variação muito próxima de 3.5
mean(y)