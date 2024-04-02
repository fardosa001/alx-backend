#!/usr/bin/python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache that inherits from BaseCaching
    and is a caching system"""

    def put(self, key, item):
        """Assign to dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """returns linked value"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
