import streamlit as st
import pandas as pd

st.title("Movie Recommender")
st.write("IMDb Top 1000 Movies")

movies = pd.read_csv('imdb_top_1000.csv')
with st.expander("Click here to view the entire dataset", expanded=False):
    st.dataframe(movies)

# Select the number of movies you want to get recommended
number_of_movies = st.slider("Use the slider value to show only N movies you want to get recommended", 1, 1000)

# Show only the first N rows of the 'movies dataframe'
st.write("You selected "+ str(number_of_movies) + " movies to be displayed")
st.write(movies.head(number_of_movies))