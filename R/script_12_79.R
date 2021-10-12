# Seção 12 - 79 - TABELAS: Prática em R - Graficose visualizacoes

install.packages("stargazer")
library(stargazer)

# formato latex
stargazer(iris)

# usar https://quicklatex.com/ para renderizar saída


# formato HTML
stargazer(iris, type="html")


# FORMATO TEXTO
stargazer(iris, type="text")


# SALVANDO EM DISCO
stargazer(women, out="women.txt", summary=F)