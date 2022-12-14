// Linked List, Two Pointers
// Amazon 4 Google 3 Adobe 2 Apple 2 Microsoft 2 Bloomberg 3 Facebook 3 Goldman Sachs 8 Qualcomm 3 Arista Networks 2 ByteDance 2 Paypal 2
// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

// Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

// Example 1:
// Input: head = [1,1,2]
// Output: [1,2]

// Example 2:
// Input: head = [1,1,2,3,3]
// Output: [1,2,3]

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
class RemoveDuplicatesFromSortedList {

  // two pointers slow and fast
  // delete while fast moves forward
  public ListNode deleteDuplicates(ListNode head) {
    ListNode beforeHead = new ListNode(Integer.MIN_VALUE); // do not use 0 as 0 can be in input
    beforeHead.next = head;

    ListNode slow = beforeHead;
    ListNode fast = beforeHead.next;
    while (fast != null) {
      if (slow.val == fast.val) {
        // same: remove fast and move pointers
        slow.next = fast.next;
        fast = slow.next;
      } else {
        // different: move pointers
        slow = slow.next;
        fast = fast.next;
      }
    }

    return beforeHead.next;
  }
}
