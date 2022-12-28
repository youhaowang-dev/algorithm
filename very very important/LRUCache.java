// Hash Table, Linked List, Design, Doubly-Linked List
// Amazon 80 Bloomberg 25 Apple 18 Google 10 Microsoft 8 Facebook 7 DoorDash 6 Paypal 4 eBay 3 Oracle 3 Adobe 3 TikTok 3 Zoom 3 Twilio 2 Yandex 2 Uber 2 Zillow 2 Intuit 2 Cloudera 2 Goldman Sachs 2 Twitch 2 ByteDance 2 Cohesity 2 PayTM 2 Media.net 2
// https://leetcode.com/problems/lru-cache/description/

// Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

// Implement the LRUCache class:

// LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
// int get(int key) Return the value of the key if the key exists, otherwise return -1.
// void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
// The functions get and put must each run in O(1) average time complexity.

// Example 1:

// Input
// ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
// [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
// Output
// [null, null, null, 1, null, -1, null, -1, 3, 4]

// Explanation
// LRUCache lRUCache = new LRUCache(2);
// lRUCache.put(1, 1); // cache is {1=1}
// lRUCache.put(2, 2); // cache is {1=1, 2=2}
// lRUCache.get(1);    // return 1
// lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
// lRUCache.get(2);    // returns -1 (not found)
// lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
// lRUCache.get(1);    // return -1 (not found)
// lRUCache.get(3);    // return 3
// lRUCache.get(4);    // return 4
class LRUCache {

  private int capacity;
  private HashMap<Integer, Node> keyToNode;
  // head is the least recent, tail is the most recent
  private Node beforeHead;
  private Node afterTail;

  public LRUCache(int capacity) {
    this.capacity = capacity;
    this.keyToNode = new HashMap<Integer, Node>();
    this.beforeHead = new Node(Integer.MAX_VALUE, Integer.MAX_VALUE);
    this.afterTail = new Node(Integer.MAX_VALUE, Integer.MAX_VALUE);
    this.beforeHead.next = this.afterTail;
    this.afterTail.prev = this.beforeHead;
  }

  public int get(int key) {
    if (!this.keyToNode.containsKey(key)) {
      return -1;
    }

    Node node = this.keyToNode.get(key);

    // detach
    // node.prev.next = node.next;
    // node.next.prev = node.prev;
    Node prev = node.prev;
    Node next = node.next;
    prev.next = next;
    next.prev = prev;
    // move to end
    this.moveToEnd(node);

    return node.value;
  }

  public void put(int key, int value) {
    // use get to move key to tail
    if (this.get(key) != -1) {
      this.keyToNode.get(key).value = value;
      return;
    }

    if (this.capacity == keyToNode.size()) {
      // this.keyToNode.remove(this.beforeHead.next.key);
      // this.beforeHead.next = this.beforeHead.next.next;
      // this.beforeHead.next.prev = this.beforeHead;

      Node head = this.beforeHead.next;
      Node prev = head.prev;
      Node next = head.next;
      prev.next = next;
      next.prev = prev;

      this.keyToNode.remove(head.key);
    }
    Node newNode = new Node(key, value);
    this.keyToNode.put(key, newNode);
    this.moveToEnd(newNode);
  }

  private void moveToEnd(Node node) {
    //   node.prev = this.afterTail.prev;
    //   this.afterTail.prev = node;
    //   node.prev.next = node;
    //   node.next = this.afterTail;
    Node currentTail = this.afterTail.prev;
    currentTail.next = node;
    node.prev = currentTail;
    node.next = this.afterTail;
    this.afterTail.prev = node;
  }

  private class Node {

    int key;
    int value;
    Node prev;
    Node next;

    public Node(int key, int value) {
      this.key = key;
      this.value = value;
      Node prev = null;
      Node next = null;
    }
  }
}
