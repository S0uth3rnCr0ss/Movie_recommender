# import streamlit as st
# import pickle
# import pandas as pd
# import requests


# #def fetch_poster(movie_id):
#     # url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)
#     # headers = {
#     #     "accept": "application/json",
#     #     "Authorization":"Bearer cb56057c10be6dc4f4d2ac69f534c318"
#     # }
#     # response = requests.get(url,headers)
#     # #response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cb56057c10be6dc4f4d2ac69f534c318&language=en-US'.format(movie_id))
#     # data = response.json()
    
#     # return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movie_list = sorted(list(enumerate(distances)),reverse=True ,key = lambda x:x[1])[1:6]
    
#     recommended_movies = []
#     #recommend_movies_poster = []
#     for i in movie_list:
#         movie_id = 
       
#         recommended_movies.append(movies.iloc[i[0]].title)
#          #fetching poster
#         #recommend_movies_poster.append(fetch_poster(movie_id))
#     return recommended_movies
        



# movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# movies = pd.DataFrame(movies_dict)

# similarity = pickle.load(open('similarity.pkl','rb'))

# st.title('Movie Recommender System')

# selected_movie_name = st.selectbox(
#     'How would you like to interact with the movie recommender system?',
#     movies['title'].values
# )

# if st.button('Recommend'):
#     names,posters = recommend(selected_movie_name)
    
    
#     # col1,col2,col3, col4, col5 = st.columns(5)
#     # with col1:
#     #     st.header(names[0])
#     #     st.image(posters[0])
#     # with col2:
#     #     st.header(names[1])
#     #     st.image(posters[1])
#     # with col3:
#     #     st.header(names[2])
#     #     st.image(posters[2])
#     # with col4:
#     #     st.header(names[3])
#     #     st.image(posters[3])
#     # with col5:
#     #     st.header(names[4])
#     #     st.image(posters[4])   


import streamlit as st 
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    Response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cb56057c10be6dc4f4d2ac69f534c318&language=en-US'.format(movie_id))
    data = Response.json()
    
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True ,key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        
    return recommended_movies,recommended_movies_posters
    
    

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender')

selected_movie_name = st.selectbox(
    'please search for movies ',
    movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    
    col1,col2,col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])   
    