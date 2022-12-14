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
    if (root == null) {
      return result;
    }

    List<Integer> leftResults = this.preorderTraversalDivideConquer(root.left);
    List<Integer> rightResults =
      this.preorderTraversalDivideConquer(root.right);

    result.add(root.val);
    result.addAll(leftResults);
    result.addAll(rightResults);

    return result;
  }

  public List<Integer> preorderTraversalIterative(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    if (root == null) {
      return result;
    }

    Stack<TreeNode> stack = new Stack<>();
    this.addLeftsAndPushRights(root, result, stack);
    while (!stack.isEmpty()) {
      TreeNode currentRoot = stack.pop();
      this.addLeftsAndPushRights(currentRoot, result, stack);
    }

    return result;
  }

  private void addLeftsAndPushRights(
    TreeNode node,
    List<Integer> result,
    Stack<TreeNode> stack
  ) {
    while (node != null) {
      // root is not null, because root-left-right order, add it now
      result.add(node.val);
      stack.push(node.right);
      node = node.left;
    }
  }
}
