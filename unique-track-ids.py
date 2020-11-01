import json
import pandas as pd

df_2019 = pd.read_csv("data/2019global.csv")
df_2020 = pd.read_csv("data/2020global.csv")

all_tracks = pd.concat([df_2019["Track_Id"], df_2020["Track_Id"]])

unique_tracks = all_tracks.unique()
all_unique_tracks = []

# save unique tracks as a list
for track in unique_tracks:
    all_unique_tracks.append(track)

output = []
prev = 0
indexes = range(0, len(unique_tracks),  100)

for index in indexes:
    output.append(all_unique_tracks[prev: index])
    prev = index

output.append(all_unique_tracks[indexes[-1]:])

print(output)

with open('data/unique_ids.json', 'w') as outfile:
    json.dump(output, outfile)
