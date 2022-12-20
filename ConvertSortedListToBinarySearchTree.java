// Linked List, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
// Facebook 11 Amazon 7 Google 3 Microsoft 3 Adobe 3 Apple 2 Paypal 2 Zenefits
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

// Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

// Example 1:
// Input: head = [-10,-3,0,5,9]
// Output: [0,-3,9,-10,null,5]
// Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
// Example 2:
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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class ConvertSortedListToBinarySearchTree {

  public TreeNode sortedListToBST(ListNode head) {
    if (head == null) {
      return null;
    }

    ListNode mid = this.findMidAndDisconnectPrev(head);

    TreeNode node = new TreeNode(mid.val); // root

    // edge case and exit condition; when list has only one node, add the tree node
    if (head == mid) {
      return node;
    }

    node.left = this.sortedListToBST(head);
    node.right = this.sortedListToBST(mid.next);

    return node;
  }

  private ListNode findMidAndDisconnectPrev(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;
    ListNode prevSlow = null;
    while (fast != null && fast.next != null) {
      prevSlow = slow;
      slow = slow.next;
      fast = fast.next.next;
    }
    if (prevSlow != null) {
      prevSlow.next = null;
    }

    return slow;
  }
}
