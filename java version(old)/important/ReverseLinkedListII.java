// Linked List
// Amazon 7 Media.net 4 Apple 3 Microsoft 2 Facebook 6 Google 4 Bloomberg 2 Adobe 2 Yahoo 2 Walmart Global Tech 2 ByteDance 2 Shopee 2
// https://leetcode.com/problems/reverse-linked-list-ii/

// Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

// Example 1:
// Input: head = [1,2,3,4,5], left = 2, right = 4
// Output: [1,4,3,2,5]
// Example 2:
// Input: head = [5], left = 1, right = 1
// Output: [5]

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
class ReverseLinkedListII {

  public ListNode reverseBetween(ListNode head, int left, int right) {
    if (left >= right || head == null) {
      return head;
    }

    ListNode headPrev = new ListNode(Integer.MIN_VALUE);
    headPrev.next = head;

    // get left list tail
    ListNode leftListTail = headPrev;
    for (int i = 1; i < left; i++) {
      if (leftListTail == null) {
        return null;
      }
      leftListTail = leftListTail.next;
    }
    // save reversed list tail
    ListNode reversedListTail = leftListTail.next;

    // prev will stop at right
    // current will stop at right next
    ListNode prev = leftListTail.next;
    ListNode current = prev.next;
    for (int i = left; i < right; i++) {
      if (current == null) {
        return null;
      }
      ListNode currentNext = current.next;
      current.next = prev;
      prev = current;
      current = currentNext;
    }

    ListNode reversedListHead = prev;
    ListNode rightListHead = current;

    leftListTail.next = reversedListHead;
    reversedListTail.next = rightListHead;

    return headPrev.next;
  }
}
