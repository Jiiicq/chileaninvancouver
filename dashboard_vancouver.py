# Importar librerías necesarias
import pandas as pd
import plotly.express as px
import streamlit as st

# Crear el DataFrame con datos de más países latinoamericanos
data = {
    "Barrio": ["Burnaby", "Coquitlam", "Surrey", "Vancouver East", "Richmond"],
    "Poblacion_Chilena": [500, 300, 250, 150, 100],
    "Poblacion_Argentina": [200, 150, 120, 90, 80],
    "Poblacion_Peruana": [180, 120, 100, 80, 50],
    "Poblacion_Mexicana": [300, 200, 170, 130, 90],
    "Poblacion_Brasilena": [150, 100, 90, 60, 40]
}
df = pd.DataFrame(data)

# GeoJSON simplificado para los barrios de Vancouver
vancouver_geojson = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature", "properties": {"Barrio": "Burnaby"}, "geometry": {"type": "Polygon", "coordinates": [[[-123.0208, 49.2488], [-122.8992, 49.2488], [-122.8992, 49.3054], [-123.0208, 49.3054], [-123.0208, 49.2488]]]}},
        {"type": "Feature", "properties": {"Barrio": "Coquitlam"}, "geometry": {"type": "Polygon", "coordinates": [[[-122.8405, 49.2748], [-122.6831, 49.2748], [-122.6831, 49.3201], [-122.8405, 49.3201], [-122.8405, 49.2748]]]}},
        {"type": "Feature", "properties": {"Barrio": "Surrey"}, "geometry": {"type": "Polygon", "coordinates": [[[-122.8892, 49.0876], [-122.7208, 49.0876], [-122.7208, 49.2504], [-122.8892, 49.2504], [-122.8892, 49.0876]]]}},
        {"type": "Feature", "properties": {"Barrio": "Vancouver East"}, "geometry": {"type": "Polygon", "coordinates": [[[-123.1024, 49.2504], [-123.0288, 49.2504], [-123.0288, 49.2768], [-123.1024, 49.2768], [-123.1024, 49.2504]]]}},
        {"type": "Feature", "properties": {"Barrio": "Richmond"}, "geometry": {"type": "Polygon", "coordinates": [[[-123.1745, 49.1118], [-123.0237, 49.1118], [-123.0237, 49.1973], [-123.1745, 49.1973], [-123.1745, 49.1118]]]}}
    ]
}

# Crear el selector en Streamlit para elegir el país a visualizar
st.title("Distribución de la Población Latinoamericana en Vancouver")
st.markdown("""
Este dashboard muestra la distribución de las comunidades latinoamericanas en los principales barrios de Vancouver.
Selecciona el país para ver la distribución correspondiente.
""")

# Crear un selector de país para visualizar
paises = ["Poblacion_Chilena", "Poblacion_Argentina", "Poblacion_Peruana", "Poblacion_Mexicana", "Poblacion_Brasilena"]
pais_seleccionado = st.selectbox("Selecciona la comunidad latinoamericana a visualizar:", paises)

# Crear el gráfico de coropletas con el país seleccionado
fig = px.choropleth_mapbox(
    df,
    geojson=vancouver_geojson,
    locations='Barrio',
    featureidkey="properties.Barrio",
    color=pais_seleccionado,
    color_continuous_scale="Oranges",
    mapbox_style="carto-positron",
    zoom=9,
    center={"lat": 49.2827, "lon": -123.1207},
    opacity=0.6,
    labels={pais_seleccionado: 'Población'},
    title=f"Distribución de la {pais_seleccionado.split('_')[1]} en Vancouver"
)

# Mostrar el gráfico en el dashboard
st.plotly_chart(fig)
