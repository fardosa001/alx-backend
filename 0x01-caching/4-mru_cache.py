#!/usr/bin/python3
"""MRU caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class MRUCache that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign to dictionary"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the order to reflect recent use
            self.order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # If cache is full, discard the most recently used item
            mru_key = self.order.pop()
            print("DISCARD:", mru_key)
            del self.cache_data[mru_key]

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Return linked value"""
        if key is None or key not in self.cache_data:
            return None

        # Update the order to reflect recent use
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
