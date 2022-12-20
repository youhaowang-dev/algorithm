// Linked List, Two Pointers, Stack, Recursion
// Amazon 5 Adobe 4 Google 3 Microsoft 2 Bloomberg 2 Apple 2 Samsung 2 Facebook 2 ByteDance 2 Yahoo 2 Uber 2 Splunk 3 Snapchat 2 Expedia 2 Oracle 2
// https://leetcode.com/problems/reorder-list/

// You are given the head of a singly linked-list. The list can be represented as:

// L0 → L1 → … → Ln - 1 → Ln
// Reorder the list to be on the following form:

// L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
// You may not modify the values in the list's nodes. Only nodes themselves may be changed.

// Example 1:
// Input: head = [1,2,3,4]
// Output: [1,4,2,3]
// Example 2:
// Input: head = [1,2,3,4,5]
// Output: [1,5,2,4,3]

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
class ReorderList {

  // find mid
  // reverse the second half
  // merge
  public void reorderList(ListNode head) {
    if (head == null) {
      return;
    }
    ListNode mid = this.getMid(head);
    ListNode midNext = mid.next;
    mid.next = null;
    ListNode reversedHead = this.reverse(midNext);
    this.merge(head, reversedHead);
  }

  public ListNode getMid(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;
    while (fast.next != null && fast.next.next != null) {
      slow = slow.next;
      fast = fast.next.next;
    }

    return slow;
  }

  public ListNode reverse(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    while (curr != null) {
      ListNode nextTemp = curr.next;
      curr.next = prev;
      prev = curr;
      curr = nextTemp;
    }
    return prev;
  }

  public void merge(ListNode first, ListNode second) {
    ListNode firstNext;
    ListNode secondNext;
    while (first != null && second != null) {
      firstNext = first.next;
      first.next = second;
      first = firstNext; // update first so second can connect to the correct first

      secondNext = second.next;
      second.next = first;
      second = secondNext;
    }
  }
}
