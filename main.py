import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df=pd.read_csv('movies.csv')
# print(df.head())
# print(df.info())
# print(df.shape)
# print(df.isnull().sum())
select_features=['genres','keywords','tagline','cast','director']
for feature in select_features:
    df[feature]=df[feature].fillna('')
    
combined_features=df['genres']+' '+df['keywords']+' '+df['tagline']+' '+df['cast']+' '+df['director']

vectorizer=TfidfVectorizer()
feature_vectors=vectorizer.fit_transform(combined_features)
similarity=cosine_similarity(feature_vectors)

movie_name=input('enter you favourite movie name: ')
list_of_all_titles=df['title'].tolist()
close_match=difflib.get_close_matches(movie_name,list_of_all_titles)
close_match=close_match[0]
index_of_movie=df[df.title==close_match]['index'].values[0]
similarity_score=list(enumerate(similarity[index_of_movie]))
sorted_similar_movies=sorted(similarity_score,key=lambda x:x[1],reverse=True)
print('Top 5 similar movies to '+movie_name+' are:\n')
i=1
for movie in sorted_similar_movies:
    index=movie[0]
    title_from_index=df[df.index==index]['title'].values[0]
    if(i<5):
        print(title_from_index)
        i+=1
    
if  movie_name not in list_of_all_titles:
        print('Movie not found.')
