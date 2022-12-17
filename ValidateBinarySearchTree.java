// Tree, Depth-First Search, Binary Search Tree, Binary Tree
// Amazon 19 Bloomberg 19 Apple 5 Microsoft 4 Yahoo 3 Zillow 3 Facebook 2 Salesforce 2 Uber 2 Yandex 2 Paypal 2
// https://leetcode.com/problems/validate-binary-search-tree/
// Given the root of a binary tree, determine if it is a valid binary search tree (BST).

// A valid BST is defined as follows:

// The left  subtree of a node contains only nodes with keys less than the node's key.
// The right subtree of a node contains only nodes with keys greater than the node's key.
// Both the left and right subtrees must also be binary search trees.

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

class ValidateBinarySearchTree {

  // Not only the right child should be larger than the node but all the elements in the right subtree.
  // so we need to compare more than two nodes.
  public boolean isValidBST(TreeNode root) {}
}
