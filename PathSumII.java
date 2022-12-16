// Backtracking, Tree, Depth-First Search, Binary Tree
// Amazon 5 Bloomberg 3 DoorDash 3 Zillow 2
// https://leetcode.com/problems/path-sum-ii/

// Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

// A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

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

class PathSumII {

  // bfs will cost too much space because each node will need to maintain a list
  // as a result, dfs is better for this question
  public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
    List<List<Integer>> result = new ArrayList<>();
    List<Integer> pathNodeValues = new ArrayList<>();
    this.searchSum(root, targetSum, pathNodeValues, result);

    return result;
  }

  // dfs
  private void searchSum(
    TreeNode root,
    int targetSum,
    List<Integer> pathNodeValues,
    List<List<Integer>> result
  ) {
    if (root == null) {
      return;
    }

    pathNodeValues.add(root.val);

    if (this.isLeaf(root) && targetSum == root.val) {
      result.add(new ArrayList<>(pathNodeValues));
    }

    if (root.left != null) {
      this.searchSum(
          root.left,
          targetSum - root.left.val,
          pathNodeValues,
          result
        );
    }

    if (root.right != null) {
      this.searchSum(
          root.right,
          targetSum - root.right.val,
          pathNodeValues,
          result
        );
    }
  }

  private boolean isLeaf(TreeNode node) {
    return node.left == null && node.right == null;
  }
}
