# This code...
# scrapes the Spotify Charts website,
# gets the necessary data from the Top 200 list (songs, artists, listen counts, and ranks in each country at each date), and
# creates a separate data file for each country for which the data is available.


import pandas as pd
import os
import requests
from bs4 import BeautifulSoup as bs
from datetime import timedelta, date

# It generates a list of dates between Jan 1, 2017 and today
# in YYYY-MM-DD format


def daterange(start_date, end_date):
    for n in range(0, int((end_date - start_date).days) + 1, 7):
        yield start_date + timedelta(n)

# It creates the list of page links we will get the data from.


def create_links(country):
    start_date = date(2019, 1, 4)
    end_date = date(2019, 2, 7)
    links = []
    dates = daterange(start_date, end_date)
    for single_date in daterange(start_date, end_date):
        week_end = single_date + timedelta(days=7)
        links.append('https://spotifycharts.com/regional/' +
                     "global" + '/weekly/' + single_date.strftime("%Y-%m-%d") + "--" + week_end.strftime("%Y-%m-%d"))
    print(links)
    return(links, dates)


# It reads the webpage.
def get_webpage(link):
    page = requests.get(link)
    soup = bs(page.content, 'html.parser')
    return(soup)

# It collects the data for each country, and write them in a list.
# The entries are (in order): Song, Artist, Date, Play Count, Rank


def get_data(country):
    [links, dates] = create_links(country)
    rows = []

    for (link, date) in zip(links, dates):
        print(link)
        soup = get_webpage(link)
        images = soup.find_all("td", class_="chart-table-image")
        entries = soup.find_all("td", class_="chart-table-track")
        streams = soup.find_all("td", class_="chart-table-streams")

        for i, (entry, stream, image) in enumerate(zip(entries, streams, images)):
            song = entry.find('strong').get_text()
            artist = entry.find('span').get_text()[3:]
            play_count = stream.get_text()
            links = image.find_all("a", href=True)
            for a in links:
                url = a["href"]
            rows.append([song, artist, date, play_count, url, i+1])

    return (rows)

# It exports the data for each country in a csv format.
# The column names are Song, Artist, Date, Streams, Rank.


def save_data(country):
    if not os.path.exists('data'):
        os.makedirs('data')
    file_name = 'data/' + country[1].replace(" ", "_").lower() + '.csv'
    data = get_data(country[0])

    if(len(data) != 0):
        data = pd.DataFrame(
            data, columns=['Song', 'Artist', 'Date', 'Streams', 'Url', 'Rank'])
        data.to_csv(file_name, sep=',', float_format='%s', index=False)

# It generates a list of countries for which the data is provided.


def get_countries():
    page = requests.get('https://spotifycharts.com/regional')
    soup = bs(page.content, 'html.parser')
    countries = []
    ctys = soup.find('ul').findAll("li")
    for cty in ctys:
        countries.append([cty["data-value"], cty.get_text()])
    return(countries)

# It runs the function save_data for each country.
# In other words, it creates the .csv data files for each country.


def scrape_data():
    countries = get_countries()
    save_data(countries[0])


scrape_data()
