import pandas as pd

def transform_data(data):
    # Crear un DataFrame a partir de los datos
    df = pd.json_normalize(data['features'])
    
    # Seleccionar y renombrar columnas relevantes
    df = df[['id', 'properties.place', 'properties.mag', 'properties.time',
             'geometry.coordinates']]
    df.columns = ['id', 'place', 'magnitude', 'time', 'coordinates']
    
    # Expandir las coordenadas en columnas separadas
    df[['longitude', 'latitude', 'depth']] = pd.DataFrame(df['coordinates'].tolist(), index=df.index)
    df = df.drop(columns=['coordinates'])
    
    # Convertir DataFrame en una lista de tuplas
    transformed_data = df.to_records(index=False).tolist()
    return transformed_data