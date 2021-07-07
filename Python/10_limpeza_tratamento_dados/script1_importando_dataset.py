import pandas as pd
import seaborn as srn
import statistics as sts




def create_dataset():
    file = "C:/Users/fabio.classo/Downloads/fabio/estudos/R_lang/formacao_cientista_de_Dados/R/download/dados/Churn.csv"

    dataset = pd.read_csv(file, sep=";")
    #print(dataset.head())
    #print(dataset.shape)

    #RENOMEANDO AS COLUNAS
    dataset.columns = [
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
    ]
    # Checanod os nomes das colunas
    #print(dataset.head())
    return dataset

if __name__ == "__main__":
    dataset = create_dataset()
    print(dataset.head())
