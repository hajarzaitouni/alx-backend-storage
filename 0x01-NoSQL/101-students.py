#!/usr/bin/env python3
"""
"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """

    Args:
        mongo_collection: 
    """
    
    return mongo_collection.aggregate([
        {"$project": {
                      "name": "$name",
                      "averageScore": {"$avg": "$topics.score"}
                      }
        },
        {"$sort": {
                   "averageScore": -1
                  }
        }
    ])
