from scipy.stats import norm

# conjunto de objetos em uma cesta,  a média  é 8 e o desvio padrão é 2
# Qual a probabilidade de tirar um obketo cuko peso é menos que 6 kg?
print(norm.cdf(6, 8, 2))
print("="*70)

# Qual a probabilidade de tirar um objeto cujo peso é maior que 6kg?
print(norm.sf(6, 8, 2))
# ou
print(1 - norm.cdf(6,8,2))
print("="*70)

# Qual a probabilidade de tirar um objeto cujo o peso é menor que 6kg 
# ou maior que 10 kg?
print(norm.cdf(6,8,2) + norm.sf(10,8,2))
print("="*70)

# Qual a probabilidade de  tirar um objeto cujo peso é menor que 10k 
# e maior que 8kg?
print(norm.cdf(10,8,2) - norm.cdf(8,8,2))