# Earthquake ETL Script

Este repositorio contiene un script ETL (Extract, Transform, Load) en Python que extrae datos de terremotos desde la API pública del US Geological Survey (USGS), transforma los datos y los carga en una base de datos Amazon Redshift.

## Descripción

El script `earthquake_etl_redshift.py` realiza las siguientes tareas:

1. **Extracción (Extract):** Realiza una solicitud GET a la API de USGS para obtener datos sobre los terremotos ocurridos en el último día en formato JSON.
2. **Transformación (Transform):** Transforma los datos JSON en una lista de tuplas que contienen los campos relevantes para cada terremoto.
3. **Carga (Load):** Conecta a una base de datos Redshift, crea una tabla (si no existe) y carga los datos transformados en la tabla.

## Requisitos

- Python 3.x
- Paquetes Python: `requests`, `psycopg2-binary`, `python-dotenv`
- Una base de datos Amazon Redshift

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/earthquake-etl.git
cd earthquake-etl
