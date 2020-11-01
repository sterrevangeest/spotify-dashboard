import pandas as pd
import random
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="*",
                                                           client_secret="*"))

with open('data/unique_ids.json') as f:
    df_ids = json.load(f)


with open('data/spotify.json') as f:
    track_info = json.load(f)

all_results = []

for index in range(len(df_ids)):
    results = sp.audio_features(tracks=df_ids[index])
    all_results.append(results)


with open('data/audio_features.json', 'w') as outfile:
    json.dump(all_results, outfile)
