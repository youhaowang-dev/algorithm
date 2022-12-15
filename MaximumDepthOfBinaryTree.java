// Tree, Depth-First Search, Breadth-First Search, Binary Tree
// Amazon 5 Apple 5 Google 3 LinkedIn 2 Facebook 2 Adobe 2 Microsoft 5 Spotify 4 Bloomberg 2

// https://leetcode.com/problems/maximum-depth-of-binary-tree/

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

// Given the root of a binary tree, return its maximum depth.
// A binary tree's maximum depth is the number of nodes along
// the longest path from the root node down to the farthest leaf node.

class MaximumDepthOfBinaryTree {

  public int maxDepth(TreeNode root) {
    if (root == null) {
      return 0;
    }

    return Math.max(this.maxDepth(root.left), this.maxDepth(root.right)) + 1;
  }
}
