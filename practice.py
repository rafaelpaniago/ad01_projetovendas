import pandas as pd

df_vendas = pd.read_csv(r'C:\Users\rpani\workspace\sells_python\sells_python\dados\data.csv', encoding='latin1')

# print(df_vendas.head())

# A parte a seguir só será executada neste arquivoi

if __name__ == "__main__":
    
    # Tipo de dados
    print(df_vendas.info())
    
    # Valores nulos
    print(df_vendas.isnull().sum())
    
    # Apenas valores nulos
    df_nulos = df_vendas[df_vendas['CustomerID'].isnull()]
    print(df_nulos.tail())
    
    # Contar caracteres de stockcode
    contador_carac = df_vendas[df_vendas['StockCode'].str.len() < 6]
    print(contador_carac.head())