import pandas as pd
from io import StringIO

# Ler a base de dados
with open(r'C:\Users\rpani\workspace\sells_python\sells_python\dados\data.csv', encoding='latin1') as file:
    content = file.read()
    

csv_data = StringIO(content)
vendas = pd.read_csv(csv_data)


# Apenas executar o que estiver abaixo se for o arquivo main

if __name__ == "__main__":
    
    # Testar o carregamento
    print(vendas.head())

    # Informações gerais
    print(vendas.info())

    # Valores ausentes
    print(vendas.isnull().sum())
    
    # DF apenas com valores nulos
    df_nulos = vendas[vendas['CustomerID'].isnull()]
    print(df_nulos.tail())

    # Linhas e colunas
    print(vendas.shape)


