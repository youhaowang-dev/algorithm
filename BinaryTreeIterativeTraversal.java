// summary of iterative solutions for preorder, inorder, and postorder

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

class BinaryTreeIterativeTraversal {

  public List<Integer> preorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    Stack<TreeNode> stack = new Stack<>();
    TreeNode current = root;
    while (!stack.isEmpty() || current != null) {
      if (current == null) {
        TreeNode node = stack.pop();
        current = node.right; // go to right subtree
      } else {
        stack.push(current);
        result.add(current.val); // root-left-right, so add before going to left subtree
        current = current.left;
      }
    }

    return result;
  }

  public List<Integer> inorderTraversal(TreeNode root) {}

  public List<Integer> postorderTraversal(TreeNode root) {}
}
