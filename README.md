🎓 **Fundamentals of Data Science**

# Spotify Mood Dashboard

In this dashboard I want to let users discover what effects the time of year and different events (such as COVID-19) have on our mood by showing which music we listen to the most during that period.

### Background

Spotify has an algorithm that classifies a song’s **“valence”**, or how happy it sounds, on a scale from 0 to 100. The algorithm is trained on ratings of positivity by musical experts, and gives Aretha Franklin’s soaring “Respect” a score of 97; Radiohead’s gloomy “Creep” gets just 10 (The Economist, 2020).

Since 2017 Spotify has also published daily and weekly tables of the 200 most-streamed songs, both worldwide and in each country on [Spotify Charts](https://spotifycharts.com/regional).

### Data Sources

**Scraping Spotify Charts**

I use the Spotify Charts website to find out which songs most people are listening to in recent years. I have to scrape the website for this. This has been done before by another developer. With some minor tweaks, I can use this code.
With a few minor changes to the code I can get the data I need from this website.

The following information is retrieved from the website:

| Song                                          | Artist                | Date       | Streams    | Url                                                   | Rank |
| --------------------------------------------- | --------------------- | ---------- | ---------- | ----------------------------------------------------- | ---- |
| Sunflower - Spider-Man: Into the Spider-Verse | Post Malone, Swae Lee | 2019-01-04 | 32,548,077 | https://open.spotify.com/track/3KkXRkHbMCARz0aVfEt68P | 1    |
| thank u, next                                 | Ariana Grande         | 2019-01-04 | 29,904,412 | https://open.spotify.com/track/2rPE9A1vEgShuZxxzR2tZH | 2    |

and is saved to a csv file.

**Spotify Api**

With the URL I can retrieve the valence of the songs.

### Design

### Skills/knowledge

### Obstacles

### References

The Economist. (2020, February 6). Data from Spotify suggest that listeners are gloomiest in February. https://www.economist.com/graphic-detail/2020/02/08/data-from-spotify-suggest-that-listeners-are-gloomiest-in-february
