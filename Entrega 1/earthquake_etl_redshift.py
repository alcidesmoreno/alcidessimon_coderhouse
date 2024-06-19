import requests
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()

def extract_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def transform_data(data):
    transformed_data = []
    for feature in data['features']:
        earthquake = (
            feature['id'],
            feature['properties']['place'],
            feature['properties']['mag'],
            feature['properties']['time'],
            feature['geometry']['coordinates'][0],  # Longitude
            feature['geometry']['coordinates'][1],  # Latitude
            feature['geometry']['coordinates'][2]   # Depth
        )
        transformed_data.append(earthquake)
    return transformed_data

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

def main():
    load_env()
    api_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
    db_params = {
        'dbname': os.getenv('REDSHIFT_DBNAME'),
        'user': os.getenv('REDSHIFT_USERNAME'),
        'password': os.getenv('REDSHIFT_PASSWORD'),
        'host': os.getenv('REDSHIFT_HOST'),
        'port': os.getenv('REDSHIFT_PORT')
    }

    conn = psycopg2.connect(**db_params)
    
    try:
        # Extract
        print("Extracting data...")
        data = extract_data(api_url)
        
        # Transform
        print("Transforming data...")
        transformed_data = transform_data(data)
        
        # Load
        print("Loading data into database...")
        load_data(transformed_data, conn)
        
    except Exception as e:
        print(f"Error processing data: {e}")
    finally:
        conn.close()

    print("ETL process completed successfully.")

if __name__ == "__main__":
    main()

