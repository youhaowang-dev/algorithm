// Hash Table, Linked List, Two Pointers
// Amazon 8 Apple 7 Adobe 4 Bloomberg 3 Cisco 2 Spotify 5 Google 3 Goldman Sachs 3 Oracle 3 Microsoft 2 Yahoo 2 Visa 6 Nvidia 4 Facebook 3 Intel 3 Salesforce 3 Sprinklr 2 Splunk 2
// https://leetcode.com/problems/linked-list-cycle/

// Given head, the head of a linked list, determine if the linked list has a cycle in it.

// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

// Return true if there is a cycle in the linked list. Otherwise, return false.

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class LinkedListCycle {

  public boolean hasCycle(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;
    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;
      // init pointers are equal, so check after moving
      if (fast == slow) {
        return true;
      }
    }

    return false;
  }

  public boolean hasCycle(ListNode head) {
    Set<ListNode> visited = new HashSet<>();
    while (head != null) {
      if (visited.contains(head)) {
        return true;
      }
      visited.add(head);
      head = head.next;
    }

    return false;
  }
}
