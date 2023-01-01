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

  // convert list to array to allow index access
  // time O(n) space O(n)
  public TreeNode sortedListToBST(ListNode head) {
    List<Integer> list = this.buildList(head);
    return this.buildBalancedBST(list, 0, list.size() - 1);
  }

  private List<Integer> buildList(ListNode node) {
    List<Integer> list = new ArrayList<>();
    while (node != null) {
      list.add(node.val);
      node = node.next;
    }

    return list;
  }

  private TreeNode buildBalancedBST(List<Integer> list, int left, int right) {
    if (left > right) {
      // left == right is fine as we need to create at least one node
      return null;
    }

    int mid = left + (right - left) / 2;
    TreeNode root = new TreeNode(list.get(mid));
    root.left = this.buildBalancedBST(list, left, mid - 1);
    root.right = this.buildBalancedBST(list, mid + 1, right);

    return root;
  }

  // dfs: inorder traverse and build the tree
  // time O(n) for two passes all nodes space O(logn) for balanced tree
  public TreeNode sortedListToBST(ListNode head) {
    if (head == null) {
      return null;
    }
    Pointer p = new Pointer(head);
    int listLength = this.getListLength(head);

    return buildBalancedBST(p, 0, listLength - 1);
  }

  private class Pointer {

    ListNode p;

    public Pointer(ListNode p) {
      this.p = p;
    }

    public void moveForward() {
      if (p != null) {
        p = p.next;
      }
    }
  }

  private int getListLength(ListNode node) {
    int length = 0;
    while (node != null) {
      length++;
      node = node.next;
    }

    return length;
  }

  // https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solutions/35502
  // Before: Pointer is always at start of linked list.
  // After left part finishes: Pointer is at middle, ie where the root is.
  // Before Generating right half: Pointer is at start of the right half.
  private TreeNode buildBalancedBST(Pointer p, int start, int end) {
    if (start > end) {
      return null;
    }

    int mid = (start + end) / 2;
    TreeNode left = this.buildBalancedBST(p, start, mid - 1);
    TreeNode root = new TreeNode(p.p.val);
    p.moveForward();
    root.left = left;
    root.right = this.buildBalancedBST(p, mid + 1, end);

    return root;
  }

  // Time Complexity: O(nlogn)
  // logn subproblems, each problem does one findMid
  // findMin complexity: O(n) -> O(n/2) -> ...
  // logn * (n + n/2 + n/4 + ...) = logn * 2n ===> O(nlogn)
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

  // build BST in inorder traversal
  // NOTE: global variable is used
  private ListNode head;

  private int getListLength(ListNode head) {
    ListNode ptr = head;
    int length = 0;
    while (head != null) {
      head = head.next;
      length += 1;
    }

    return length;
  }

  private TreeNode convertListToBST(int l, int r) {
    if (l > r) {
      return null;
    }

    int mid = (l + r) / 2;

    // First step of simulated inorder traversal. Recursively form
    // the left half
    TreeNode left = this.convertListToBST(l, mid - 1);

    // Once left half is traversed, process the current node
    TreeNode node = new TreeNode(this.head.val);
    node.left = left;

    // Maintain the invariance mentioned in the algorithm
    this.head = this.head.next;

    // Recurse on the right hand side and form BST out of them
    node.right = this.convertListToBST(mid + 1, r);
    return node;
  }

  public TreeNode sortedListToBST(ListNode head) {
    int size = this.getListLength(head);

    this.head = head;

    return this.convertListToBST(0, size - 1);
  }
}
