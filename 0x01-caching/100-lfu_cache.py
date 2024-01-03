#!/usr/bin/env python3
"""
100-lfu_cache.py - Provides one class:
    LFUCache(BaseCaching)
"""


from typing import Dict, List, Any
BaseCaching = __import__('base_caching').BaseCaching


class Freq():
    """
    Freq implements an object for tracking frequencies and
     indices of cached items
    """
    def __init__(self, key: Any):
        self.frq = 0
        self.key = key


class LFUCache(BaseCaching):
    """
    LFUCache implements a caching system of size MAX_ITEMS
     that removes the least frequently used (accessed/edited)
     data
    """
    def __init__(self):
        """Initialize the age of data
        """
        self.freqs: List[Freq] = []
        self.freq_idx: Dict[Any, int] = {}
        super().__init__()

    def __inc_freq(self, key):
        """ Increments the frequency after an access
        """
        idx = self.freq_idx.get(key, None)
        if idx is None:
            return
        self.freqs[idx].frq += 1
        if idx > 0:
            insert_freq: Freq = self.freqs.pop(idx)
            for i in reversed(range(0, idx)):
                if self.freqs[i].frq > insert_freq.frq:
                    self.freqs.insert((i + 1), insert_freq)
                    self.freq_idx[key] = i + 1
                    return
                self.freq_idx[self.freqs[i].key] += 1
            self.freqs.insert(0, insert_freq)
            self.freq_idx[key] = 0

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key is None) or (item is None):
            return
        if self.cache_data.get(key, None) is None:
            if len(self.freqs) >= self.MAX_ITEMS:
                lfu_key = self.freqs[self.MAX_ITEMS - 1].key
                print("DISCARD: {}".format(lfu_key))
                self.cache_data.pop(lfu_key)
                self.freq_idx.pop(lfu_key)
                self.freqs[self.MAX_ITEMS - 1] = Freq(key)
                self.freq_idx.update({key: (self.MAX_ITEMS - 1)})
                self.__inc_freq(key)
            else:
                self.freqs.insert(0, Freq(key))
                if len(self.freqs) >= self.MAX_ITEMS:
                    for i in range(len(self.freqs)):
                        self.freq_idx.update({self.freqs[i].key: i})
        else:
            self.__inc_freq(key)
        self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        data = self.cache_data.get(key, None)
        if data is not None:
            self.__inc_freq(key)
        return data


if __name__ == "__main__":
    my_cache = LFUCache()
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
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
