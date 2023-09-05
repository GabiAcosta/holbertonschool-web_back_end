#!/usr/bin/env python3
"""
This module defines a function for retrieving schools with a specific topic
from a MongoDB collection.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve schools with a specific topic from a MongoDB collection.
    """
    docs = [doc for doc in mongo_collection.find({"topics": topic})]
    return docs
