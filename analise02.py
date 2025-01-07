from analise01 import vendas_df02
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


print(vendas_df02.tail())
print(vendas_df02.dtypes)
print(vendas_df02.columns)

# Total gasto e número de pedidos por cliente
clientes = vendas_df02.groupby('id_cliente').agg({
    'valor_total': 'sum',
    'numero_fatura': 'nunique',
    'data_fatura': lambda x: x.dt.month.mode()[0]
}).rename(columns={
    'valor_total': 'total_gasto',
    'numero_fatura': 'nota_fiscal',
    'data_fatura': 'mes_freq'
})

# Padronização
scaler = StandardScaler()
clientes_scaled = scaler.fit_transform(clientes[['total_gasto', 'nota_fiscal']])

# Aplicação do kmeans
kmeans = KMeans(n_clusters=3, random_state=42)
clientes['cluster'] = kmeans.fit_predict(clientes_scaled)

# Visualizar clusters
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=clientes['total_gasto'], y=clientes['nota_fiscal'],
    hue=clientes['cluster'], palette='viridis', alpha=0.7
)

plt.title('Cluster de clientes')
plt.xlabel('Total')
plt.ylabel('Pedidos')
# plt.show()

# Características
print(clientes.groupby('cluster').mean())
print(vendas_df02.dtypes)