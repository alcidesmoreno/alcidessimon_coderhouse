import psycopg2

def load_data(data, conn):
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS earthquakes (
        id TEXT PRIMARY KEY,
        place TEXT,
        magnitude REAL,
        time BIGINT,
        longitude REAL,
        latitude REAL,
        depth REAL
    )
    ''')
    
    cursor.executemany('''
    INSERT INTO earthquakes (
        id, place, magnitude, time, longitude, latitude, depth
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', data)
    
    conn.commit()
    cursor.close()
