// Array, Divide and Conquer, Stack, Tree, Monotonic Stack, Binary Tree
// Amazon 3 Microsoft
// https://leetcode.com/problems/maximum-binary-tree/

// You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

// Create a root node whose value is the maximum value in nums.
// Recursively build the left subtree on the subarray prefix to the left of the maximum value.
// Recursively build the right subtree on the subarray suffix to the right of the maximum value.
// Return the maximum binary tree built from nums.

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

class MaximumBinaryTree {

  // https://leetcode.com/problems/maximum-binary-tree/solution/158169
  // "This is also called a Cartesian Tree. One interesting property is that if we do an in-order traversal, we get the array back which we used to create it."

  // find max index and partition the array and build the tree
  public TreeNode constructMaximumBinaryTree(int[] nums) {
    return this.buildTree(nums, 0, nums.length - 1);
  }

  private TreeNode buildTree(int[] nums, int start, int end) {
    if (start > end) {
      return null;
    }

    if (start == end) {
      return new TreeNode(nums[start]);
    }

    int maxNumIndex = this.getMaxNumIndex(nums, start, end);
    TreeNode node = new TreeNode(nums[maxNumIndex]);
    node.left = this.buildTree(nums, start, maxNumIndex - 1);
    node.right = this.buildTree(nums, maxNumIndex + 1, end);

    return node;
  }

  private int getMaxNumIndex(int[] nums, int start, int end) {
    if (start >= end) {
      return -1; // throw
    }

    int maxNumIndex = 0;
    int maxNum = Integer.MIN_VALUE;
    for (int i = start; i <= end; i++) {
      if (nums[i] > maxNum) {
        maxNum = nums[i];
        maxNumIndex = i;
      }
    }

    return maxNumIndex;
  }
}
