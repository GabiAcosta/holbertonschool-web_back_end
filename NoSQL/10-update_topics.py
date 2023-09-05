#!/usr/bin/env python3
"""
This module defines a function for updating the topics field of a school
document in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics field of a school document in a MongoDB collection.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
