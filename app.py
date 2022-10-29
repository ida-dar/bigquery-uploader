from google.cloud import bigquery
import os
from dotenv import load_dotenv

load_dotenv('.env')
TABLE_PATH_CREDENTIALS = os.getenv('TABLE_PATH_CREDENTIALS')
TABLE_ID = os.getenv('TABLE_ID')

credentials_path = TABLE_PATH_CREDENTIALS
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = TABLE_ID

rows_to_insert = [
    {'title': 'Test', 'director': 'John Doe', 'year': '2000', 'awards': 5},
    {'title': 'Test1', 'director': 'Mary Jane', 'year': '2020', 'awards': 2},
]

errors = client.insert_rows_json(table_id, rows_to_insert)

if not errors:
    print('No errors, new rows have been inserted successfully')
else:
    print(errors)

