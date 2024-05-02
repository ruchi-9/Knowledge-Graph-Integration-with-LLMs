from minio import Minio 
import pandas as pd
from sqlalchemy import create_engine
import constants

# Postgres configuration 

postgres_uri="postgresql://postgres:postgres@localhost:5432/postgres" #postgres_uri='postgresql://username:password@localhost:5432/database_name',
# Create a client with MinIOserver
#  add secure=False , because of ssl error
"""
TO start the MinIO server use : MINIO_ROOT_USER=admin MINIO_ROOT_PASSWORD=password minio server /home/ruchi/object_store --console-address ":9001"
"""
minIO_client =Minio(constants.MINIO_ENDPOINT,access_key=constants.MINIO_ACCESS_KEY,secret_key=constants.MINIO_SECRET_KEY,secure=False) 
obj = minIO_client.get_object(constants.MINIO_BUCKET_NAME, "titanic.csv") #constants.MINIO_DESTINATION_FILE
df = pd.read_csv(obj)
engine = create_engine(postgres_uri)
df.to_sql(constants.TABLE_NAME, engine, if_exists='append', index=False)

"""
dbname="postgres"
user="postgres"
password="postgres"
host="localhost"
port="5432"
#csv_data = obj.data.decode('utf-8')
#df = pd.read_csv(obj)
#df = pd.read_csv(BytesIO(csv_data)) 
#print(df.head())
# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port  
)"""

