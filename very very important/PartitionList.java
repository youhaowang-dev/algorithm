// Linked List, Two Pointers
// Adobe 3 Microsoft 2 Bloomberg 2 Apple 3 Facebook 2 Amazon 5
// https://leetcode.com/problems/partition-list/

// Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

// You should preserve the original relative order of the nodes in each of the two partitions.

// Example 1:
// Input: head = [1,4,3,2,5,2], x = 3
// Output: [1,2,2,4,3,5]
// Example 2:
// Input: head = [2,1], x = 2
// Output: [1,2]

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class PartitionList {

  // two head nodes for two lists
  // merge them after processing all node
  public ListNode partition(ListNode head, int x) {
    ListNode smallHead = new ListNode(Integer.MIN_VALUE);
    smallHead.next = head; // or (..., head)
    ListNode bigHead = new ListNode(Integer.MIN_VALUE);

    // pointers for inserted node
    ListNode small = smallHead;
    ListNode big = bigHead;
    ListNode current = head;
    while (current != null) {
      if (current.val >= x) {
        big.next = current;
        big = big.next;
      }
      if (current.val < x) {
        small.next = current;
        small = small.next;
      }
      current = current.next;
    }
    // connect 3 lists
    small.next = bigHead.next;
    big.next = null;

    return smallHead.next;
  }
}
