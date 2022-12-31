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

  private class TreeNodeWithSum {

    TreeNode node;
    int sum;

    public TreeNodeWithSum(TreeNode node, int sum) {
      this.node = node;
      this.sum = sum;
    }
  }

  // bfs
  public boolean hasPathSum(TreeNode root, int targetSum) {
    if (root == null) {
      return false;
    }

    Queue<TreeNodeWithSum> queue = new LinkedList<>();
    queue.offer(new TreeNodeWithSum(root, root.val));
    while (!queue.isEmpty()) {
      TreeNodeWithSum nodeWithSum = queue.poll();
      TreeNode node = nodeWithSum.node;
      int sum = nodeWithSum.sum;
      if (this.isLeaf(node) && sum == targetSum) {
        return true;
      }

      if (node.left != null) {
        queue.offer(new TreeNodeWithSum(node.left, sum + node.left.val));
      }

      if (node.right != null) {
        queue.offer(new TreeNodeWithSum(node.right, sum + node.right.val));
      }
    }

    return false;
  }

  private boolean isLeaf(TreeNode node) {
    return node.left == null && node.right == null;
  }

  // dfs
  public boolean hasPathSum(TreeNode root, int targetSum) {
    if (root == null) {
      return false;
    }

    int newTargetSum = targetSum - root.val;
    if (root.left == null && root.right == null) {
      return newTargetSum == 0;
    }

    boolean leftHasPathSum = this.hasPathSum(root.left, newTargetSum);
    boolean rightHasPathSum = this.hasPathSum(root.right, newTargetSum);

    return leftHasPathSum || rightHasPathSum;
  }
}
