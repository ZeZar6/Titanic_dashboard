import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(layout='wide')
st.title('Project 3: Data Visualization with Plotly')

df= pd.read_csv('clean_auto_mpg.csv')

unique_origin= list(df['origin'].unique())
unique_origin.sort()


unique_origin_str=['Origin ' + str(i) for i in unique_origin]

#create tabs
tab1, tab2, tab3 = st.tabs([unique_origin_str[0], unique_origin_str[1], unique_origin_str[2]])


with tab1:
    st.subheader('I am a tab for ' + unique_origin_str[0])
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    df_tab= df[df['origin'] == unique_origin[0]]
    average_mpg = round(df_tab['mpg'].mean(), 2)
    average_avgdisplacement = round(df_tab['displacement'].mean(), 2)
    average_horsepower = round(df_tab['horsepower'].mean(), 2)
    average_weight = round(df_tab['weight'].mean(), 2)
    col1.metric('Average MPG', average_mpg)
    col2.metric('Average Displacement', average_avgdisplacement)
    col3.metric('Average Horsepower', average_horsepower)
    col4.metric('Average Weight', average_weight)
    
    col1, col2= st.columns([3,1])
    fig = px.scatter(df_tab, x='weight', y='horsepower', color='cylinders',
                     title='Weight vs Horsepower ',
                     labels={'weight': 'Weight (lbs)', 'horsepower': 'Horsepower'})
    col1.plotly_chart(fig, use_container_width=True)
    
    fig2=px.histogram(df_tab, x='mpg', color='cylinders',
                title='MPG Distribution ',
                labels={'mpg': 'Miles Per Gallon (MPG)'})
    col2.plotly_chart(fig2, use_container_width=True)


with tab2:
    st.subheader('I am a tab for ' + unique_origin_str[1])
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    df_tab= df[df['origin'] == unique_origin[1]]
    average_mpg = round(df_tab['mpg'].mean(), 2)
    average_avgdisplacement = round(df_tab['displacement'].mean(), 2)
    average_horsepower = round(df_tab['horsepower'].mean(), 2)
    average_weight = round(df_tab['weight'].mean(), 2)
    col1.metric('Average MPG', average_mpg)
    col2.metric('Average Displacement', average_avgdisplacement)
    col3.metric('Average Horsepower', average_horsepower)
    col4.metric('Average Weight', average_weight)
    
    col1, col2= st.columns([3,1])
    fig = px.scatter(df_tab, x='weight', y='horsepower', color='cylinders',
                     title='Weight vs Horsepower',
                     labels={'weight': 'Weight (lbs)', 'horsepower': 'Horsepower'})
    col1.plotly_chart(fig, use_container_width=True)
    
    fig2=px.histogram(df_tab, x='mpg', color='cylinders',
                title='MPG Distribution ',
                labels={'mpg': 'Miles Per Gallon (MPG)'})
    col2.plotly_chart(fig2, use_container_width=True)


with tab3:
    st.subheader('I am a tab for ' + unique_origin_str[2])
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    df_tab= df[df['origin'] == unique_origin[2]]
    average_mpg = round(df_tab['mpg'].mean(), 2)
    average_avgdisplacement = round(df_tab['displacement'].mean(), 2)
    average_horsepower = round(df_tab['horsepower'].mean(), 2)
    average_weight = round(df_tab['weight'].mean(), 2)
    col1.metric('Average MPG', average_mpg)
    col2.metric('Average Displacement', average_avgdisplacement)
    col3.metric('Average Horsepower', average_horsepower)
    col4.metric('Average Weight', average_weight)
    
    col1, col2= st.columns([3,1])
    fig = px.scatter(df_tab, x='weight', y='horsepower', color='cylinders',
                     title='Weight vs Horsepower',
                     labels={'weight': 'Weight (lbs)', 'horsepower': 'Horsepower'})
    col1.plotly_chart(fig, use_container_width=True)
    
    fig2=px.histogram(df_tab, x='mpg', color='cylinders',
                title='MPG Distribution ',
                labels={'mpg': 'Miles Per Gallon (MPG)'})
    col2.plotly_chart(fig2, use_container_width=True)
    