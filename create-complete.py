import json
import pandas as pd

df_2019 = pd.read_csv("data/2019global.csv")
df_2020 = pd.read_csv("data/2020global.csv")

df_complete = pd.concat([df_2019, df_2020])

with open('data/audio_features.json') as f:
    results = json.load(f)

del results[0]


for result in results:
    for track in result:
        print(track['valence'])
        print(track['id'])
        mask = df_complete["Track_Id"] == track['id']
        df_complete.loc[mask, "Valence"] = track['valence']
        df_complete.to_csv("data/data_complete.csv")
