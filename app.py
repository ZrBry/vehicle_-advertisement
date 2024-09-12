import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")

st.header("Vehicle Advertisement")

button = st.button("Construir histograma")

second_button = st.button("Construir grafico de dispersión")

if button:
    st.write("Creacion de un histograma sobre la transmision para el conjunto de datos de anuncios de venta de coches")

    fig = px.histogram(car_data, x="transmission")

    st.plotly_chart(fig, use_container_width=True)

if button:
    st.write("Creacion de un histograma sobre el kilometraje para el conjunto de datos de anuncios de venta de coches")

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

if second_button:
    st.write("Creacion de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches")

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)