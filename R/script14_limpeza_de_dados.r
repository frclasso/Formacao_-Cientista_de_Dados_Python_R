# Limpeza e tratamento de dados
#print(getwd())
file = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/R/download/dados/Churn.csv"
dados = read.csv(file, sep=";", na.strings="")

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
print("==================================================================")
# VERIFICNADO VALORES FALTANTES
print(dados[!complete.cases(dados),])
print("==================================================================")
# TRATANDO SALARIOS
print(summary(dados$Salario))
mediana_salarios = median(dados$Salario, na.rm=T)
print(mediana_salarios)

# Atribuir mediana aos NAs
dados[is.na(dados$Salario),]$Salario = mediana_salarios

# Verifica se há NAs
print(dados[!complete.cases(dados$Salario),])
print("==================================================================")
# TRATANDO GENEROS
#print(unique(dados$Genero))
dados[is.na(dados$Genero) | dados$Genero == "M", ]$Genero = "Masculino"
dados[dados$Genero =="F" | dados$Genero == "Fem", ]$Genero = "Feminino"

# remover levels nao utilizados
dados$Genero = factor(dados$Genero)
print(summary(dados$Genero))
print("==================================================================")
# Idades
print(summary(dados$Idade))
print(dados[dados$Idade < 0 | dados$Idade > 110,]$Idade)
print(dados[is.na(dados$Idade),])
#atribuindo a mediana aos valores indesejados
mediana_ = median(dados$Idade)
dados[dados$Idade < 0 | dados$Idade > 110,]$Idade = mediana_
#print(dados[dados$Idade < 0 | dados$Idade > 110,]$Idade)
print(summary(dados$Idade))
print("==================================================================")
# buscando registros duplicados
duplicados = dados[duplicated(dados$Id),]
print(duplicados)
dados = dados[-c(82),]
print(dados[dados$Id == duplicados$Id, ])
print("==================================================================")
# ESTADO FORA DO DOMINIO
print(unique(dados$Estado))
#print(summary(dados$Estado))

# preencher com a moda RS
dados[!dados$Estado %in% c("RS", "SC", "PR"), ]$Estado = "RS"
#print(summary(dados$Estado))

# removendo factores nao usados
dados$Estado =factor(dados$Estado)
print(summary(dados$Estado))
print("==================================================================")
# OUTLIERS
desvio_salario = sd(dados$Salario, na.rm =T)
print(desvio_salario)
print(dados[dados$Salario >= 2 * desvio_salario,]$Salario)
#boxplot(dados$Salario, outline = F)
#outliers_ = boxplot(dados$Salario)$out
#print(outliers_)

# atualizando outliers para mediana
mediana_salarios_out = median(dados$Salario)
dados[dados$Salario >= 2 * desvio_salario, ]$Salario = mediana_salarios_out
#check
print(dados[dados$Salario >= 2 * desvio_salario,]$Salario)