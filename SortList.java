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

  // The problem is to sort the linked list in O(nlogn) time and using only constant extra space.
  // If we look at various sorting algorithms, Merge Sort is one of the efficient sorting algorithms that
  // is popularly used for sorting the linked list. The merge sort algorithm runs in O(nlogn) time in all the cases.
  // Let's discuss approaches to sort linked list using merge sort.
  public ListNode sortList(ListNode head) {
    if (head == null || head.next == null) {
      return head;
    }

    ListNode mid = this.getMid(head);
    ListNode leftList = this.sortList(head);
    ListNode rightList = this.sortList(mid);
    return this.merge(leftList, rightList);
  }

  private ListNode getMid(ListNode node) {
    // two pointers and one speed is the 2x of the other
    ListNode slow = node;
    ListNode fast = node;
    ListNode prevSlow = null;
    while (fast != null && fast.next != null) {
      prevSlow = slow;
      slow = slow.next;
      fast = fast.next.next;
    }
    if (prevSlow != null) {
      // IMPORTANT: must detach the mid from the rest of the list
      // so the partition actually happens, otherwise the later
      // getMid calls will still treat the list end as the end instead
      // of the partition end
      prevSlow.next = null;
    }

    ListNode mid = slow;
    return mid;
  }

  private ListNode merge(ListNode list1, ListNode list2) {
    ListNode beforeHead = new ListNode(Integer.MIN_VALUE);
    ListNode last = beforeHead; // merged list insert position
    while (list1 != null && list2 != null) {
      if (list1.val < list2.val) {
        last.next = list1;
        list1 = list1.next;
      } else {
        last.next = list2;
        list2 = list2.next;
      }
      last = last.next;
    }
    // connect the leftovers
    if (list1 != null) {
      last.next = list1;
    }
    if (list2 != null) {
      last.next = list2;
    }

    return beforeHead.next;
  }
}
