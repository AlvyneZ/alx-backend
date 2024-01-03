#!/usr/bin/env python3
"""
1-fifo_cache.py - Provides one class:
    FIFOCache(BaseCaching)
"""


from re import A


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache implements a caching system of size MAX_ITEMS
     that removes the oldest inserted data
    """
    def __init__(self):
        """Initialize the age of data
        """
        self.data_count = 0
        self.first_key_index = 0
        self.keys = [""] * self.MAX_ITEMS
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key is None) or (item is None):
            return
        if self.cache_data.get(key, None) is None:
            if self.data_count >= self.MAX_ITEMS:
                print("DISCARD: {}".format(self.keys[self.first_key_index]))
                self.cache_data.pop(self.keys[self.first_key_index])
                self.keys[self.first_key_index] = key
            else:
                self.keys[self.data_count] = key
                self.data_count += 1
            self.first_key_index = (self.first_key_index + 1) % self.MAX_ITEMS
        self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
