import streamlit as st
import pandas as pd
import plotly.express as px


st.title('Titanic dashboard')
st.set_page_config(layout='wide')

df=pd.read_csv('titani_data.csv')

df['Embarked'] = df['Embarked'].fillna('Unkown')


embarked_port= df['Embarked'].unique()
gender= list(df['Sex'].unique())


col1, col2= st.columns([1,1])
selected_port = col1.selectbox('Select Port of Embarkation', embarked_port)
selected_gender = col2.selectbox('Select Gender', gender)




