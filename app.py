import streamlit as st
import pandas as pd

st.title("Movie Recommender")
st.write("Here is the IMDB Top 1000 movies dataset:")

movies = pd.read_csv('imdb_top_1000.csv')
st.write(movies)

# Select the number of movies you want to get recommended
number_of_movies = st.slider("Use the slider value to show only N movies you want to get recommended", 1, 1000)

# Show only the first N rows of the 'movies dataframe'
st.write("You selected "+ str(number_of_movies) + " movies to be displayed")
st.write(movies.head(number_of_movies+1))