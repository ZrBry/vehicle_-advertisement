import pandas as pd
import streamlit as st 
import plotly.express as px
import matplotlib as plt

data = pd.read_csv("./vehicles_us.csv")
#print(data.info())
#print(data.sample(10))
#print(data["transmission"].sample(20))

fig = px.histogram(data, "transmission")
fig.show()

st.plotly_chart(fig)
