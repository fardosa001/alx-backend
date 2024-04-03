#!/usr/bin/python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """class LRUCache that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """assign to dictionary"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the order to reflect recent use
            self.order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # If cache is full, discard the least recently used item
            lru_key = self.order.pop(0)
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # Update the order to reflect recent use
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
