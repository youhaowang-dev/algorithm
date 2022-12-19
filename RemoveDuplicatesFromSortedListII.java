// Linked List
// Microsoft 2 Amazon 2 Adobe 2 Facebook 4 Bloomberg 3 Google 2 ByteDance 2 Arista Networks 2
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

// Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

// Example 1:
// Input: head = [1,2,3,3,4,4,5]
// Output: [1,2,5]

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
class RemoveDuplicatesFromSortedListII {

  public ListNode deleteDuplicates(ListNode head) {
    ListNode beforeHead = new ListNode(Integer.MIN_VALUE);
    beforeHead.next = head; // donot forget

    ListNode prev = beforeHead;
    ListNode current = head;
    while (current != null) {
      // detect duplicate
      if (current.next != null && current.val == current.next.val) {
        int duplicatedVal = current.val;
        // find the first non-duplicate node
        while (current != null && current.val == duplicatedVal) {
          current = current.next;
        }
        // currrent == null or current.val != duplicate skip all the duplicate nodes
        prev.next = current;
      } else {
        prev = current;
        current = current.next;
      }
    }

    return beforeHead.next;
  }
}