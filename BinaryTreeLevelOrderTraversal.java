// Tree, Breadth-First Search, Binary Tree
// Bloomberg 11 Amazon 10 LinkedIn 2 Microsoft 8 Facebook 7 Oracle 4 Google 3 Apple 3 ServiceNow 3 Splunk 2 Adobe 2 Uber 3 Paypal 2 Visa 2 Accolite 2 TikTok 2
// https://leetcode.com/problems/binary-tree-level-order-traversal/

// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

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
class BinaryTreeLevelOrderTraversal {

  public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) {
      return result;
    }

    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);

    while (!queue.isEmpty()) {
      List<Integer> currentLevelResult = new ArrayList<>();
      int currentLevelCount = queue.size();
      for (int i = 0; i < currentLevelCount; i++) {
        TreeNode node = queue.poll();
        if (node == null) {
          continue;
        }
        currentLevelResult.add(node.val);
        this.addNextLevelNodes(node, queue);
      }
      result.add(currentLevelResult);
    }

    return result;
  }

  private void addNextLevelNodes(TreeNode node, Queue<TreeNode> queue) {
    if (node.left != null) {
      queue.offer(node.left);
    }
    if (node.right != null) {
      queue.offer(node.right);
    }
  }
}
