import numpy as np
from scipy import stats

jogadores = [40000,18000,12000,250000,30000,140000,300000,40000,800000]
print(np.mean(jogadores))
print(np.median(jogadores))
print()
# criação da variável para geração de quartis (0%,25%, 50%, 75%, 100%)
quartis = np.quantile(jogadores,[0, 0.23, 0.5, 0.75, 1])
print(quartis)
print()

# Desvio padrão
print(np.std(jogadores, ddof=1))
print()

# VIsualização de estatpicicas mais detalhadas
print(stats.describe(jogadores))