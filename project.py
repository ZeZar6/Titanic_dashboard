import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px



st.set_page_config(layout="wide")

# page title
st.title("Data Analysis and Visualization App")
# Load the dataset
df = pd.read_csv("gapminder_data_graphs.csv")

unique_years = df['year'].unique()

#add dropdown
selected_year= st.selectbox(label='Select a year', options=unique_years)

df_plot= df[df['year']== selected_year]


average_gdp = round(df_plot['gdp'].mean(), 2)
   
average_life_expectancy = round(df_plot['life_exp'].mean(), 2)

average_hdi = round(df_plot['hdi_index'].mean(), 2)

col1, col2, col3= st.columns([1,1,1], gap="medium")

col1.metric(label="Average GDP", value=average_gdp)
col2.metric(label="Average Life Expectancy", value=average_life_expectancy)
col3.metric(label="Average HDI Index", value=average_hdi)

#add scatter plot
fig = px.scatter(data_frame=df_plot, x='gdp', y='life_exp', color='continent',
                 hover_name='country', 
                 title=f'GDP vs Life Expectancy in {selected_year}')

st.plotly_chart(fig, use_container_width=True)

col1, col2= st.columns([1,1], gap="medium")
with col1:
    #add bar chart
    fig_bar = px.bar(data_frame=df_plot, x='continent', y='gdp', color='continent',
                     title=f'GDP by Continent in {selected_year}')
    st.plotly_chart(fig_bar, use_container_width=True)
    
    #add bar chart
    fig_bar = px.bar(data_frame=df_plot, x='continent', y='life_exp', color='continent',
                     title=f'Life Expectancy by Continent in {selected_year}')
    st.plotly_chart(fig_bar, use_container_width=True)
    
    #add bar chart
    fig_bar = px.bar(data_frame=df_plot, x='continent', y='hdi_index', color='continent',
                     title=f'HDI Index by Continent in {selected_year}')
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    #add histogram
    fig_hist = px.histogram(data_frame=df_plot, x='gdp', color='continent',
                            title=f'GDP Distribution in {selected_year}')
    st.plotly_chart(fig_hist, use_container_width=True)
    
    #add histogram
    fig_hist = px.histogram(data_frame=df_plot, x='life_exp', color='continent',
                            title=f'Life Expectancy Distribution in {selected_year}')
    st.plotly_chart(fig_hist, use_container_width=True)
    
    #add histogram
    fig_hist = px.histogram(data_frame=df_plot, x='hdi_index', color='continent',
                            title=f'HDI Index Distribution in {selected_year}')
    st.plotly_chart(fig_hist, use_container_width=True)




