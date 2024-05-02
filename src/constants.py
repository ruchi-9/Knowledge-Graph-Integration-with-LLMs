# PostgreSQL connection parameters
POSTGRESQL_HOST = "localhost"
POSTGRESQL_DBNAME = "postgres"
POSTGRESQL_USER = "postgres"
POSTGRESQL_PASSWORD = "postgres"
POSTGRESQL_PORT = "5432"

# Table name
TABLE_NAME = "Example3"

# MinIO connection parameters
MINIO_ENDPOINT = "127.0.0.1:9000"
MINIO_ACCESS_KEY = "reQTEdp5AMdAUdRBB3ih"
MINIO_SECRET_KEY = "bRinVoH1Tni6bpZ96OmIykC5PHGfus4z9OVBNp57"


# The file to upload, change this path if needed
SOURCE_FILE = "/home/ruchi/Desktop/DE_Project/titanic.csv"

# File location url
URL_FILE = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
STORE_FILE = True

# The destination bucket and filename on the MinIO server
MINIO_BUCKET_NAME = "csv-data"
MINIO_DESTINATION_FILE = "titanic1.csv"
MINIO_BUCKET_NAME_GRAPH = "graph-data"

#####################################3
MINIO_GRAPH_FILE = "generated_data.ttl"
