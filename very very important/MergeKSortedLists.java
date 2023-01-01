// Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
// Amazon 41 Microsoft 5 Uber 5 Facebook 5 Apple 4 Google 4 Adobe 3 Walmart Global Tech 3 Indeed 2 Bloomberg 2 Zillow 2 Media.net 2 ByteDance 10 VMware 5 LinkedIn 4 TikTok 4 Shopee 3 Sprinklr 3 Snapchat 2 Oracle 2 Goldman Sachs 2 Yandex 2
// https://leetcode.com/problems/merge-k-sorted-lists/

// You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

// Merge all the linked-lists into one sorted linked-list and return it.

// Example 1:
// Input: lists = [[1,4,5],[1,3,4],[2,6]]
// Output: [1,1,2,3,4,4,5,6]
// Explanation: The linked-lists are:
// [
//   1->4->5,
//   1->3->4,
//   2->6
// ]
// merging them into one sorted list:
// 1->1->2->3->4->4->5->6

// Example 2:
// Input: lists = []
// Output: []

// Example 3:
// Input: lists = [[]]
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
class MergeKSortedLists {

  private class ListMinIterator {

    PriorityQueue<ListNode> minHeap;

    public ListMinIterator(ListNode[] lists) {
      this.minHeap = new PriorityQueue<>((a, b) -> a.val - b.val);

      for (ListNode list : lists) {
        if (list != null) {
          this.minHeap.offer(list);
        }
      }
    }

    public ListNode getNext() {
      if (!this.hasNext()) {
        return null;
      }

      ListNode node = this.minHeap.poll();

      if (node.next != null) {
        this.minHeap.offer(node.next);
      }

      return node;
    }

    public boolean hasNext() {
      return !this.minHeap.isEmpty();
    }
  }

  // min heap
  // O(Nlogk)
  public ListNode mergeKLists(ListNode[] lists) {
    ListNode beforeHead = new ListNode(0);
    ListMinIterator iterator = new ListMinIterator(lists);

    ListNode current = beforeHead;
    while (iterator.hasNext()) {
      ListNode next = iterator.getNext();
      current.next = next;
      current = current.next;
    }

    return beforeHead.next;
  }

  // for space optimized solution
  // Convert merge k lists problem to merge 2 lists (k-1) times.
  // time O(kN) space O(1)

  // divide and conquer
  // like a merge sort
  // Time complexity : O(Nlog⁡k) where k is the number of linked lists.
  // We can merge two sorted linked list in O(n) time where nnn is the total number of nodes in two lists.
  public ListNode mergeKLists(ListNode[] lists) {
    if (lists == null || lists.length == 0) {
      return null;
    }
    return this.mergeHelper(lists, 0, lists.length - 1);
  }

  private ListNode mergeHelper(ListNode[] lists, int start, int end) {
    // [0,7] => [0,3][4,7] => [0,1][2,2][4,5][6,7] => [0,0][1,1][2,2][4,4][5,5][6,6][7,7]
    // partition end result
    if (start == end) {
      System.out.println(start + ":" + end);
      return lists[start];
    }

    int mid = start - (start - end) / 2;
    ListNode left = this.mergeHelper(lists, start, mid);
    ListNode right = this.mergeHelper(lists, mid + 1, end);

    return this.mergeTwoLists(left, right);
  }

  private ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode beforeHead = new ListNode(0);
    ListNode tail = beforeHead;
    while (list1 != null && list2 != null) {
      if (list1.val < list2.val) {
        tail.next = list1;
        list1 = list1.next;
      } else {
        tail.next = list2;
        list2 = list2.next;
      }
      tail = tail.next;
    }
    if (list1 != null) {
      tail.next = list1;
    }
    if (list2 != null) {
      tail.next = list2;
    }

    return beforeHead.next;
  }
}
