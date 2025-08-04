import sqlite3

database_file = 'dbs/song_features.db'

def inspect_db_schema(db_file):
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            for table_names in tables:
                table_name = table_names[0]
                print(f"Table: {table_name}")
                
                cursor.execute(f"PRAGMA table_info({table_name});")
                schema_info = cursor.fetchall()
                
                for column in schema_info:
                    # id, name, type, notnull, default_value, pk
                    col_name = column[1]
                    col_type = column[2]
                    is_pk = " (Primary Key)" if column[5] == 1 else ""
                    print(f"  - {col_name} ({col_type}){is_pk}")
    except:
        print("Error inspecting the database.")

def song_feature_random_from_each_cluster(n):
    try:
        with sqlite3.connect("dbs/song_features.db") as conn:
            cursor = conn.cursor()
            for cluster in range(4):
                cursor.execute(
                        "SELECT track_uri, track_name, artist_name, cluster, role_annotation "
                        "FROM song_features WHERE cluster = ? ORDER BY RANDOM() LIMIT ?",
                        (cluster, n)
                    )
                for column in cursor.fetchall():
                    print(column)
    except Exception as e:
        print(f"Error printing from the database. Error: {e}")

connection = sqlite3.connect(database_file)
#inspect_db_schema(database_file)
song_feature_random_from_each_cluster(3)
