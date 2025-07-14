# SpotifySongRoles_CAP4770
# Synopsis:
The goal of this project is to develop a classification for songs based on how they are used in user-generated playlists. We will first cluster songs into various labels based on their popularity and reach metrics. Then, we will analyze the roles of each song via their position in playlists and associated genres/themes. We might find categories that can be described as 'niche,' 'rising,' 'curated,' 'mainstream,' or something in-between these. Finally, a predictive decision-tree model will be trained on these clusters to help classify future songs. This aims to solve the real-world problem of tracking a song's lifecycle and audience appeal without needing to analyze the actual content of the songs.
# Details:
- Dataset: Our project uses the Spotify Million Playlist Dataset, a collection of 1-million user-generated playlists in JSON format.

  - https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge
 
- Problem Statement: Create a classification for songs based on their functional roles within user-generated playlists.

Conventional measurements of a song's success, such as overall listener count and chart rankings, often fall short to capture important context, such as how a song is often used by listeners. This project aims to create a multidimensional song classification system that leverages the functional roles of songs within user-created playlists, uncovering a more nuanced understanding of a song's lifecycle and audience appeal.
