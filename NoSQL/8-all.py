#!/usr/bin/env python3
"""
This module defines a function for retrieving all documents from a
MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from a MongoDB collection and return as a list.
    """
    docs = [doc for doc in mongo_collection.find({})]
    return docs
