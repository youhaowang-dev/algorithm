// Tree, Breadth-First Search, Binary Tree
// Amazon 4 Apple 4 Microsoft 3
// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

// Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

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
class BinaryTreeLevelOrderTraversalII {

  public List<List<Integer>> levelOrderBottom(TreeNode root) {
    LinkedList<List<Integer>> result = new LinkedList<>();
    if (root == null) {
      return result;
    }

    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    while (!queue.isEmpty()) {
      List<TreeNode> currentLevelNodes = this.getCurrentLevelNodes(queue);
      List<Integer> currentLevelResult = new ArrayList<>();
      for (TreeNode node : currentLevelNodes) {
        currentLevelResult.add(node.val);
        if (node.left != null) {
          queue.offer(node.left);
        }
        if (node.right != null) {
          queue.offer(node.right);
        }
      }
      result.addFirst(currentLevelResult);
    }

    return result;
  }

  private List<TreeNode> getCurrentLevelNodes(Queue<TreeNode> queue) {
    List<TreeNode> nodes = new ArrayList<>();
    while (!queue.isEmpty()) {
      nodes.add(queue.poll());
    }

    return nodes;
  }
}
