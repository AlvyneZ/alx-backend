#!/usr/bin/env python3
"""
3-lru_cache.py - Provides one class:
    LRUCache(BaseCaching)
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache implements a caching system of size MAX_ITEMS
     that removes the least recently used (accessed/inserted)
     data
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
                print("DISCARD: {}".format(self.keys[0]))
                self.cache_data.pop(self.keys[0])
                self.keys.pop(0)
            self.keys.append(key)
        else:
            # Update edits to become the new last in
            self.keys.remove(key)
            self.keys.append(key)
        self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        data = self.cache_data.get(key, None)
        if data is not None:
            self.keys.remove(key)
            self.keys.append(key)
        return data


if __name__ == "__main__":
    my_cache = LRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
