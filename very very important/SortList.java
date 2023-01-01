// Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
// Amazon 4 Apple 4 TikTok 3 Microsoft 2 Google 2 Facebook 4 ByteDance 4 Adobe 2 Bloomberg 4 Uber 3 Yahoo 2
// https://leetcode.com/problems/sort-list/
// Given the head of a linked list, return the list after sorting it in ascending order.

// Example 1:
// Input: head = [4,2,1,3]
// Output: [1,2,3,4]
// Example 2:
// Input: head = [-1,5,3,4,0]
// Output: [-1,0,3,4,5]
// Example 3:
// Input: head = []
// Output: []

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
class SortList {

  // The problem is to sort the linked list in O(nlogn) time and O(logn) space
  // merge sort: partition list + merge
  public ListNode sortList(ListNode head) {
    if (head == null || head.next == null) {
      return head;
    }

    ListNode mid = this.partitionList(head);
    ListNode leftList = this.sortList(head);
    ListNode rightList = this.sortList(mid);
    return this.merge(leftList, rightList);
  }

  private ListNode partitionList(ListNode node) {
    ListNode slow = node;
    ListNode fast = node;
    ListNode prevSlow = null;
    while (fast != null && fast.next != null) {
      prevSlow = slow;
      slow = slow.next;
      fast = fast.next.next;
    }
    if (prevSlow != null) {
      // do the partition work
      prevSlow.next = null;
    }

    return slow;
  }

  private ListNode merge(ListNode list1, ListNode list2) {
    ListNode beforeHead = new ListNode(Integer.MIN_VALUE);
    ListNode current = beforeHead;
    while (list1 != null && list2 != null) {
      if (list1.val < list2.val) {
        current.next = list1;
        list1 = list1.next;
      } else {
        current.next = list2;
        list2 = list2.next;
      }
      current = current.next;
    }
    // connect rest
    if (list1 != null) {
      current.next = list1;
    }
    if (list2 != null) {
      current.next = list2;
    }

    return beforeHead.next;
  }
}
