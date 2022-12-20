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
  // space optimized solution
  // Convert merge k lists problem to merge 2 lists (k-1) times.
  // time O(kN) space O(1)
}
