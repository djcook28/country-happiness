import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Country Happiness Factor Correlation')

df = pd.read_csv('happy.csv')

df.columns = df.columns.str.replace("_", " ").str.title()
df_columns = df.columns.to_list()
#removes country as an option.  Countries is a label not a data point
df_columns.pop(0)

x_axis = st.selectbox('Select the data for the X-axis', options=df_columns)

y_axis = st.selectbox('Select the data for the Y-axis', options=df_columns)

st.subheader(f'{x_axis} and {y_axis}')
figure = px.scatter(data_frame=df, x=df[x_axis], y=df[y_axis])
st.plotly_chart(figure)