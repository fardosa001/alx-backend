#!/usr/bin/python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""

    def __init__(self):
        """"""
        super().__init__()

    def put(self, key, item):
        """Assign to the dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # If cache is full, remove the first item inserted
            discarded_key = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item

    def get(self, key):
        """returns linked value"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
