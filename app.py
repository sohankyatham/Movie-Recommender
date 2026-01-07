import streamlit as st
import pandas as pd

st.title("IMDB Movie Recommender")

movies = pd.read_csv("imdb_top_1000.csv")

st.write("Dataset Preview")
st.dataframe(movies.head())

#streamlit run app.py
