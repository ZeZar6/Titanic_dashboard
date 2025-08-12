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

df_plot= df[df['Embarked'] == selected_port]
df_plot= df_plot[df_plot['Sex']==selected_gender]

plot= px.histogram(df_plot, x='Age', color='Survived', template='seaborn', title='Survival by Age', facet_col='Survived')

col1.plotly_chart(plot)


#add a pie chart
df_plot_pie= df_plot.loc[:, ['Survived', 'PassengerId']].groupby('Survived').count().reset_index()
df_plot_pie.rename({'PassengerId': 'Count'}, inplace=True, axis='columns')


#pie chart for survival or not survival of passengers
pie_plot= px.pie(df_plot_pie, names='Survived', values='Count', title='Survival Distribution')

col2.plotly_chart(pie_plot)


#add box plot
box_plot= px.box(df_plot, x='Survived', y='Fare', color='Survived', template='seaborn', title='Fare Distribution by Class and Survival', facet_col='Survived')

st.plotly_chart(box_plot)

