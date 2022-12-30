// Tree, Depth-First Search, Breadth-First Search, Binary Tree
// Amazon 5 Apple 5 Google 3 Facebook 2 LinkedIn 10 Microsoft 5 Spotify 4 Adobe 3 Bloomberg 2 Intel 3 Visa 2 Yahoo Uber
// https://leetcode.com/problems/maximum-depth-of-binary-tree/

// Given the root of a binary tree, return its maximum depth.
// A binary tree's maximum depth is the number of nodes along
// the longest path from the root node down to the farthest leaf node.

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
class MaximumDepthOfBinaryTree {

  // depth = 1 + max(left subtree depth, right subtree depth) recursively
  public int maxDepth(TreeNode root) {
    // exit
    if (root == null) {
      return 0;
    }

    int subtreeMaxDepth = Math.max(
      this.maxDepth(root.left),
      this.maxDepth(root.right)
    );

    return subtreeMaxDepth + 1;
  }

  public int maxDepth(TreeNode root) {
    int depth = 0;
    if (root == null) {
      return depth;
    }

    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    while (!queue.isEmpty()) {
      depth++;
      int levelNodeCount = queue.size();
      for (int i = 0; i < levelNodeCount; i++) {
        TreeNode node = queue.poll();
        if (node.left != null) {
          queue.offer(node.left);
        }
        if (node.right != null) {
          queue.offer(node.right);
        }
      }
    }

    return depth;
  }
}
