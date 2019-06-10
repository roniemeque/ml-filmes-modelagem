import pandas as pd
import math
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from database import atualiza_grupo

# numero definido usando elbow point
n_clusters = 8

# pegando os usuarios ja com medias processadas
usuarios = pd.read_csv(
    '/Users/ronieeduardomeque/Code/tcc/filmes/public/storage/exports/users.csv')

# separandos os ids de usuarios
usuarios_ids = usuarios.iloc[:, :1]

# separando as medias
medias = usuarios.drop(columns=['id', 'imax'])

# convertendo notas em bools
divisor = 4

notas_booleanas = medias.applymap(lambda nota: 1 if nota >= divisor else 0)

# reposicionando usuarios
usuarios_com_notas_booleanas = pd.concat(
    [usuarios_ids, notas_booleanas], axis=1)

# normalizando notas booleanas
scaler = StandardScaler()
notas_bool_escaladas = scaler.fit_transform(notas_booleanas.values)

modelo_medias_otimizado = KMeans(n_clusters)
modelo_medias_otimizado.fit(notas_bool_escaladas)

grupos_otimizados = pd.DataFrame(modelo_medias_otimizado.cluster_centers_,
                                 columns=medias.columns)

labels = modelo_medias_otimizado.labels_

usuarios['grupo'] = labels

for row in usuarios.itertuples():
    atualiza_grupo(row.id, row.grupo)
