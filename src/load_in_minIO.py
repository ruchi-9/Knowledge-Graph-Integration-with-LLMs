from minio import Minio 
import json
import os
import constants

# Create a client with MinIOserver 
# add secure=False , because of ssl error
client =Minio(
    constants.MINIO_ENDPOINT,
    access_key=constants.MINIO_ACCESS_KEY,
    secret_key=constants.MINIO_SECRET_KEY,
    secure=False) 

# Use put_object if we need to directly load the file. put_object(upload from stream), fput_object( upload from file)
client.fput_object(
    constants.MINIO_BUCKET_NAME, 
    constants.MINIO_DESTINATION_FILE, 
    constants.SOURCE_FILE)

print(constants.SOURCE_FILE, "successfully uploaded as object", constants.MINIO_DESTINATION_FILE, "to bucket", constants.MINIO_BUCKET_NAME)