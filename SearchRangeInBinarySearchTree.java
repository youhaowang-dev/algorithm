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
    List<Integer> result = new ArrayList<>();
    if (root == null) {
      return result;
    }
    TreeNode start = this.getResultStart(root, k1);
    // get all elements <= k2
    InorderIterator iterator = new InorderIterator(root);
    if (start)
  }

  // binary search a node >= k1
  private TreeNode getResultStart(TreeNode root, int target) {
    TreeNode current = root;
    TreeNode greaterOrEqualNode = null;
    while (current != null) {
      if (current.val == target) {
        return current;
      }

      if (current.val > target) {
        greaterOrEqualNode = current;
        current = current.left;
      }

      if (current.val < target) {
        current = current.right;
      }
    }
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

    private void pushLefts() {
      while (this.current != null) {
        this.stack.push(this.current);
        this.current = this.current.left;
      }
    }
  }
}
