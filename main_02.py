"""
Aqui serão feitos os ajustes no dataframe.

1. Renomear colunas
2. Ajustar tipo de dado das colunas data e ID
3. Adicionar coluna 'total_valor'
4. Remover dados ausentes

"""
import pandas as pd
from main import vendas

# Ajustar nomes das colunas

vendas = vendas.rename(columns={'InvoiceNo':'numero_fatura'})
vendas = vendas.rename(columns={'StockCode':'codigo_estoque'})
vendas = vendas.rename(columns={'Description':'descricao'})
vendas = vendas.rename(columns={'Quantity':'quantidade'})
vendas = vendas.rename(columns={'InvoiceDate':'data_fatura'})
vendas = vendas.rename(columns={'UnitPrice':'preco_unidade'})
vendas = vendas.rename(columns={'CustomerID':'id_cliente'})
vendas = vendas.rename(columns={'Country':'nome_pais'})


# Tipo de dados
# print(vendas.dtypes)

# Ajustando tipo de dado coluna DATA
vendas['data_fatura'] = pd.to_datetime(vendas['data_fatura'])

# Ajustando tipo de dado coluna id
vendas['id_cliente'] = vendas['id_cliente'].astype('object')

# Criar coluna 'valor total'
vendas['valor_total'] = vendas['quantidade']*vendas['preco_unidade']

# Remover linhas com valores nulos
vendas = vendas.dropna()

# Verificar valores nulos
# print(vendas.isnull().sum())

# Verificar dataframe pronto para análises
vendas_df = vendas
# print(vendas_df.head())
# print(vendas_df.info())