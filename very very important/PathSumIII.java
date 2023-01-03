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

  // dfs with prefix sum
  // time O(n) space O(n)
  // There is just one thing that is particular for the binary tree. There are two ways to go forward -
  // to the left and to the right. To keep parent->child direction, we shouldn't blend prefix sums from the left and right subtrees in one hashmap.
  public int pathSum(TreeNode root, int target) {
    Map<Long, Integer> prefixSumToCount = new HashMap();
    this.traverse(root, target, 0, prefixSumToCount);
    return this.count;
  }

  // preorder
  public void traverse(
    TreeNode node,
    int target,
    long sum,
    Map<Long, Integer> prefixSumToCount
  ) {
    if (node == null) {
      return;
    }

    long currentSum = sum + node.val;

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

    this.traverse(node.left, target, currentSum, prefixSumToCount);
    this.traverse(node.right, target, currentSum, prefixSumToCount);

    // reset the prefix sum count to the previous count as the current subtree is done
    prefixSumToCount.put(currentSum, prefixSumToCount.get(currentSum) - 1);
  }

  // dfs
  // time O(n^2) every node will need to do a scan for rest of the children
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

  public int pathSum(TreeNode root, int sum) {
    if (root == null) return 0;
    return (
      pathSumFrom(root, sum) +
      pathSum(root.left, sum) +
      pathSum(root.right, sum)
    );
  }

  private int pathSumFrom(TreeNode node, int sum) {
    if (node == null) {
      return 0;
    }
    int currentSumCount = node.val == sum ? 1 : 0;
    int remainSum = sum - node.val;
    int leftSumCount = this.pathSumFrom(node.left, remainSum);
    int rightSumCount = this.pathSumFrom(node.right, remainSum);

    return currentSumCount + leftSumCount + rightSumCount;
  }
}
