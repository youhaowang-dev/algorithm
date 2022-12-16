// Dynamic Programming, Tree, Depth-First Search, Binary Tree
// DoorDash 23 Microsoft 5 Amazon 4 Facebook 3 Bloomberg 2 Adobe 2 Apple 2 Samsung 2 TikTok 2 Akuna Capital 2 Google 8 ByteDance 6 Snapchat 3 Oracle 2 Twitter 2 Twilio 2 Yandex 2 Sprinklr 2 TuSimple 2
// https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

// A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has
// an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

// The path sum of a path is the sum of the node's values in the path.

// Given the root of a binary tree, return the maximum path sum of any non-empty path.

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

class BinaryTreeMaximumPathSum {

  private class PathVals {

    int rootToAny;
    int anyToAny;

    public PathVals(int rootToAny, int anyToAny) {
      this.rootToAny = rootToAny;
      this.anyToAny = anyToAny;
    }
  }

  // max(root to any) = max(left root to any, right root to any) + root.val
  // max(any to any) = max(any to any, max left root to any + max right root to any + root.val)
  // val can be negative, so is the max left/right/total, so max(0, ...) is needed
  public int maxPathSum(TreeNode root) {
    return this.getMaxPathSum(root).anyToAny;
  }

  private PathVals getMaxPathSum(TreeNode root) {
    // exit
    if (root == null) {
      return new PathVals(Integer.MIN_VALUE, Integer.MIN_VALUE);
    }

    // divide
    PathVals leftVals = this.getMaxPathSum(root.left);
    PathVals rightVals = this.getMaxPathSum(root.right);

    // merge
    int maxRootToAny =
      Math.max(0, Math.max(leftVals.rootToAny, rightVals.rootToAny)) + root.val;
    int derivedAnyToAny =
      Math.max(0, leftVals.rootToAny) +
      Math.max(0, rightVals.rootToAny) +
      root.val;
    int maxAnyToAny = Math.max(
      derivedAnyToAny,
      Math.max(leftVals.anyToAny, rightVals.anyToAny)
    );

    return new PathVals(maxRootToAny, maxAnyToAny);
  }
}
