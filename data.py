
import pandas as pd

# GET all data
df = pd.read_csv("data/data_complete-kopie.csv")

# Assign extra different date types to the data
df['Date'] = df['Date'].astype('datetime64[ns]')
df['Day'] = df["Date"].dt.strftime("%m-%d")
df["Week"] = df["Date"].dt.strftime("%V")
df["Year"] = df['Date'].dt.year
df['Month'] = pd.to_datetime(
    df['Date'], format='%m').dt.month_name()

# Round Valence
df["Valence"] = df["Valence"].round(3)


def get_data():
    return df
