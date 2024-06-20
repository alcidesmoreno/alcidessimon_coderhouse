def transform_data(data):
    transformed_data = []
    for feature in data['features']:
        earthquake = (
            feature['id'],
            feature['properties']['place'],
            feature['properties']['mag'],
            feature['properties']['time'],
            feature['geometry']['coordinates'][0],  # Longitud
            feature['geometry']['coordinates'][1],  # Latitud
            feature['geometry']['coordinates'][2]   # Profundidad
        )
        transformed_data.append(earthquake)
    return transformed_data
