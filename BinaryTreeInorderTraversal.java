// Stack, Tree, Depth-First Search, Binary Tree
// Amazon 8 Adobe 4 Google 3 Facebook 2 Microsoft 2 Apple 3 Yahoo 2
// https://leetcode.com/problems/binary-tree-inorder-traversal/
// Given the root of a binary tree, return the inorder traversal of its nodes' values.

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

// inorder = left subtree -> root -> right subtree
import java.util.*;

class BinaryTreeInorderTraversal {

  public List<Integer> inorderTraversalRecursion(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    this.recursionHelp(root, result);

    return result;
  }

  private void recursionHelp(TreeNode root, List<Integer> result) {
    if (root == null) {
      return;
    }

    // left-root-right
    this.recursionHelp(root.left, result);
    result.add(root.val);
    this.recursionHelp(root.right, result);
  }

  public List<Integer> inorderTraversalDivideConquer(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    if (root == null) {
      return result;
    }

    List<Integer> leftResults = this.inorderTraversalDivideConquer(root.left);
    List<Integer> rightResults = this.inorderTraversalDivideConquer(root.right);
    result.addAll(leftResults);
    result.add(root.val);
    result.addAll(rightResults);

    return result;
  }

  public List<Integer> inorderTraversalIterative(TreeNode root) {
    List<Integer> result = new ArrayList<>();
  }
}
