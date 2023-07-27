#!/usr/bin/env python3
"""class to add elements to the cache"""
from typing import Any, Optional

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """

        if key and item:
            self.cache_data.update({key: item})
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_discard = list(self.cache_data.keys())[0]
                self.cache_data.pop(key_discard)
                print("DISCARD {}".format(key_discard))

    def get(self, key: Any) -> Optional[Any]:
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.cache_data.get(key)
