// summary of iterative solutions for preorder, inorder, and postorder(not very important)

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
        current = current.left; // go to left subtree
      }
    }

    return result;
  }

  public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    Stack<TreeNode> stack = new Stack<>();
    TreeNode current = root;
    while (!stack.isEmpty() || current != null) {
      if (current == null) {
        TreeNode node = stack.pop();
        result.add(node.val); // left subtree is done, add now; left-root-right
        current = node.right; // go to right subtree
      } else {
        stack.push(current);
        current = current.left; // go to left subtree
      }
    }

    return result;
  }

  // https://leetcode.com/problems/binary-tree-postorder-traversal/solutions/45551/preorder-inorder-and-postorder-iteratively-summarization/comments/44991
  // "The key point is when you pop a node from stack, you ensure you have already explored its children."
  // Important, when you pop a node, ensure its children are traversed.
  public List<Integer> postorderTraversal(TreeNode root) {
    Stack<TreeNode> stack = new Stack();
    List<Integer> result = new ArrayList<Integer>();
    TreeNode cur = root;

    while (!stack.empty() || cur != null) {
      while (!this.isLeaf(cur)) {
        stack.push(cur);
        cur = cur.left;
      }

      if (cur != null) {
        result.add(cur.val);
      }

      while (!stack.empty() && cur == stack.peek().right) {
        TreeNode node = stack.pop();
        result.add(node.val);
        cur = node;
      }

      if (stack.empty()) {
        cur = null;
      } else {
        cur = stack.peek().right;
      }
    }

    return result;
  }

  private boolean isLeaf(TreeNode r) {
    if (r == null) return true;
    return r.left == null && r.right == null;
  }

  // https://leetcode.com/problems/binary-tree-postorder-traversal/solutions/45551/preorder-inorder-and-postorder-iteratively-summarization/
  // this is a trick because we are not visiting the node in postorder and may not work for all situations
  public List<Integer> postorderTraversalTrick(TreeNode root) {
    LinkedList<Integer> result = new LinkedList<>();
    Stack<TreeNode> stack = new Stack<>();
    TreeNode current = root;
    while (!stack.isEmpty() || current != null) {
      if (current == null) {
        TreeNode node = stack.pop();
        current = node.left;
      } else {
        stack.push(current);
        result.addFirst(current.val);
        current = current.right;
      }
    }

    return result;
  }
}
