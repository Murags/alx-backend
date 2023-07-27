#!/usr/bin/env python3
"""class to add elements to the cache"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS and\
                    self.cache_data.get(key) is None:

                k, v = self.cache_data.popitem()
                print("DISCARD {}".format(k))
            self.cache_data[key] = item

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.cache_data.get(key)
