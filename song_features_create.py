import sqlite3
import pandas as pd

database_file = 'playlists.db'

def create_song_feature_db_from(db_file):
    try:
        query = """
                SELECT
                    t.track_uri,
                    t.track_name,
                    t.artist_name,
                    COUNT(pt.pid) AS in_number_of_playlists,
                    AVG(p.num_followers) AS avg_playlist_followers,
                    AVG(pt.pos + 1) AS avg_position_in_playlist
                FROM
                    playlist_track pt
                JOIN
                    playlists p ON pt.pid = p.pid
                JOIN
                    tracks t ON pt.track_uri = t.track_uri
                GROUP BY
                    t.track_uri, t.track_name, t.artist_name
                ORDER BY
                    in_number_of_playlists DESC;
                """
        with sqlite3.connect(db_file) as conn:
            song_features_df = pd.read_sql_query(query, conn)
        new_db = 'song_features.db'
        table_name = 'song_features'
        with sqlite3.connect(new_db) as conn_new:
            song_features_df.to_sql(table_name, conn_new, if_exists='replace', index=False)
            print(f"Song features database created successfully in {new_db} with table '{table_name}'.")
        print(song_features_df.head())
            
    except Exception as e:
        print(f"Error: {e}")
    
create_song_feature_db_from(database_file)
print("Song features database creation completed.")