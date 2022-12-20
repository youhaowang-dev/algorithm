// Linked List, Two Pointers
// Amazon 4 LinkedIn 3 Microsoft 6 Bloomberg 4 Adobe 2 Facebook 2 Google 2 Oracle 2 Apple 5 Yahoo 2 Samsung 2 Uber 2
// https://leetcode.com/problems/rotate-list/
// Given the head of a linked list, rotate the list to the right by k places.

// Example 1:
// Input: head = [1,2,3,4,5], k = 2
// Output: [4,5,1,2,3]
// Example 2:
// Input: head = [0,1,2], k = 4
// Output: [2,0,1]

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
class RotateList {

  // find the node, connect and disconnect
  // new end = length - (rotate % length) - 1
  public ListNode rotateRight(ListNode head, int rotation) {
    if (head == null || head.next == null || rotation == 0) {
      return head;
    }

    ListNode target = this.getTargetNode(head, rotation);
    if (target.next == null) {
      return head;
    }
    ListNode tail = this.getTail(head);

    ListNode newTail = target;
    ListNode newHead = target.next;
    target.next = null;
    tail.next = head;

    return newHead;
  }

  private ListNode getTargetNode(ListNode head, int rotation) {
    int length = this.getLength(head);
    int kth = length - rotation % length; // count from 1

    ListNode kthNode = head;
    for (int i = 1; i < kth; i++) {
      kthNode = kthNode.next;
    }

    return kthNode;
  }

  private ListNode getTail(ListNode head) {
    while (head.next != null) {
      head = head.next;
    }

    return head;
  }

  private int getLength(ListNode head) {
    int length = 0;

    while (head != null) {
      length++;
      head = head.next;
    }

    return length;
  }
}
