// https://mrleonhuang.gitbooks.io/lintcode/content/binary-tree-and-divide-conquer/binary-tree-maximum-path-sum-ii.html
// Given a binary tree, find the maximum path sum from root.

// The path may end at any node in the tree and contain at least one node in it.

// Example

// Given the below binary tree:

//   1
//  / \
// 2   3
// return4. (1->3)

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
public class BinaryTreeMaximumPathSumII {

  // find maxRootToAny
  // root.val + max(leftSum, rightSum, 0)
  public int maxPathSum2(TreeNode root) {
    if (root == null) {
      return 0;
    }

    int leftSum = this.maxPathSum2(root.left);
    int rightSum = this.maxPathSum2(root.right);

    return root.val + Math.max(0, Math.max(leftSum, rightSum));
  }
}
