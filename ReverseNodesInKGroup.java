// Linked List, Recursion
// Amazon 14 Microsoft 10 Apple 4 Bloomberg 4 Adobe 4 Google 2 TikTok 2 Capital One 8 Facebook 5 Yahoo 3 ByteDance 3 Zoom 2 MakeMyTrip 2 Zenefits 2 eBay 3 Uber 3 Snapchat 2 VMware 2 Qualcomm 2 Walmart Global Tech 2 Oracle 2 PayTM 2 Intuit 2 Tesla 2
// https://leetcode.com/problems/reverse-nodes-in-k-group/

// Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

// k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

// You may not alter the values in the list's nodes, only nodes themselves may be changed.

// Example 1:
// Input: head = [1,2,3,4,5], k = 2
// Output: [2,1,4,3,5]
// Example 2:
// Input: head = [1,2,3,4,5], k = 3
// Output: [3,2,1,4,5]

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
class ReverseNodesInKGroup {

  public ListNode reverseKGroup(ListNode head, int k) {
    ListNode prevRevTail = null;
    ListNode firstRevHead = null;
    ListNode current = head;
    ListNode reverseStart = head;
    while (current != null) {
      int count = 0;
      while (count < k && current != null) {
        current = current.next;
        count += 1;
      }
      if (count == k) {
        // current stops at the next reverseStart
        ListNode revHead = this.reverse(reverseStart, k);

        if (firstRevHead == null) {
          // if is for init
          firstRevHead = revHead;
        }

        if (prevRevTail != null) {
          // if is for init
          // connect tail of prev reversed  with head of current reversed
          prevRevTail.next = revHead;
        }

        prevRevTail = reverseStart;
        reverseStart = current;
      }
    }

    // attach the final, possibly un-reversed portion
    if (prevRevTail != null) {
      prevRevTail.next = reverseStart;
    }

    return firstRevHead != null ? firstRevHead : head;
  }

  // Reverse k nodes
  public ListNode reverse(ListNode head, int k) {
    ListNode prev = null;
    ListNode current = head;
    while (k > 0) {
      ListNode nextCurrent = current.next;
      current.next = prev;
      prev = current;
      current = nextCurrent;

      k--;
    }

    return prev;
  }
}
