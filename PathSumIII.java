// Tree, Depth-First Search, Binary Tree
// Amazon 5 Bloomberg 3 Visa 3 Microsoft 2
// https://leetcode.com/problems/path-sum-iii/
// Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

// The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

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

class PathSumIII {

  private int count = 0;

  // There is just one thing that is particular for the binary tree. There are two ways to go forward -
  // to the left and to the right. To keep parent->child direction, we shouldn't blend prefix sums from the left and right subtrees in one hashmap.
  public int pathSum(TreeNode root, int target) {
    HashMap<Long, Integer> prefixSumToCount = new HashMap();
    this.preorder(root, target, 0, prefixSumToCount);
    return this.count;
  }

  public void preorder(
    TreeNode node,
    int target,
    long currentSum,
    HashMap<Long, Integer> prefixSumToCount
  ) {
    if (node == null) {
      return;
    }

    currentSum += node.val;

    if (currentSum == target) {
      this.count++;
    }

    long previousTargetSum = currentSum - target;
    if (prefixSumToCount.containsKey(previousTargetSum)) {
      this.count += prefixSumToCount.get(previousTargetSum);
    }

    prefixSumToCount.put(
      currentSum,
      prefixSumToCount.getOrDefault(currentSum, 0) + 1
    );

    this.preorder(node.left, target, currentSum, prefixSumToCount);
    this.preorder(node.right, target, currentSum, prefixSumToCount);

    // reset the prefix sum count to the previous count as the current subtree is done
    prefixSumToCount.put(currentSum, prefixSumToCount.get(currentSum) - 1);
  }

  public int pathSum(TreeNode root, int targetSum) {
    if (root == null) {
      return 0;
    }

    return (
      this.helper(root, targetSum) +
      this.pathSum(root.left, targetSum) +
      this.pathSum(root.right, targetSum)
    );
  }

  private int helper(TreeNode node, int targetSum) {
    if (node == null) {
      return 0;
    }

    return (
      (node.val == targetSum ? 1 : 0) +
      this.helper(node.left, targetSum - node.val) +
      this.helper(node.right, targetSum - node.val)
    );
  }
}
