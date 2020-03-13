# https://cc3cc9f39374448598659dd32a18e153.us-east-1.aws.found.io:9243
from pprint import pprint

import elasticsearch
import json

es = elasticsearch.Elasticsearch(['https://cc3cc9f39374448598659dd32a18e153.us-east-1.aws.found.io:9243'],
                                 http_auth=("elastic", "cB6zelqHAMrXzGOlLP1NuxJT"), scheme="https", port=9243,
                                 verify_certs=True)

# print(es.cat.health())
# print(es.cat.indices())

# with open("Sample Json File with 500 Records.json", encoding='utf-8') as json_file:
#     json_docs = json.loads(json_file.read())
# print(type(json_docs["feeds"][0]))
# for i, feed in enumerate(json_docs["feeds"]):
#     es.index(index="testing_sample_1", body=json.dumps(feed), id=i+1)

with open("generated.json") as json_file:
    json_docs = json.loads(json_file.read())
for i, feed in enumerate(json_docs):
    es.index(index="fake_data", body=json.dumps(feed), id=i+1)