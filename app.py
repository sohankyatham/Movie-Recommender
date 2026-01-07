import streamlit as st
import pandas as pd

st.title("Movie Recommender")

movies = pd.read_csv("imdb_top_1000.csv")

num_recs = st.slider("Number of recommendations", 1, 1000)

st.write("Dataset Preview")
st.dataframe(movies.head())