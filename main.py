import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Country Happiness Factor Correlation')

df = pd.read_csv('happy.csv')

columns = df.columns.to_list()
columns.pop(0)

x_axis = st.selectbox('Select the data for the X-axis', options=df.columns)

y_axis = st.selectbox('Select the data for the Y-axis', options=df.columns)

figure = px.scatter(data_frame=df, x=df[x_axis], y=df[y_axis])
st.plotly_chart(figure)