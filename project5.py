import pandas as pd
import plotly.express as px
import streamlit as st



st.set_page_config(
    layout='wide',)
df= pd.read_csv("share-of-individuals-using-the-internet.csv")
df= df[(df['Year'] >=2000) & (df['Year'] <= 2016)]
print(df.columns)
print(df.info())



years= df['Year'].unique()
years.sort()
country = df['Country'].unique(
)
selected_year= st.selectbox(label='Year', options=years)

selected_country= st.selectbox(label='Country', options=country)

df_plot= df[df['Year'] == selected_year]

st.header('Internet Usage DashBoard')
col1, col2= st.columns([1,1])

plot= px.choropleth(data_frame=df_plot, locations='Country', locationmode='country names', color='Individuals using the Internet (% of population)', hover_name='Country',  title='Visual showing internet usage percentage across countries', color_continuous_scale=px.colors.qualitative.Vivid)

plot2= px.histogram(data_frame=df_plot, x='Individuals using the Internet (% of population)', title='Histogram showing internet usage percentage across countries', color='Country',)


with col1:
    st.plotly_chart(plot)

with col2:
    st.plotly_chart(plot2)


#add a sidebar
st.sidebar.subheader('Country level detail')


#add a form
form= st.sidebar.form('form')
selected_country=form.selectbox(label='Select Country', options=country, index=0)
submit=form.form_submit_button('Submit')


st.subheader('Country level detail for {}'.format(selected_country))

if submit:
    df_by_country=df[df['Country'] == selected_country]
    plot= px.line(data_frame=df_by_country, x='Year', y='Individuals using the Internet (% of population)', title='Internet Usage Over Time for {}'.format(selected_country))
    st.plotly_chart(plot)


