import pandas as pd
import plotly..express as px
import streamlit as st



st.set_page_config(
    layout='wide',)
df= pd.read_csv('share-of-individuals-using-the-internet.csv')
df= df[(df['Year'] >=2000) & (df['Year'] <= 2016)]
print(df.columns())
print(df.info())


years= df['Year'].unique()
country = df['Country'].unique(
)
selected_year= st.selectbox(label='Year', options=years)

selected_country= st.selectbox(label='Country', options=country)


st.header('Internet Usage DashBoard')
