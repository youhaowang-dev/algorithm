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
  // reverse the second half of the list
  // merge two lists
  public void reorderList(ListNode head) {
    if (head == null) {
      return;
    }

    ListNode mid = this.getMid(head);
    ListNode reversedHead = this.reverse(mid.next);
    mid.next = null;
    this.merge(head, reversedHead);
  }

  // two pointers fast and slow
  private ListNode getMid(ListNode node) {
    ListNode slow = node;
    ListNode fast = node;
    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;
    }

    return slow;
  }

  // two pointers same speed
  private ListNode reverse(ListNode node) {
    ListNode prev = null;
    ListNode current = node;
    while (current != null) {
      ListNode currentNext = current.next;
      current.next = prev;
      prev = current;
      current = currentNext;
    }

    return prev;
  }

  private void merge(ListNode list1, ListNode list2) {
    ListNode beforeHead = new ListNode(0);
    ListNode current = beforeHead;
    int counter = 0;
    while (list1 != null && list2 != null) {
      boolean firstListInsert = counter % 2 == 0;
      if (firstListInsert) {
        current.next = list1;
        list1 = list1.next;
      } else {
        current.next = list2;
        list2 = list2.next;
      }
      current = current.next;
      counter++;
    }
    if (list1 != null) {
      current.next = list1;
    }
    if (list2 != null) {
      current.next = list2;
    }
  }
}
