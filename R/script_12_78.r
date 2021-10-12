# Seção 12 - 78: Prática em R - Graficose visualizacoes

# data frame
trees

# vers 1
boxplot(trees$Volume,
         main='Arvores',
         xlab="Volume"
         )

# vers 2
boxplot(trees$Volume,
        main='Arvores',
        xlab="Volume",
        col = "blue",
        horizontal = T
)


# vers 3, eliminando o outlier
boxplot(trees$Volume,
        main='Arvores',
        xlab="Volume",
        col = "blue",
        horizontal = T,
        outline = F
)

# vers 4, notch
boxplot(trees$Height,
        main='Arvores',
        xlab="Volume",
        col = "blue",
        horizontal = F,
        outline = F,
        notch = TRUE
)
# verificando dados utilizados para gerar o grafico
boxplot.stats(trees$Height)
#acessando apenas uma variavel
boxplot.stats(trees$Height)$stats

#varios graficos
boxplot(trees)

# AGREGAÇÕES
# VAMOS UTILIZAR O CONJUNTO DE DADOS INSECTSPRAYS
InsectSprays
spray = aggregate(. ~spray, data = InsectSprays,sum)
spray

# GRAFICO DE BARRAS
barplot(
  spray$count, 
  col=gray.colors(6), 
  xlab="Spray",
  ylab = "Total",
  names.arg = spray$spray
  )
box()

# GRAFICO DE SETOR(PIZZA)
pie(
  spray$count, 
  labels = spray$spray, 
  main = "Spray", 
  col=c(1:6)
  )


# GRAFICO DE SETOR(PIZZA) -- COM LEGENDA
pie(
  spray$count, 
  labels =NA, 
  main = "Spray", 
  col=c(1:6))
legend("bottomright", legend = spray$spray, cex=1, fill = c(1:6))

