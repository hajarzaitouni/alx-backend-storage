#!/usr/bin/env python3
"""
Define Module Writing strings to Redis
"""

import redis
import uuid
from typing import Union, Optional, Callable


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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieves the data stored in Redis for the given key
        and apply an optional conversion function to the data.
        """
        stored_data = self._redis.get(key)
        if stored_data is None:
            return None
        if fn:
            return fn(stored_data)
        return stored_data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve the stored data for the given key and convert to string"""
        stored_data = self._redis.get(key)
        return stored_data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Retrieve the data stored in Redis and convert it to an integer """
        return self.get(key, lambda s_data: int(s_data))
