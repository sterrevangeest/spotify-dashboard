import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="142dc9c01d2940b6b1e9d6b599031354",
                                                           client_secret="079880f29265486daa9231bc63e959c2"))

results = sp.search(q='weezer', limit=20)
print(results)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
