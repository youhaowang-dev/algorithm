// https://www.lintcode.com/problem/11/description
// Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.

/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {

  /**
   * @param root: param root: The root of the binary search tree
   * @param k1: An integer
   * @param k2: An integer
   * @return: return: Return all keys that k1<=key<=k2 in ascending order
   */
  public List<Integer> searchRange(TreeNode root, int k1, int k2) {
    // write your code here
  }

  private class InorderIterator {

    TreeNode current;
    Stack<TreeNode> stack;

    public InorderIterator(TreeNode root) {
      this.current = root;
      this.stack = new Stack<TreeNode>();
      this.pushLefts();
    }

    public boolean hasNext() {
      return !this.stack.isEmpty() || this.current != null;
    }

    public TreeNode getNext() {
      if (!this.hasNext()) {
        return null;
      }

      if (!this.stack.isEmpty()) {
        TreeNode node = this.stack.pop();
        this.current = node;
        this.pushLefts();

        return node;
      }

      return null; // should not reach this line
    }

    private void pushLefts() {}
  }
}
