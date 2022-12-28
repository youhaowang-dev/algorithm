// https://www.lintcode.com/problem/129/

// The size of the hash table is not determinate at the very beginning.
// If the total size of keys is too large (e.g. size >= capacity / 10), we should
// double the size of the hash table and rehash every keys. Say you have a hash table looks like below:

// size=3, capacity=4

// [null, 21, 14, null]
//        ↓    ↓
//        9   null
//        ↓
//       null
// The hash function is:

// int hashcode(int key, int capacity) {
//     return key % capacity;
// }
// here we have three numbers, 9, 14 and 21, where 21 and 9 share the same position as they all have the same hashcode 1 (21 % 4 = 9 % 4 = 1). We store them in the hash table by linked list.

// rehashing this hash table, double the capacity, you will get:

// size=3, capacity=8

// index:   0    1    2    3     4    5    6   7
// hash : [null, 9, null, null, null, 21, 14, null]
// Given the original hash table, return the new hash table after rehashing .

// Example 1:

// Input:

// hashTable = [null, 21->9->null, 14->null, null]
// Output:

// [null, 9->null, null, null, null, 21->null, 14->null, null]
// Explanation:

// Double the capacity of the hash table and rearrange all the hash values.

/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

class Rehashing {

  /**
   * @param hashTable: A list of The first node of linked list
   * @return: A list of The first node of linked list which have twice size
   */
  public ListNode[] rehashing(ListNode[] hashTable) {
    if (hashTable.length <= 0) {
      return hashTable;
    }

    int newCapacity = 2 * hashTable.length;
    ListNode[] newTable = new ListNode[newCapacity];
    for (int i = 0; i < hashTable.length; i++) {
      // process all nodes in the bucket
      while (hashTable[i] != null) {
        int oldVal = hashTable[i].val;
        // this is for negative number
        int newIndex = (oldVal % newCapacity + newCapacity) % newCapacity;
        if (newTable[newIndex] == null) {
          newTable[newIndex] = new ListNode(oldVal);
        } else {
          // old and new hash are the same
          ListNode head = newTable[newIndex];
          while (head.next != null) {
            head = head.next;
          }
          head.next = new ListNode(oldVal);
        }
        hashTable[i] = hashTable[i].next; // next node in the bucket
      }
    }

    return newTable;
  }
}
