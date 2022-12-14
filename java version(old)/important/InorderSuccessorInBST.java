// Tree, Depth-First Search, Binary Search Tree, Binary Tree
// Microsoft 3 Arista Networks 3 Facebook 4 Google 4 Adobe 3 Apple 2 Amazon 7 Bloomberg 3 Walmart Global Tech 2 Pocket Gems
// https://leetcode.com/problems/inorder-successor-in-bst/description/

// Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

// The successor of a node p is the node with the smallest key greater than p.val.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class InorderSuccessorInBST {

  // brute force: build inorder iterator for the tree, find target, get next node

  // tree is BST, so we can do binary search for a node where its value is greater than target
  // and it should be as small as possible
  public TreeNode inorderSuccessor(TreeNode root, TreeNode target) {
    TreeNode successor = null;
    TreeNode current = root;
    int targetVal = target.val;
    while (current != null) {
      int currentVal = current.val;
      if (targetVal == currentVal) {
        current = current.right; // question BST definition
      }
      // target successor in right tree
      if (targetVal > currentVal) {
        current = current.right;
      }
      // target successor in current tree, try to make it smaller
      if (targetVal < currentVal) {
        successor = current;
        current = current.left;
      }
    }

    return successor;
  }

  public TreeNode inorderSuccessor(TreeNode root, TreeNode target) {
    if (root == null || target == null) {
      return null;
    }

    if (target.val >= root.val) {
      // target successor in right tree
      return this.inorderSuccessor(root.right, target);
    }

    // target in current tree and target.val < root.val
    // make it as small as possible
    TreeNode successor = this.inorderSuccessor(root.left, target);
    if (successor == null) {
      return root;
    } else {
      return successor;
    }
  }
}
