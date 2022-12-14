// Stack, Tree, Depth-First Search, Binary Tree
// Facebook 2 Amazon 2 Apple 2 TuSimple 2 Bloomberg 2

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

// left-right-root
class BinaryTreePostorderTraversal {

  public List<Integer> postorderTraversalRecursion(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    this.recursionHelper(root, result);

    return result;
  }

  private void recursionHelper(TreeNode root, List<Integer> result) {
    if (root == null) {
      return;
    }

    this.recursionHelper(root.left, result);
    this.recursionHelper(root.right, result);
    result.add(root.val);
  }

  public List<Integer> postorderTraversalDivideConquer(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    if (root == null) {
      return result;
    }

    List<Integer> leftResults = this.postorderTraversalDivideConquer(root.left);
    List<Integer> rightResults =
      this.postorderTraversalDivideConquer(root.right);

    result.addAll(leftResults);
    result.addAll(rightResults);
    result.add(root.val);

    return result;
  }

  // linked list and append root at the head
  public List<Integer> postorderTraversalIterative(TreeNode root) {
    LinkedList<Integer> result = new LinkedList<>();
    if (root == null) {
      return result;
    }

    Stack<TreeNode> stack = new Stack<>();
    stack.push(root);

    while (!stack.isEmpty()) {
      TreeNode currentRoot = stack.pop();
      result.addFirst(currentRoot.val);
      if (currentRoot.left != null) {
        stack.push(currentRoot.left);
      }
      if (currentRoot.right != null) {
        stack.push(currentRoot.right);
      }
    }

    return result;
  }
}
