from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()

def get_db_params():
    return {
        'dbname': os.getenv('REDSHIFT_DBNAME'),
        'user': os.getenv('REDSHIFT_USERNAME'),
        'password': os.getenv('REDSHIFT_PASSWORD'),
        'host': os.getenv('REDSHIFT_HOST'),
        'port': os.getenv('REDSHIFT_PORT')
    }

def get_api_url():
    return 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'