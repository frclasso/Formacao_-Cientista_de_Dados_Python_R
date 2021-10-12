# Seção 12: Prática em R - Graficose visualizacoes 
#View(trees)
trees
hist(trees$Height)

hist(
  trees$Height,
  main= "Arvores",
  ylab="Frequencia",
  xlab="Altura",
  col="blue")

hist(
  trees$Height,
  main= "Arvores",
  ylab="Frequencia",
  xlab="Altura",
  col="blue",
  density = 20,
  breaks = 20
  )

# DENSIDADE
densidade = density(trees$Height)
plot(densidade)

# DENSIDADE SOBRE O HISTOGRAMA
hist(trees$Height, main = NULL, xlab = NULL, ylab = NULL)
par(new=TRUE)
plot(densidade)

# DISPERSÃO
#versao 1
plot(trees$Girth, trees$Volume)

#versao 2
plot(trees$Girth, trees$Volume, main = "Arvores")

#versao 3
plot(trees$Girth, 
     trees$Volume, 
     main = "Arvores",
     xlab = "Volume",
     ylab = "Circunferencia",
     col="blue"
    )
#versao 4
plot(trees$Girth, 
     trees$Volume, 
     main = "Arvores",
     xlab = "Volume",
     ylab = "Circunferencia",
     col="blue",
     pch=20  # pch muda elemento gráfico
)

# MUDANDO O TIPO DE GRAFICO

#versao 5
plot(trees$Girth, 
     trees$Volume, 
     main = "Arvores",
     xlab = "Volume",
     ylab = "Circunferencia",
     col="blue",
     pch=20,  # pch muda elemento gráfico
     type = 'l'
)

# TRENULAÇÃO, diminui a sobreposição

#versao 5
plot(jitter(trees$Girth), 
     trees$Volume, 
     main = "Arvores",
     xlab = "Volume",
     ylab = "Circunferencia",
     col="blue"
     
)

# LEGENDA COM DIMENSÃO CATEGÓRICA
CO2
plot(CO2$conc, CO2$uptake, pch=20, col=CO2$Treatment)
legend("bottomright", legend = c("nonchilled", "chilled"), cex=1, fill=c("black", "red"))


# NOVOS DADOS
plot(trees)

# DIVISAO DE TELA
split.screen(figs = c(2,2)) # divisao na tela
screen(1) # escolhe tela 1
plot(trees$Girth, trees$Volume)
screen(2)
plot(trees$Girth, trees$Height)
screen(3)
plot(trees$Height, trees$Volume)
screen(4)
plot(trees$Volume)
close.screen(all=T)