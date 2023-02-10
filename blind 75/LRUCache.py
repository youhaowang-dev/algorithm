# Hash Table, Linked List, Design, Doubly-Linked List
# Amazon 80 Bloomberg 25 Apple 18 Google 10 Microsoft 8 Facebook 7 DoorDash 6 Paypal 4 eBay 3 Oracle 3 Adobe 3
# TikTok 3 Zoom 3 Twilio 2 Yandex 2 Uber 2 Zillow 2 Intuit 2 Cloudera 2 Goldman Sachs 2 Twitch 2 ByteDance 2
# Cohesity 2 PayTM 2 Media.net 2
# https://leetcode.com/problems/lru-cache/description/

# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair
# to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); # cache is {1=1}
# lRUCache.put(2, 2); # cache is {1=1, 2=2}
# lRUCache.get(1);    # return 1
# lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    # returns -1 (not found)
# lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    # return -1 (not found)
# lRUCache.get(3);    # return 3
# lRUCache.get(4);    # return 4


# dict to save key to (key, val), (key, val) is connected by linked list
# dict size will be used for max size control
class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.key_to_node = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.remove_self(node)
        self.insert_at_head(node)

        return node.val

    def remove_self(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def put(self, key: int, val: int) -> None:
        if key not in self.key_to_node:
            node = Node(key, val)
            self.insert_at_head(node)
            self.key_to_node[key] = node
            if self.max_size < len(self.key_to_node):
                self.remove_last()
        else:
            node = self.key_to_node[key]
            node.val = val
            self.remove_self(node)
            self.insert_at_head(node)

    def remove_last(self):
        node = self.tail.prev
        self.remove_self(node)
        del self.key_to_node[node.key]


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
