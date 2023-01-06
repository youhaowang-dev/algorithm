// Linked List, Two Pointers
// Amazon 10 Apple 6 Adobe 4 Facebook 4 Microsoft 3 Bloomberg 3 Yahoo 2 eBay 2 American Express 2 Dell 2 Google 5 Uber 3 Nvidia 2 VMware 2 Salesforce 2 Walmart Global Tech 2 Intel 2 Paypal 3 Oracle 2 Nagarro 2
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

// Given the head of a linked list, remove the nth node from the end of the list and return its head.

// Example 1:
// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]
// Example 2:
// Input: head = [1], n = 1
// Output: []
// Example 3:
// Input: head = [1,2], n = 1
// Output: [1]

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
class RemoveNthNodeFromEndofList {

  // two passes: find the len, use counter to find the node before target

  // two pointers
  // one stop at the end.next(null)
  // one stop at the (n+1)th from the end
  // then remove the nth
  // 1,2,3,null remove the 1st from the end; one stops at null, the other one should stop at 2
  // so the fast pointer should move n+1(1+1) steps before both pointers move
  public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode beforeHead = new ListNode(0); // the list structure will change, so head can be removed, so we need an extra pointer
    beforeHead.next = head;
    ListNode stopAtNull = beforeHead;
    ListNode beforeTarget = beforeHead;
    // move fast pointer
    while (n >= 0) {
      stopAtNull = stopAtNull.next;
      n--;
    }

    // move both pointers
    while (stopAtNull != null) {
      stopAtNull = stopAtNull.next;
      beforeTarget = beforeTarget.next;
    }

    beforeTarget.next = beforeTarget.next.next;

    return beforeHead.next;
  }
}
