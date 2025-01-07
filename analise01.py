
from main_02 import vendas_df
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Verificando base
# print(vendas_df.head())

# Resumo estatístico
# print(vendas_df.describe())

# Contagem de registros
print(f'Total de registros (linhas): {vendas_df.shape[0]}')
print(f'Total de variáveis (colunas): {vendas_df.shape[1]}')

# Ordenação por valor_total
# print(vendas_df.sort_values(by='valor_total', ascending=False))

# Identificar outliers e removê-los 
"""
Para identificação de outliers, temos o IQR (interquartil).
IQR = Q3 - Q1

Idenficar valores que estejam fora do intervalo:
Abaixo de: [Q1 - 1.5*IQR]
Acima de: [Q3 + 1.5*IQR]
"""

# Primeiro passo: Identificar Q1 / Q3 / IQR
q1 = vendas_df['valor_total'].quantile(0.25)
q3 = vendas_df['valor_total'].quantile(0.75)
iqr = q3 - q1

# Segundo passo: Identificar limite inferior e superior
limite_inferior = q1 - 1.5*iqr
limite_superior = q3 + 1.5*iqr
# print(f'Limite inf: {limite_inferior}.\nLimite sup: {limite_superior}')

"""AQUI ESTÁ O DF SEM OUTLIERS"""
# Terceiro passo: filtrar os dados removendo outliers
vendas_df02 = vendas_df[(vendas_df['valor_total'] >= limite_inferior) & (vendas_df['valor_total'] <= limite_superior)]
# print(vendas_df02.sort_values(by='valor_total', ascending=False).head())
""" --------------------------"""

# Removendo linhas onde o valor_total está zerado
vendas_df02 = vendas_df02[(vendas_df02['valor_total'] != 0)]
# print(vendas_df02.describe())

# Pedidos por país
vendas_por_pais = vendas_df02['nome_pais'].value_counts()
# print(vendas_por_pais)

# Produto mais vendido
prod_mais_vendido = vendas_df02['descricao'].value_counts().idxmax()
# print(prod_mais_vendido)

# Valor médio dos pedidos por país
valor_medio_pais = vendas_df02.groupby('nome_pais')['valor_total'].mean().sort_values(ascending=False)
#print(valor_medio_pais)

# Agrupar pela quantidade de pedidos
qtde_pedidos_cliente = vendas_df02.groupby('id_cliente')['numero_fatura'].count().sort_values(ascending=False)
# print(qtde_pedidos_cliente.head(15))