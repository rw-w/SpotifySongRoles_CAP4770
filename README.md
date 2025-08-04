# SpotifySongRoles_CAP4770
# Synopsis:
The goal of this project is to develop a classification for songs based on how they are used in user-generated playlists. We will first cluster songs into various labels based on their popularity and reach metrics. Then, we will analyze the roles of each song via their position in playlists and associated genres/themes. We might find categories that can be described as 'niche,' 'rising,' 'curated,' 'mainstream,' or something in-between these. Finally, a predictive decision-tree model will be trained on these clusters to help classify future songs. This aims to solve the real-world problem of tracking a song's lifecycle and audience appeal without needing to analyze the actual content of the songs.
# Details:
- Dataset: Our project uses the Spotify Million Playlist Dataset, a collection of 1-million user-generated playlists in JSON format.

  - https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge
 
- Problem Statement: Create a classification for songs based on their functional roles within user-generated playlists.

Conventional measurements of a song's success, such as overall listener count and chart rankings, often fall short to capture important context, such as how a song is often used by listeners. This project aims to create a multidimensional song classification system that leverages the functional roles of songs within user-created playlists, uncovering a more nuanced understanding of a song's lifecycle and audience appeal.

# Instructions
- We've included every step of the project's pipelines into a single Jupyter Notebook, master_script.ipynb.
- After downloading the Spotify Million Playlist Dataset detailed earlier and extracting the files, locate the DATA_DIR variable in the second cell. Change the value to the path location to the SpotifyData folder that was extracted.
  - We suggest the directory to be setup as:
  
        /
    
        master_script.ipynb
    
        db_inspect.py
    
        SpotifyData/
    
            .json files
    
- Please review requirements.txt and perform 'pip install -r requirements.txt' if any packages are missing.
- From here, you are free to "Run All" or run each cell sequentially.
    - This will create, populate, and perform necessary modifications to playlists.db, song_features.db, and staple_scores.pkl that lead to the results from our project.
- Additionally, a db_inspect.py script is included that can perform two functions: 1. Identify the table structures in a .db file, 2. Randomly select and print information about N songs from each cluster (0, 1, 2, 3).
