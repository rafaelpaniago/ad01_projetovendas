import pandas as pd

df_vendas = pd.read_csv(r'C:\Users\rpani\workspace\sells_python\sells_python\dados\data.csv', encoding='latin1')

# Testar a base de dados
# print(df_vendas.head())
# print(df_vendas.tail())

# # Tipo de dados das colunas
# print(df_vendas.dtypes)
# df_qtde = df_vendas.sort_values(by='Quantity', ascending=False)
# print(df_qtde.head())

# # Verificar quantidade de linhas e colunas
# print(df_vendas.shape)

# # Valores nulos / ausentes. Entender e pensar solução.
# print(df_vendas.isnull().sum())

# Criar nova coluna com valor total compra
df_vendas['valor_total'] = df_vendas['Quantity']*df_vendas['UnitPrice']
print(df_vendas.head())

# Valor total somado
print(df_vendas['valor_total'].sum())

# Valor total somado apenas para ids nulos
print(df_vendas[df_vendas['CustomerID'].isna()]['valor_total'].sum())



"""
--- ANOTAÇÕES ---

1. Customer ID deve ser object (string)
2. InvoiceDate deve ser data
3. Criar uma coluna com o valor total da compra (qtde * valor_unit)
"""
