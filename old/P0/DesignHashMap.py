# Array, Hash Table, Linked List, Design, Hash Function
# Amazon 5 Microsoft 4 Apple 4 LinkedIn 3 Goldman Sachs 3 VMware 3 Walmart Global Tech 3 Oracle 3 Shopee 3 Twitter 2 Salesforce 2 Facebook 2 Google 2 ServiceNow 4 Uber 3 Adobe 3 Bloomberg 3 ByteDance 2 2 Zynga
# https://leetcode.com/problems/design-hashmap/description/
# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/hash_table/hash_map.ipynb
# For simplicity, are the keys integers only? Yes
# For collision resolution, can we use chaining? Yes
# Do we have to worry about load factors? No
# Can we assume inputs are valid or do we have to validate them? Yes, Assume they're valid
# Can we assume this fits memory? Yes
class Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class MyHashMap:
    def __init__(self, size=997):
        self.size = size
        self.buckets = [list() for _ in range(size)]

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self._hash(key)]
        for item in bucket:
            if item.key == key:
                item.val = value
                return

        bucket.append(Item(key, value))

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]
        for item in bucket:
            if item.key == key:
                return item.val

        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        for i, item in enumerate(bucket):
            if item.key == key:
                bucket.pop(i)
                return

    def _hash(self, key):
        return key % self.size
