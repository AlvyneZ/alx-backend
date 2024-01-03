#!/usr/bin/env python3
"""
2-lifo_cache.py - Provides one class:
    LIFOCache(BaseCaching)
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache implements a caching system of size MAX_ITEMS
     that removes the oldest inserted data
    """
    def __init__(self):
        """Initialize the age of data
        """
        self.keys = []
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key is None) or (item is None):
            return
        if self.cache_data.get(key, None) is None:
            if len(self.keys) >= self.MAX_ITEMS:
                print("DISCARD: {}".format(self.keys[self.MAX_ITEMS - 1]))
                self.cache_data.pop(self.keys[self.MAX_ITEMS - 1])
                self.keys[self.MAX_ITEMS - 1] = key
            else:
                self.keys.append(key)
        else:
            # Update edits to become the new last in
            self.keys.remove(key)
            self.keys.append(key)
        self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    my_cache = LIFOCache()
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
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
