import requests
import boto3
import uuid
import time
import random
import json
from datetime import datetime

client = boto3.client('kinesis', region_name='us-east-2')
partition_key = str(uuid.uuid4())
start = datetime.now()

while True:
    r = requests.get('https://randomuser.me/api/?exc=login')
    r = r.json()
    data = json.dumps(r)
    age = r['results'][0]['dob']['age']

    if age >= 21:
        # first = data['results'][0]['name']['first']
        # last = data['results'][0]['name']['last']
        # gender = data['results'][0]['gender']
        # lat = data['results'][0]['location']['coordinates']['latitude']
        # lon = data['results'][0]['location']['coordinates']['longitude']

        # record = {
        #     "FIRST": str(first),
        #     "LAST": str(last),
        #     "AGE": str(age),
        #     "GENDER": str(gender),
        #     "LATITUDE": str(lat),
        #     "LONGITUDE": str(lon)
        # }
        
        # record = json.dumps(record)
        # record = json.loads(record)

        client.put_record(StreamName='random-user-stream', Data=data, PartitionKey=partition_key)
    
    elapsed = datetime.now() - start
    if elapsed.seconds % 60 == 0:
        print(f'{elapsed.seconds // 60} Minutes elapsed | {elapsed.seconds} Seconds')

    time.sleep(random.uniform(0, 1))



