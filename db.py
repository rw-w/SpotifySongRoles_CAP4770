import sqlite3

database_file = 'playlists.db'

def inspect_db_schema(db_file):
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

connection = sqlite3.connect(database_file)
inspect_db_schema(database_file)