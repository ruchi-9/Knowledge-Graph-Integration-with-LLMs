import requests
import os
import pandas as pd
from io import BytesIO
import constants

query_parameters = {"downloadformat": "csv"}
try:
   response = requests.get(constants.URL_FILE, params=query_parameters)
   if response.raise_for_status() == "200":
      df=pd.read_csv(BytesIO(response.content))
      if constants.STORE_FILE:
         df.to_csv("titanic.csv",index=False)
except:
   print("Kindly check file url.")


# Store the file in local with name titanic.csv
# with open("titanic.csv", mode="wb") as file:
#    file.write(response.content)
