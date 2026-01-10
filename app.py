import streamlit as st
import pandas as pd

st.title("Movie Recommender")
st.write("Here is the IMDB Top 1000 movies dataset:")

movies = pd.read_csv('imdb_top_1000.csv')
st.write(movies)