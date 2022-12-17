// Amazon 4 Google 3 Adobe 3 Spotify 3 Facebook 2 Uber 2 Bloomberg 2
// Tree, Depth-First Search, Binary Tree

// https://leetcode.com/problems/balanced-binary-tree/

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

class BalancedBinaryTree {

  public boolean isBalanced(TreeNode root) {
    return this.evaluateDepth(root).isBalanced;
  }

  private class Result {

    int depth;
    boolean isBalanced;

    public Result(int depth, boolean isBalanced) {
      this.depth = depth;
      this.isBalanced = isBalanced;
    }
  }

  private Result evaluateDepth(TreeNode root) {
    if (root == null) {
      return new Result(0, true);
    }

    Result leftResult = this.evaluateDepth(root.left);
    Result rightResult = this.evaluateDepth(root.right);

    if (!leftResult.isBalanced || !rightResult.isBalanced) {
      return new Result(0, false);
    }

    if (Math.abs(leftResult.depth - rightResult.depth) > 1) {
      return new Result(0, false);
    }

    // dont forget +1
    return new Result(Math.max(leftResult.depth, rightResult.depth) + 1, true);
  }
}
