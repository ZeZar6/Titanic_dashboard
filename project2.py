import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

def create_histogram(df,x,title):
    return px.histogram(df, x=x, title=title, color_discrete_sequence=['blue'])
st.set_page_config(layout="wide")
st.title("Project 2: Data Analysis and Visualization")

df= pd.read_csv("iris.csv")

unique_species= df['species'].unique()

col1, col2= st.columns([1,1])

with col1:
    selectedspecies= st.selectbox("Select Species", unique_species, label_visibility="collapsed")
with col2:
    show_hist= st.checkbox("Show histogram",  key='mykey') 
    
    
df_plot= df[df['species']   == selectedspecies]


average_sepal_length= round(df_plot['sepal_length'].mean(), 2)
average_petal_length= round(df_plot['petal_length'].mean(), 2)
average_sepal_width= round(df_plot['sepal_width'].mean(), 2)
average_petal_width= round(df_plot['petal_width'].mean(),2)


col1, col2, col3, col4= st.columns([1,1,1,1])
with col1:
    st.metric("Average Sepal Length", average_sepal_length)
with col2:
    st.metric("Average Petal Length", average_petal_length)
with col3:
    st.metric("Average Sepal Width", average_sepal_width)
with col4:
    st.metric("Average Petal Width", average_petal_width)   
    
color_map = {'setosa': 'gray', 'versicolor': 'gray', 'virginica': 'gray'}

color_map[selectedspecies]= 'blue'

scatter= px.scatter(data_frame=df, x='sepal_length', y='petal_width', size='petal_length', color_discrete_map=color_map, color='species',
                     title=f'Sepal Length vs Petal Width for {selectedspecies}' )


st.plotly_chart(scatter)
    
col1, col2, col3, col4= st.columns([1,1,1,1])



with col1:
    hist1= create_histogram(df, 'sepal_length', f'Sepal Length Distribution for {selectedspecies}')


with col2:
    hist2= create_histogram(df, 'sepal_width', f'Sepal Width Distribution for {selectedspecies}')

with col3:
    hist3= create_histogram(df, 'petal_length', f'Petal Length Distribution for {selectedspecies}')

with col4:
    hist4= create_histogram(df, 'petal_width', f'Petal Width Distribution for {selectedspecies}')


if show_hist:
    col1.plotly_chart(hist1)
    col2.plotly_chart(hist2)
    col3.plotly_chart(hist3)
    col4.plotly_chart(hist4)


