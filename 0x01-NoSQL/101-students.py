#!/usr/bin/env python3
"""
Create a function that
returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    List all students sorted by average score

    Args:
        mongo_collection: The pymongo collection object
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
