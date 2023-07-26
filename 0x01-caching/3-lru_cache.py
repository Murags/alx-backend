#!/usr/bin/env python3
"""class to add elements to the cache"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """_summary_
        """
        super().__init__()

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS and\
                    self.cache_data.get(key) is None:

                key_to_remove = list(self.cache_data.keys())[0]
                self.cache_data.pop(key_to_remove)
                print("DISCARD {}".format(key_to_remove))
            self.cache_data[key] = item

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        value = self.cache_data.get(key)
        if value:
            self.cache_data.pop(key)
            self.cache_data[key] = value
        return value
