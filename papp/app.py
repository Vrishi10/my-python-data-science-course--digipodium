import pandas as pd
import streamlit as st
import plotly.express as px

# page config
st.set_page_config(
    page_title='Pokemon App',
    page_icon='🦖',
    layout='wide'
    )

st.sidebar.title('🦖 🦕 🐉 Pokemon App')
st.image('papp/Pikachu.webp', use_column_width=True)

#load data
def load_pokemon():
    data = pd.read_csv('papp/Pokemon.csv', index_col=0)
    return data

with st.spinner('Loading Pokemon Data...'):
    pokemon = load_pokemon()
    st.sidebar.success("Loaded Pokemon Data")

#sidebar
show_data = st.sidebar.checkbox('Show the dataset')
if show_data:
    st.subheader('Pokemon Data')
    st.dataframe(pokemon, use_container_width=True)      #use area

#dropdown
#user chooses column type and we get the graph

type1 = st.sidebar.selectbox('Select Pokemon Type', pokemon['Type 1'].unique())

#group by
subset = pokemon[pokemon['Type 1'] == type1]          #filter

#to visualise the data
tabs = st.tabs(['Data','Univariate Analysis','Bivariate Analysis','Trivariate Analysis'])

#data tab
tabs[0].subheader(f'{type1} Pokemons')
tabs[0].dataframe(subset, use_container_width=True)

#Univariate Analysis Tab
# Attack
ss = subset.sort_values(by='Attack')
fig1 = px.histogram(subset, x='Attack', nbins=20)            #nbins -intervals in the histogram
fig2 = px.area(subset, y='Attack')
tabs[1].subheader(f'{type1} Stats')
tabs[1].subheader('Attack')
tabs[1].plotly_chart(fig1, use_container_width=True)
tabs[1].plotly_chart(fig2, use_container_width=True)

#defense 
ss = subset.sort_values(by='Defense') 
fig1 = px.histogram(subset, x='Defense', nbins=20)            #nbins -intervals in the histogram
fig2 = px.area(subset, y='Defense')  
tabs[1].subheader(f'{type1} Stats')
tabs[1].subheader('Defense')
tabs[1].plotly_chart(fig1)
tabs[1].plotly_chart(fig2)
 
#HP, Sp, Atk, Speed

#HP
ss = subset.sort_values(by='HP') 
fig1 = px.histogram(subset, x='HP', nbins=20)            
fig2 = px.area(subset, y='HP')  
tabs[1].subheader(f'{type1} Stats')
tabs[1].subheader('HP')
tabs[1].plotly_chart(fig1)
tabs[1].plotly_chart(fig2)

#Sp.Atk
ss = subset.sort_values(by='Sp. Atk') 
fig1 = px.histogram(subset, x='Sp. Atk', nbins=20)            
fig2 = px.area(subset, y='Sp. Atk')  
tabs[1].subheader(f'{type1} Stats')
tabs[1].subheader('Sp. Atk')
tabs[1].plotly_chart(fig1)
tabs[1].plotly_chart(fig2)

#Sp.Def
ss = subset.sort_values(by='Sp. Def') 
fig1 = px.histogram(subset, x='Sp. Def', nbins=20)            
fig2 = px.area(subset, y='Sp. Def')  
tabs[1].subheader(f'{type1} Stats')
tabs[1].subheader('Sp. Def')
tabs[1].plotly_chart(fig1)
tabs[1].plotly_chart(fig2)

#Speed
ss = subset.sort_values(by='Speed') 
fig1 = px.histogram(subset, x='Speed', nbins=20)            
fig2 = px.area(subset, y='Speed')  
tabs[1].subheader(f'{type1} Stats')
tabs[1].subheader('Speed')
tabs[1].plotly_chart(fig1)
tabs[1].plotly_chart(fig2)

#bivariate Analysis Tab
x = tabs[2].selectbox('Select X',pokemon.select_dtypes('number').columns)
y = tabs[2].selectbox('Select Y',pokemon.select_dtypes('number').columns)
c = tabs[2].selectbox('Select Color',pokemon.select_dtypes(exclude='number').columns)
fig = px.scatter(subset, x=x, y=y, color=c, hover_data=['Name'], size=x, size_max=60)
tabs[2].subheader(f'{type1} : {x} vs {y} by {c}')
tabs[2].plotly_chart(fig, use_container_width=True)

#Trivariate Analysis Tab
x = tabs[3].selectbox('Select X data',pokemon.select_dtypes('number').columns)
y = tabs[3].selectbox('Select Y data',pokemon.select_dtypes('number').columns)
z = tabs[3].selectbox('Select Z data',pokemon.select_dtypes('number').columns)
c = tabs[3].selectbox('Select Color type',pokemon.select_dtypes(exclude='number').columns)
fig = px.scatter_3d(subset, x=x, y=y, z=z, color=c, hover_data=['Name'], size=x, size_max=60)
tabs[3].subheader(f'{type1} : {x} vs {y} vs {z} by {c}')
tabs[3].plotly_chart(fig, use_container_width=True)
