# https://cc3cc9f39374448598659dd32a18e153.us-east-1.aws.found.io:9243
from pprint import pprint

import elasticsearch
import json

es = elasticsearch.Elasticsearch(['https://cc3cc9f39374448598659dd32a18e153.us-east-1.aws.found.io:9243'],
                                 http_auth=("elastic", "cB6zelqHAMrXzGOlLP1NuxJT"), scheme="https", port=9243, verify_certs=True)

# print(es.cat.health())
# print(es.cat.indices())

with open("Sample Json File with 500 Records.json", encoding='utf-8') as json_file:
    json_docs = json.loads(json_file.read())
print(type(json_docs["feeds"][0]))
for feed in json_docs["feeds"]:
    str = {}
    pprint(feed)
    break
