// Tree, Depth-First Search, Binary Tree
// Facebook 24 Amazon 22 Bloomberg 8 Microsoft 4 Karat 4 Google 2 LinkedIn 2 Oracle 2 Yahoo 2 Splunk 2 Qualcomm 2 TikTok 2 Samsung 2
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
// Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

// According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
// two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

// p and q will exist in the tree.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class LowestCommonAncestorOfABinaryTree {

  // search LCA in subtrees
  // if found both, return current root
  // if found one, return the one
  // if found none, return null
  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null) {
      return null;
    }
    if (root == p || root == q) {
      return root;
    }

    // divide
    TreeNode ancestor1 = this.lowestCommonAncestor(root.left, p, q);
    TreeNode ancestor2 = this.lowestCommonAncestor(root.right, p, q);

    // conquer(merge subtree results)
    if (ancestor1 != null && ancestor2 != null) {
      return root;
    }
    if (ancestor1 != null) {
      return ancestor1;
    }
    if (ancestor2 != null) {
      return ancestor2;
    }

    return null;
  }
}
