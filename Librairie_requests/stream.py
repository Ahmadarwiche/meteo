import streamlit as st
import pandas as pd
#import requests_exercice

weather_data = pd.read_csv('weather_data.csv')

# # Création d'un titre
st.title("Meteo France")

# Ajout d'une zone de texte
st.write("10 villes les plus grandes !")

cities = ['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Lille']


# création d'une liste déroulante pour sélectionner une ville
selected_city = st.selectbox('Sélectionnez une ville', cities)

# affichage des informations météorologiques pour la ville sélectionnée
st.write('Informations météorologiques pour', selected_city)
st.write(weather_data[weather_data['Ville'] == selected_city].iloc[0, 1:])

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Chargement des données de température pour chaque ville
df = weather_data
df.set_index('Ville', inplace=True)

# Coordonnées des villes
cities = {
    'Paris': [48.856614, 2.3522219],
    'Marseille': [43.296482, 5.369779],
    'Lyon': [45.764043, 4.835659],
    'Toulouse': [43.604652, 1.444209],
    'Nice': [43.7101728, 7.2619532],
    'Nantes': [47.2186371, -1.5541362],
    'Strasbourg': [48.584614, 7.7507127],
    'Montpellier': [43.610769, 3.876716],
    'Bordeaux': [44.837789, -0.57918],
    'Lille': [50.62925, 3.057256]
}

# Création de la carte avec folium
m = folium.Map(location=[46.227638, 2.213749], zoom_start=6)

# Ajout des marqueurs pour chaque ville
for city, coord in cities.items():
    temp = df.loc[city]['Température actuelle']
    ressenti = df.loc[city]['Température ressentie']
    temp_min = df.loc[city]['Température minimale']
    temp_max = df.loc[city]['Température maximale']
    pression = df.loc[city]['Pression atmosphérique']
    humidite = df.loc[city]['Humidité']
    vitesse_vent = df.loc[city]['Vitesse du vent']
    direction_vent = df.loc[city]['Direction du vent']
    lever_soleil = df.loc[city]['Lever du soleil']
    coucher_soleil = df.loc[city]['Coucher du soleil']
    popup = f"{city}<br>Température actuelle : {temp}°C<br>Température ressentie : {ressenti}°C<br>Température min : {temp_min}°C<br>Température max : {temp_max}°C<br>Pression atmosphérique : {pression} hPa<br>Humidité : {humidite}%<br>Vitesse du vent : {vitesse_vent} km/h<br>Direction du vent : {direction_vent}<br>Lever du soleil : {lever_soleil}<br>Coucher du soleil : {coucher_soleil}"
    folium.Marker(location=coord, popup=popup).add_to(m)

# Affichage de la carte avec Streamlit
folium_static(m)

# Affichage des informations de toutes les colonnes dans un tableau
#st.write(df)




