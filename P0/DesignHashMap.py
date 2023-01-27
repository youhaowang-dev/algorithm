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
# 1). hash function design and 2). collision handling.

# TODO: use doubly linked list
class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class MyHashMap:
    DEFAULT_SIZE = 997  # prime number also for hashing

    def __init__(self):
        self.size = self.DEFAULT_SIZE
        self.buckets = [None for _ in range(self.size)]

    def put(self, key, value):
        hash = self.get_hash(key)
        if self.buckets[hash] == None:
            self.buckets[hash] = ListNode(key, value)
        else:
            cur = self.buckets[hash]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)  # update
                    return
                if cur.next == None:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key):
        node = self.get_node(key)
        if not node:
            return -1

        return node.pair[0]

    def remove(self, key):
        node = self.get_node(key)
        if not node:
            return

        hash = self.get_hash(key)
        cur = prev = self.buckets[hash]
        if not cur:
            return
        if cur.pair[0] == key:
            self.buckets[hash] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next

    def get_hash(self, key):
        return key % self.size

    def get_node(self, key):
        hash = self.get_hash(key)
        nodes = self.buckets[hash]
        if not nodes:
            return None

        for node in nodes:
            pair_key, _ = node.pair
            if pair_key == key:
                return node

        return None
