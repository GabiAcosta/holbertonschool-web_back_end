#!/usr/bin/env python3
"""
This script connects to a MongoDB database, analyzes Nginx logs,
and prints log statistics.
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    log = logs_collection.count_documents({})
    get = logs_collection.count_documents({"method": "GET"})
    post = logs_collection.count_documents({"method": "POST"})
    put = logs_collection.count_documents({"method": "PUT"})
    patch = logs_collection.count_documents({"method": "PATCH"})
    delete = logs_collection.count_documents({"method": "DELETE"})
    status = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f'{log} logs\nMethods:\n\tmethod GET: {get} \
        \n\tmethod POST: {post}\n\tmethod PUT: {put}\n\tmethod PATCH: {patch} \
        \n\tmethod DELETE: {delete}\n{status} status check')
