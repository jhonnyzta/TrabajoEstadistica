import os

dir_file = os.path.join(os.path.dirname(__file__), '../..', 'reports/by_country')

def make_md(key_format):
    route_file = f"{dir_file}/{key_format['country']}.md"
    content_format = contenido_md.format(**key_format)
    with open(route_file, 'w') as file_md:
        file_md.write(content_format)


contenido_md = """
# Reporte de resultados {country}

A continuación se presentan algunos resultados obtenidos.

## Medidas de tendencia

En la siguiente tabla se reportan los resultados de las medidas media, desviación estándar muestral, y los cuartiles.

| Conjunto de datos | media | desviación estándar | Q1 | Q2 | Q3 |
| :-- | :--: | :--: | :--: | :--: | :--: |
| Hombres Urbano | {men_urban[mean]:.3f}  | {men_urban[std_dev]:.3f}  | {men_urban[quartil][0]:.3f} | {men_urban[quartil][1]:.3f}  | {men_urban[quartil][2]:.3f} |
| Hombres Rural | {men_rural[mean]:.3f}  | {men_rural[std_dev]:.3f}  | {men_rural[quartil][0]:.3f} | {men_rural[quartil][1]:.3f}  | {men_rural[quartil][2]:.3f} |
| Mujeres Urbano | {women_urban[mean]:.3f}  | {women_urban[std_dev]:.3f}  | {women_urban[quartil][0]:.3f} | {women_urban[quartil][1]:.3f}  | {women_urban[quartil][2]:.3f} |
| Mujeres Rural | {women_rural[mean]:.3f}  | {women_rural[std_dev]:.3f}  | {women_rural[quartil][0]:.3f} | {women_rural[quartil][1]:.3f}  | {women_rural[quartil][2]:.3f} |


## Gráficos

A continuación se presentan los gráficos generados a partir del conjunto de datos.


#### Diagrama de barras 

Para los diagramas de barras se representan los valores 

#### Gráfico de barras Urbano

<p align="center">
<img src="../../graphics/{country}/barras_urban.png" alt="Graphic 1" width="400" height="300">
</p>

#### Gráfico de barras Rural

<p align="center">
<img src="../../graphics/{country}/barras_rural.png" alt="Graphic 2" width="400" height="300">
</p>

#### Diagrama de bigotes

##### Hombres urbano

<p align="center">
<img src="../../graphics/{country}/bigotes_urban_men.png" alt="Graphic 3" width="400" height="300">
</p>

##### Hombres rural

<p align="center">
<img src="../../graphics/{country}/bigotes_rural_men.png" alt="Graphic 4" width="400" height="300">
</p>

##### Mujeres urbano

<p align="center">
<img src="../../graphics/{country}/bigotes_urban_men.png" alt="Graphic 5" width="400" height="300">
</p>

##### Mujeres rural

<p align="center">
<img src="../../graphics/{country}/bigotes_rural_women.png" alt="Graphic 6" width="400" height="300">
</p>


"""