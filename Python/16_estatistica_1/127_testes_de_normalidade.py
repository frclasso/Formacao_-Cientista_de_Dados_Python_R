from scipy import stats
from scipy.stats import norm, skewnorm
import matplotlib.pyplot as plt


# Criação de uma variável com dados em uma distribuição normal com a 
# função ervs (1000 elementos)
dados = norm.rvs(size=1000)
#print(dados)
# 1
# criando histograma com os dados gerados
#plt.hist(dados, bins=20)
#plt.title("Dados")

# 2
# Gerando grafico para verificar distribuição normal
#fig, ax = plt.subplots()
#stats.probplot(dados, fit=True, plot=ax)

# 3
# Teste de Shapiro 
# o segundo valor é o valor de p, não há como rejeitar hipótese nula
print(stats.shapiro(dados))

# DADOS NÃO NORMAIS
dados2 = skewnorm.rvs(4, size=1000)

# histograma
#plt.hist(dados2, bins=20)
#plt.title('Dados 2')

 # Gerando gráfico para verificar se a distribuição é normal
#fig, ax = plt.subplots()
#stats.probplot(dados2, fit=True, plot=ax)
#plt.show()

# Teste de shapiro
print(stats.shapiro(dados2))