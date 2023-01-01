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

  public ListNode deleteDuplicates(ListNode head) {
    ListNode beforeHead = new ListNode(Integer.MIN_VALUE); // do not use 0 as 0 can be in input
    beforeHead.next = head;

    ListNode prev = beforeHead;
    ListNode current = head;
    while (current != null) {
      if (prev.val == current.val) {
        // delete current
        prev.next = current.next;
        // update pointers
        current = prev.next;
      } else {
        // move pointers forward
        current = current.next;
        prev = prev.next;
      }
    }

    return beforeHead.next;
  }
}
