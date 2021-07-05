# Limpeza e tratamento de dados
#print(getwd())
file = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/R/download/dados/Churn.csv"
dados = read.csv(file, sep=";", na.strings="")
print(head(dados))
print("==================================================================")
print(summary(dados))
print("==================================================================")
# Atribuindo nomes as colunas
colnames(dados) = c(
    "Id",
    "Score",
    "Estado",
    "Genero",
    "Idade",
    "Patrimonio",
    "Saldo",
    "Produtos",
    "TemCartCredito",
    "Ativo",
    "Salario",
    "Saiu"
)

print(head(dados))
print("==================================================================")
#ESTADOS
#counts = table(dados$Estado)
#barplot(counts, main="Estados", xlab="Estados")
print("==================================================================")
#GENERO
#counts = table(dados$Genero)
#barplot(counts, main="Generos", xlab="Generos")
print("==================================================================")
#SCORE
print(summary(dados$Score))
#boxplot(dados$Score)
#hist(dados$Score)
print("==================================================================")
#IDADE
print(summary(dados$Idade))
#boxplot(dados$Idade)
#hist(dados$Idade)
print("==================================================================")
#SALDO
print(summary(dados$Saldo))
#boxplot(dados$Saldo)
#hist(dados$Saldo)
print("==================================================================")
#SALARIO
print(summary(dados$Salario))
#boxplot(dados$Salario)
#hist(dados$Salario)
print("==================================================================")
