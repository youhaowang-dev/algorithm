// Tree, Depth-First Search, Binary Tree
// Amazon 4 Google 3 Adobe 3 Spotify 3 Facebook 2 Uber 2 Bloomberg 2
// https://leetcode.com/problems/balanced-binary-tree/

// Given a binary tree, determine if it is height-balanced.

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

    int maxSubtreeDepth = Math.max(leftResult.depth, rightResult.depth);

    return new Result(maxSubtreeDepth + 1, true);
  }

  // iterative postorder traversal
  public boolean isBalanced(TreeNode root) {
    Stack<TreeNode> stack = new Stack<TreeNode>();
    Map<TreeNode, Integer> nodeToheight = new HashMap<TreeNode, Integer>();

    TreeNode current = root;
    TreeNode lastVisitedNode = null;
    while (!stack.isEmpty() || current != null) {
      if (current != null) {
        stack.push(current);
        current = current.left;
      } else {
        TreeNode node = stack.peek();
        if (node.right != null && node.right != lastVisitedNode) {
          current = node.right;
        } else {
          int leftHeight = node.left != null
            ? nodeToheight.remove(node.left)
            : 0;
          int rightHeight = node.right != null
            ? nodeToheight.remove(node.right)
            : 0;

          if (Math.abs(leftHeight - rightHeight) > 1) {
            return false;
          }

          int maxNodeHeight = 1 + Math.max(leftHeight, rightHeight);
          nodeToheight.put(node, maxNodeHeight);
          stack.pop();
          lastVisitedNode = node;
        }
      }
    }

    return true;
  }
}
