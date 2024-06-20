#!/usr/bin/env python3
"""
Define a Module for fetching and caching HTML content of a given URL
"""

import redis
import requests
from typing import Callable
import functools

r = redis.Redis()


def cache_result(method: Callable) -> Callable:
    """ Decorator to count accesses and cache the result for 10 seconds """

    @functools.wraps(method)
    def wrapper(url: str, *args, **kwargs) -> str:
        # Increment the count for a given URL
        r.incr(f"count:{url}")

        # Try to fetch the cached result
        cache_key = f"cache:{url}"
        cached_result = r.get(cache_key)
        if cached_result:
            return cached_result.decode("utf-8")

        # Fetch and cache the result if not found in cache
        result = method(url, *args, **kwargs)
        r.setex(cache_key, 10, result)
        return result

    return wrapper


@cache_result
def get_page(url: str) -> str:
    """ Fetch the HTML content of a given URL """
    return requests.get(url).text
