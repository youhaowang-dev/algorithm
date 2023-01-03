// Hash Table, Linked List, Two Pointers
// Amazon 5 Microsoft 2 Bloomberg 2 Apple 2 ShareChat 2 Oracle 4 Facebook 2 Goldman Sachs 2 Paypal 2
// https://leetcode.com/problems/linked-list-cycle-ii/

// Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

// Do not modify the linked list.

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
public class LinkedListCycleII {

  public ListNode detectCycle(ListNode head) {
    Set<ListNode> visited = new HashSet<ListNode>();

    ListNode current = head;
    while (current != null) {
      if (visited.contains(current)) {
        return current;
      }
      visited.add(current);
      current = current.next;
    }

    return null;
  }

  // To find the entrance to the cycle, we have two pointers traverse at
  // the same speed -- one from the front of the list, and the other from
  // the point of intersection.

  // https://leetcode.com/problems/linked-list-cycle-ii/solutions/127485/linked-list-cycle-ii/comments/932331
  //     Algorithm: Assume non-cyclic length N and cyclic length M with index [0,M-1]
  // <-  N  ->          1. When slow enters the cycle at 0 (◎), fast is at N (■)
  //         s
  // □-□-□-□-◎-□-□-□    2. Fast is M-N behind, so they will meet at M-N (※)
  //         |     |
  //         □  M  ■ f  3. Cycle entrance is now M-(M-N) = N away, so if we
  //         |     |       make one pointer start over and both at slow speed,
  //         □-□-※-□       they will guarantee to meet again at 0 (◎)
  //            meet

  // https://leetcode.com/problems/linked-list-cycle-ii/solutions/127485/linked-list-cycle-ii/comments/892393
  // F + a = nC
  // F + a = n(a + b) <- because C = a + b
  // F + a = n*a + n*b
  // F = n*a + n*b - a
  // F = (n-1)*a + n*b
  // F = (n-1)*a + (n-1)*b + b
  // F = (n-1)*C + b

  // just use an example to reverse eng this formula
  // given start and the overlapped node, find the overlap start
  // so we can only play with the two nodes, start and overlap
  // use the example to play with them and tell interviewer your finding
  // we can also verify the finding with additional test cases
  public ListNode detectCycle(ListNode head) {
    if (head == null) {
      return null;
    }

    ListNode intersect = this.getIntersect(head);
    if (intersect == null) {
      // no cycle
      return null;
    }

    return this.getCycleStart(head, intersect);
  }

  // if has cycle, intersect and head will meet at the cycle begin
  private ListNode getCycleStart(ListNode head, ListNode intersect) {
    while (head != intersect) {
      head = head.next;
      intersect = intersect.next;
    }

    return head;
  }

  // fast and slow will meet if has cycle
  private ListNode getIntersect(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;

    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;
      if (slow == fast) {
        return slow;
      }
    }

    return null;
  }
}
