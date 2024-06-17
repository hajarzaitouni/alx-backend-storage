#!/usr/bin/env python3
""" Inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    and returns the new _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
