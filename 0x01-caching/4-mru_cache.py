#!/usr/bin/env python3
"""caching using MRU caching system"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A caching class using MRU system
    """
    def __init__(self):
        """
        lass initialization
        """
        super().__init__()

    def put(self, key, item):
        """
        this adds elements into the cache and removes the first
        item using MRU system
        """
        if not key or not item:
            return

        if len(self.cache_data) == BaseCaching.MAX_ITEMS and\
                self.cache_data.get(key) is None:

            key_to_remove = list(self.cache_data.keys())[-1]
            self.cache_data.pop(key_to_remove)
            print("DISCARD {}".format(key_to_remove))
        self.cache_data[key] = item

    def get(self, key):
        """
        retrieves elements from the cache based on the key given
        """
        value = self.cache_data.get(key)
        if value:
            self.cache_data.pop(key)
            self.cache_data[key] = value
        return value
