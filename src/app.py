import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Cargar las variables del .env
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Configurar la autenticación con Spotipy
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# ID del artista
artist_id = "5gznATMVO85ZcLTkE9ULU7"

# Obtener las 10 canciones más populares
top_tracks = sp.artist_top_tracks(artist_id)

# Lista para guardar los datos
tracks_data = []

# Recorrer los tracks y extraer la info
for track in top_tracks['tracks']:
    name = track['name']
    popularity = track['popularity']
    duration_ms = track['duration_ms']
    duration_min = round(duration_ms / 60000, 2)  # Convertir a minutos y redondear a 2 decimales

    tracks_data.append({
        'Nombre Canción': name,
        'Popularidad': popularity,
        'Duración (min)': duration_min
    })

# Crear DataFrame
df_tracks = pd.DataFrame(tracks_data)

print (df_tracks)