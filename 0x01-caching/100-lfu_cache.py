#!/usr/bin/env python3
"""LFU Caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Assign to dictionary"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If key exists, update the value and increase its frequency
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If cache is full, discard the least frequently used item(s)
                min_freq = min(self.frequency.values())
                least_frequent_keys = [k for k, v in
                                       self.frequency.items() if v == min_freq]
                if len(least_frequent_keys) > 1:
                    lru_key = min(self.cache_data,
                                  key=lambda k: self.frequency.get(k, 0))
                    print("DISCARD:", lru_key)
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                else:
                    lfu_key = least_frequent_keys[0]
                    print("DISCARD:", lfu_key)
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]

            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """return linked value to key"""
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency of the accessed key
        self.frequency[key] += 1

        return self.cache_data[key]
