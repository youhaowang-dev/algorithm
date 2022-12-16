// Tree, Depth-First Search, Breadth-First Search, Binary Tree
// Amazon 6 Google 3 Bloomberg 2 Microsoft 8 Facebook 7 Walmart Global Tech 2
// https://leetcode.com/problems/path-sum/
// Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

// A leaf is a node with no children.

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

// only check root-leaf
class PathSum {

  public boolean hasPathSum(TreeNode root, int targetSum) {
    if (root == null) {
      return false;
    }

    targetSum = targetSum - root.val;
    if (root.left == null && root.right == null) {
      return targetSum == 0;
    }

    return (
      this.hasPathSum(root.left, targetSum) ||
      this.hasPathSum(root.right, targetSum)
    );
  }
}
