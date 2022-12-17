// Tree, Breadth-First Search, Binary Tree
// Amazon 4 Apple 4 Microsoft 3
// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

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
    // note: LinkedList<List is needed for addFirst
    LinkedList<List<Integer>> result = new LinkedList<>();
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
}
