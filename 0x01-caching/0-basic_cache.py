#!/usr/bin/env python3
"""class to add elements to the cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
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
            self.cache_data[key] = item

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.cache_data.get(key)
