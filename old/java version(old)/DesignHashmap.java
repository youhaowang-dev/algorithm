// Array, Hash Table, Linked List, Design, Hash Function
// Amazon 5 Microsoft 4 Apple 4 LinkedIn 3 Goldman Sachs 3 VMware 3 Walmart Global Tech 3 Oracle 3 Shopee 3 Twitter 2 Salesforce 2 Facebook 2 Google 2 ServiceNow 4 Uber 3 Adobe 3 Bloomberg 3 ByteDance 2 2 Zynga
// https://leetcode.com/problems/design-hashmap/description/
// Design a HashMap without using any built-in hash table libraries.

// Implement the MyHashMap class:

// MyHashMap() initializes the object with an empty map.
// void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
// int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
// void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

// Example 1:

// Input
// ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
// [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
// Output
// [null, null, null, 1, -1, null, 1, null, -1]

// There are two main issues that we should tackle, in order to design an efficient hashmap data structure: 1). hash function design and 2). collision handling.
class MyHashMap {

  private int size = 911; // prime to reduce hashing conflict chance
  // LinkedList is for hashing conflict
  private ArrayList<LinkedList<Pair>> hashToPairs;

  // key value pair
  private class Pair {

    int key;
    int val;

    public Pair(int key, int val) {
      this.key = key;
      this.val = val;
    }
  }

  public MyHashMap() {
    this.hashToPairs = new ArrayList<LinkedList<Pair>>(this.size);
    for (int i = 0; i < this.size; i++) {
      this.hashToPairs.add(new LinkedList<Pair>());
    }
  }

  public void put(int key, int value) {
    Pair pair = this.getPair(key);
    if (pair != null) {
      pair.val = value;
    } else {
      this.getPairs(key).add(new Pair(key, value));
    }
  }

  private Pair getPair(int key) {
    LinkedList<Pair> pairs = this.getPairs(key);
    for (Pair pair : pairs) {
      if (pair.key == key) {
        return pair;
      }
    }

    return null;
  }

  private LinkedList<Pair> getPairs(int key) {
    int hashKey = this.getHashKey(key);
    return this.hashToPairs.get(hashKey);
  }

  public int get(int key) {
    Pair pair = this.getPair(key);
    if (pair != null) {
      return pair.val;
    }

    return -1;
  }

  public void remove(int key) {
    Pair pair = this.getPair(key);
    if (pair != null) {
      this.getPairs(key).remove(pair);
    }
    // java.util.ConcurrentModificationException
    // for (Pair pair : pairs) {
    //   if (pair.key == key) {
    //     pairs.remove(pair);
    //   }
    // }
  }

  private int getHashKey(int key) {
    return key % this.size;
  }
}
