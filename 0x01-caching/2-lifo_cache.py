#!/usr/bin/python3
"""LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assign to dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # If cache is full, remove the last item inserted
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD:", last_key)
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """return linked value"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
