import streamlit as st
import pickle
import pandas as pd
import numpy as np

def recommend(movie):
    # Find the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    # Get the top 5 most similar movies
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    for i in movies_list:
        # Append only the title
        recommend_movies.append(movies.iloc[i[0]].title)
    
    return recommend_movies

# 1. Load data dataframes
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# 2. Load and combine the split similarity matrix chunks
part1 = pickle.load(open('similarity_part1.pkl', 'rb'))
part2 = pickle.load(open('similarity_part2.pkl', 'rb'))
similarity = np.concatenate((part1, part2), axis=0)

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie from the list', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for name in recommendations:
        st.write(name)