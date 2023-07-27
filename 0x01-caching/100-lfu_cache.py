#!/usr/bin/env python3
"""
LFU caching module
"""
from base_caching import BaseCaching
from typing import Any, Optional


class LFUCache(BaseCaching):
    """ LFU cache class
    """
    def __init__(self):
        """ Initializes a new instance
        """
        super().__init__()
        self.usage_counter = {}

    def put(self, key: Any, item: Any) -> None:
        """ Adds data to the cache based on LFU policy
            - Args:
                - key: new entry's key
                - item: entry's value
        """
        if not key or not item:
            return

        # Check if the cache is full and if the key is new
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.cache_data:
            least_used_key = min(self.usage_counter, key=self.usage_counter.get)
            self.cache_data.pop(least_used_key)
            self.usage_counter.pop(least_used_key)
            print(f'DISCARD: {least_used_key}')

        # Update the cache with the new item and update usage counter
        self.cache_data[key] = item
        self.usage_counter[key] = self.usage_counter.get(key, 0) + 1

    def get(self, key: Any) -> Optional[Any]:
        """ Gets cache data associated with the given key
            and updates dict in accordance with the LFU policy
            - Args:
                - key to look for
            - Return:
                - value associated with the key
        """
        cache_item = self.cache_data.get(key)
        if cache_item:
            # Update usage counter and sort it based on usage frequency
            self.usage_counter[key] = self.usage_counter.get(key) + 1
            self.usage_counter = dict(sorted(self.usage_counter.items(), key=lambda x: (x[1], x[0])))
        return cache_item
