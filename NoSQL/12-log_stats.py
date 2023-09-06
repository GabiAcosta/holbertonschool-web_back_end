#!/usr/bin/env python3
"""
This script connects to a MongoDB database, analyzes Nginx logs,
and prints log statistics.
"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
logs_collection = client.logs.nginx
log = logs_collection.count_documents({})
get = logs_collection.count_documents({"method": "GET"})
post = logs_collection.count_documents({"method": "POST"})
put = logs_collection.count_documents({"method": "PUT"})
patch = logs_collection.count_documents({"method": "PATCH"})
delete = logs_collection.count_documents({"method": "DELETE"})
status = logs_collection.count_documents({"method": "GET", "path": "/status"})
print(f'{log} logs')
print("Methods:")
print(f'\tmethod GET: {get}')
print(f'\tmethod POST: {post}')
print(f'\tmethod PUT: {put}')
print(f'\tmethod PATCH: {patch}')
print(f'\tmethod DELETE: {delete}')
print(f'{status} status check')
