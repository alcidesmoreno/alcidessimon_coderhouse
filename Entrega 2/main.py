import psycopg2
from config import load_env, get_db_params, get_api_url
from extract import extract_data
from transform import transform_data
from load import load_data
import pandas as pd

def main():
    load_env()
    api_url = get_api_url()
    db_params = get_db_params()

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