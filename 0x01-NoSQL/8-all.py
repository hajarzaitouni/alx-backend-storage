#!/usr/bin/env python3
""" Lists all documents in a collection """


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
        mongo_collection : The pymongo collection object.
    Return an empty list if no document in the collection
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
