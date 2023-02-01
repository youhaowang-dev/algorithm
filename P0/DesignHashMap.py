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

# There are two main issues that we should tackle, in order to design an efficient hashmap data structure:
# 1). hash function design and 2). collision/conflict handling.
class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class MyHashMap:
    DEFAULT_SIZE = 997  # prime number also for hashing

    def __init__(self):
        self.size = self.DEFAULT_SIZE
        self.hash_to_head = [None for _ in range(self.size)]

    def put(self, key, val):
        hash = self.get_hash(key)
        if not self.hash_to_head[hash]:
            self.hash_to_head[hash] = ListNode(key, val)
        else:
            node = self.hash_to_head[hash]
            while node.next:  # may need the tail to append
                # try update node
                if self.try_update(node, key, val):
                    return
                node = node.next
            # try update tail
            if self.try_update(node, key, val):
                return
            # not found, append
            node.next = ListNode(key, val)

    def try_update(self, node: ListNode, key: int, val: int) -> bool:
        if node.pair[0] == key:  # found, so update and return
            node.pair = (key, val)
            return True

        return False

    def get(self, key):
        hash = self.get_hash(key)
        node = self.hash_to_head[hash]
        while node:
            if node.pair[0] == key:
                return node.pair[1]
            else:
                node = node.next
        return -1

    def remove(self, key):
        hash = self.get_hash(key)
        node = self.hash_to_head[hash]
        if not node:
            return
        if node.pair[0] == key:  # first node is the target
            self.hash_to_head[hash] = node.next
        else:  # two pointers same speed
            prev = node
            node = node.next
            while node:
                if node.pair[0] == key:
                    prev.next = node.next  # remove
                    return
                else:
                    node = node.next
                    prev = prev.next

    def get_hash(self, key):
        return key % self.size
