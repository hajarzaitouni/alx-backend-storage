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
    def wrapper(url: str) -> str:
        # Increment the count for a given URL
        r.incr(f"count:{url}")

        cached_data = r.get(f"cached:{url}")
        if cached_data:
            return cached_data.decode("utf-8")
        response = method(url)
        r.set(f"count:{url}", 0)
        r.setex(f"cached:{url}", 10, response)
        return response

    return wrapper


@cache_result
def get_page(url: str) -> str:
    """ Fetch the HTML content of a given URL """
    return requests.get(url).text
