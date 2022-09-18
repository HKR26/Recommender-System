import streamlit as st
import numpy as np
import pandas as pd
import pickle

animes_dict = pickle.load(open('animes_dict.pkl','rb'))
animes = pd.DataFrame(animes_dict)
@st.cache()
def recommend(anime):
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    index = animes[animes["Name"] == anime]["index"].values[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_anime_names = []
    recommended_anime_summery = []
    recommended_anime_tags = []
    for i in distances[1:6]:
        recommended_anime_names.append(animes.iloc[i[0]].Name)
        recommended_anime_summery.append(animes.iloc[i[0]].Synopsis)
        recommended_anime_tags.append(animes.iloc[i[0]].Tags)
    return recommended_anime_names ,recommended_anime_summery,recommended_anime_tags


st.title('Anime Recommender')
selected_anime = st.selectbox(
'Which anime did you like?',
(animes['Name'].values))

if st.button('Recommend'):
    with st.spinner(text='In progress'):
         recommendations,summery,tags = recommend(selected_anime)
         st.success('Done')
         for i in range(5):
             st.write(f"{i+1})"+"Title  :  "+str(recommendations[i]))
             st.write("Summery  : "+str(summery[i]))
             st.write("Tags :  "+str(tags[i]))