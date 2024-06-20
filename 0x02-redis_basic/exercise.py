#!/usr/bin/env python3
"""
Define Module Writing strings to Redis
"""

import redis
import uuid
from typing import Union


class Cache():
    """ Define a class Cache """
    def __init__(self):
        """
        constructor - Initialize the Cache instance.
        Create an instance of the Redis client
        and flush the Redis database to clear any existing data.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store the input data in Redis with a randomly generated key. """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
