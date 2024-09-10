import streamlit as st
import pandas as pd
import plotly_express
car_data = pd.read_csv("vehicles_us.csv")
st.header("Vehicle Advertisement")
first_button = st.button("Construir histograma")
second_button = st.button("construir grafico de dispersión")

if first_button:
    st.write("Creacion de un histograma para el conjunto de datos de anuncios de venta de coches")

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

if second_button:
    st.write("Creacion de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches")

    fig = px.histogram(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)