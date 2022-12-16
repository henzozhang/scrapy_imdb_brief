import streamlit as st

st.title("brief scrapy")

st.subheader("top film 250")

st.subheader('Quel est le film le plus long ?' )

import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client["detail_film"]
collection =db["imbd_tb"]
cursor = collection.find({},{'Titre original':1,'Duree':1,'_id':0}).sort("Duree", -1).limit(1)
for film in cursor:
    # titre = 
    st.text(f"le film le plus est le film '{film['Titre original']}' avec {film['Duree']} minutes")
    
st.subheader('Quels sont les 5 films les mieux notés' )

client = MongoClient('localhost', 27017)
db = client["detail_film"]
collection =db["imbd_tb"]
cursor = collection.find({},{'Titre original':1,'Score sur 10':1,'_id':0}).sort("Score sur 10", -1).limit(5)
for film in cursor:
    st.text(f"le film '{film['Titre original']}' avec un score de {film['Score sur 10']} sur 10")
    
st.subheader('Dans combien de films a joué Morgan Freeman ? Tom Cruise ?' )

count = collection.count_documents({"Acteurs": {"$in": ["Tom Cruise"]}})

st.text(f"Dans {count} film a joué Tom Cruise ")

count = collection.count_documents({"Acteurs": {"$in": ["Morgan Freeman"]}})
st.text(f"Dans {count} films a joué Morgan Freeman ")
st.subheader('Quels sont les 3 meilleurs films d’horreur ? Dramatique ? Comique ?' )

pipeline = [
    {"$match":{"Genre":"Drama"}},
    {'$sort':{"Score sur 10": -1}},
    {'$limit': 3},
    {'$project':{'Titre original':1,'Score sur 10':1,'_id':0}}
]
result = collection.aggregate(pipeline)
st.text("les meilleurs films Dramatique sont:")
for film in result:
    st.text(f"le film '{film['Titre original']}' avec un score de {film['Score sur 10']} sur 10")

pipeline = [
    {"$match":{"Genre":"Comedy"}},
    {'$sort':{"Score sur 10": -1}},
    {'$limit': 3},
    {'$project':{'Titre original':1,'Score sur 10':1,'_id':0}}
]
result = collection.aggregate(pipeline)
st.text("les meilleurs films de comique sont:")
for film in result:
    st.text(f"le film '{film['Titre original']}' avec un score de {film['Score sur 10']} sur 10")

pipeline = [
    {"$match":{"Genre":"Horror"}},
    {'$sort':{"Score sur 10": -1}},
    {'$limit': 3},
    {'$project':{'Titre original':1,'Score sur 10':1,'_id':0}}
]
result = collection.aggregate(pipeline)
st.text("les meilleurs films d'horreur sont:")
for film in result:
    st.text(f"le film '{film['Titre original']}' avec un score de {film['Score sur 10']} sur 10")

st.subheader('Parmi les 100 films les mieux notés, quel pourcentage sont américains ? Français ?' )

pipeline = [
    {'$sort':{"Score sur 10": -1}},
    {'$limit': 100},
    {'$match': {'Pays d’origine': {'$in': ['France', 'United States']}}},
    {'$group': {
        '_id': '$Pays d’origine',
        'num_movies': {'$sum': 1}}}
    
]
results = collection.aggregate(pipeline)
for result in results:
    st.text(f"Les film d'origine {result['_id']} representent {result['num_movies']} % des 100 meilleurs films.")

st.subheader('Quel est la durée moyenne d’un film en fonction du genre ?' )
pipeline = [
    
    {'$group': {
        '_id': '$Genre',
        'average_duration': {'$avg': '$Duree'}
    }}
]
results = collection.aggregate(pipeline)
for result in results:
    st.text(f"Le genre {result['_id']} a une durée moyenne de {result['average_duration']} minutes.")
