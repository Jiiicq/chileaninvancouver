import pandas as pd
import plotly.express as px
import streamlit as st

# Datos de ejemplo para la población chilena en barrios de Vancouver
data = {
    "Barrio": ["Burnaby", "Coquitlam", "Surrey", "Vancouver East", "Richmond"],
    "Poblacion_Chilena": [500, 300, 250, 150, 100]
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

# Crear el mapa interactivo usando Plotly
fig = px.choropleth_mapbox(
    df, 
    geojson=vancouver_geojson, 
    locations='Barrio', 
    featureidkey="properties.Barrio", 
    color='Poblacion_Chilena',
    color_continuous_scale="Blues",
    mapbox_style="carto-positron",
    zoom=9,
    center={"lat": 49.2827, "lon": -123.1207},
    opacity=0.6,
    labels={'Poblacion_Chilena': 'Chilean Population'},
    title="Distribution of Chilean Population in Vancouver Neighborhoods"
)

# Mostrar el gráfico con Streamlit
st.title("Distribución de la población chilena en Vancouver")
st.plotly_chart(fig)
