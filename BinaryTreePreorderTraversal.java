// Stack, Tree, Depth-First Search, Binary Tree
// Google 3 Adobe 2 Apple 2 Amazon 4 Bloomberg 3 Microsoft 2
// https://leetcode.com/problems/binary-tree-preorder-traversal/
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

import java.util.*;

// root-left-right
class BinaryTreePreorderTraversal {

  public List<Integer> preorderTraversalRecursion(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    this.recursionHelper(root, result);

    return result;
  }

  private void recursionHelper(TreeNode root, List<Integer> result) {
    if (root == null) {
      return;
    }
    result.add(root.val);
    this.recursionHelper(root.left, result);
    this.recursionHelper(root.right, result);
  }

  public List<Integer> preorderTraversalDivideConquer(TreeNode root) {
    List<Integer> result = new ArrayList<>();
  }

  public List<Integer> preorderTraversalIterative(TreeNode root) {
    List<Integer> result = new ArrayList<>();
  }
}
