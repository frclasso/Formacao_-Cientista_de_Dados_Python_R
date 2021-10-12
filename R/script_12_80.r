# sessao 12-80

library(lattice)
# Gerando boxplot com lattice
bwplot(trees$Volume)

#versao 2
bwplot(
  trees$Volume,
  main="Arvores",
  xlab="Volume"
  )

# Histograma com lattice
#aspecto pe a proporção , nint número de quebras, type: percent, coun, density
histogram(
  trees$Volume,
  main="Arvores",
  xlab="Volume",
  aspect=1,
  type="percent",
  nint=20
        )

# Peso de galinhas de acordo com a alimentação
chickwts
histogram(chickwts$weight)
#agregação
aggregate(chickwts$weight, by=list(chickwts$feed), FUN=sum)
#histograma condicional
histogram( ~weight | feed, data=chickwts)


# Graficos de dispersão condicional
#CO2 , seis plantas em dois locais, refrigeradas ou não durante a noite
CO2
xyplot(CO2$conc ~ CO2$uptake)
#type é a origem
xyplot(CO2$conc ~ CO2$uptake | CO2$Type)
# refrigeado ou não
xyplot(CO2$conc ~ CO2$uptake | CO2$Treatment)

#Cance de esofago
# agegp: idade, alcpg:alcool, tobgp: tabaco
esoph
dotplot(esoph$alcgp ~esoph$ncases, data=esoph)

dotplot(esoph$alcgp ~esoph$ncontrols | esoph$tobgp)

# Matriz de dispersão com lattice
splom(~CO2[4:5] | CO2$Type, CO2)

# Densidade Condicional
densityplot(~CO2$conc | CO2$Treatment, plot.points=F) # conc =concentração
densityplot(~CO2$conc | CO2$Treatment)

# Grafico 3D
# spray para repeli abelhas
OrchardSprays
cloud(
  decrease ~ rowpos * colpos, 
  data=OrchardSprays
  )

# versao 2
cloud(
  decrease ~ rowpos * colpos, 
  data=OrchardSprays,
  groups = treatment)

# levelplot Circunferencia, largura e volume das arvores
levelplot(Girth ~ Height * Volume, data = trees)
