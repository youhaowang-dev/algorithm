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

    this.inorderTraversal(root, k1, k2, result);

    return result;
  }

  private void inorderTraversal(
    TreeNode root,
    int k1,
    int k2,
    List<Integer> result
  ) {
    if (root == null) {
      return;
    }

    int rootVal = root.val;

    if (k1 > rootVal) {
      this.inorderTraversal(root.right, k1, k2, result);
    }
    if (k1 <= rootVal && rootVal <= k2) {
      this.inorderTraversal(root.left, k1, k2, result);
      result.add(rootVal);
      this.inorderTraversal(root.right, k1, k2, result);
    }
    if (rootVal > k2) {
      this.inorderTraversal(root.left, k1, k2, result);
    }
  }
}
