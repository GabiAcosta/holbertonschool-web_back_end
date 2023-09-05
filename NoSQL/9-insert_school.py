#!/usr/bin/env python3
"""
This module defines a function for inserting a school document into a
MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    nsert a school document into a MongoDB collection.
    """
    mongo_collection.insert_one(kwargs)
    return (kwargs.get('_id'))
