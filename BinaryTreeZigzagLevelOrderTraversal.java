// Tree, Breadth-First Search, Binary Tree
// Amazon 17 Bloomberg 8 Microsoft 7 Facebook 3 Adobe 3 Yandex 3 Apple 2 Oracle 2 Walmart Global Tech 2 LinkedIn 4 Google 2 ServiceNow 2 Salesforce 2 VMware 2 SAP 2 Cisco 2 TikTok 2
// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
// Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

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

// IMPORTANT: do not try to reverse during the traversal because tree left right will not make it work
// only reverse the level value results before adding to the master list
class BinaryTreeZigzagLevelOrderTraversal {

  enum Direction {
    TO_RIGHT,
    TO_LEFT,
  }

  public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) {
      return result;
    }
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    Direction direction = Direction.TO_RIGHT;

    while (!queue.isEmpty()) {
      List<TreeNode> nodes = this.getCurrentLevelNodes(queue);
      this.addCurrentLevelValues(nodes, result, direction);
      this.setNextLevelNodes(queue, nodes);
      direction = this.getNextDirection(direction);
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

  private void addCurrentLevelValues(
    List<TreeNode> nodes,
    List<List<Integer>> result,
    Direction direction
  ) {
    List<Integer> levelResult = new ArrayList<>();
    for (TreeNode node : nodes) {
      levelResult.add(node.val);
    }
    if (direction == Direction.TO_LEFT) {
      Collections.reverse(levelResult);
    }
    result.add(levelResult);
  }

  private void setNextLevelNodes(Queue<TreeNode> queue, List<TreeNode> nodes) {
    for (TreeNode node : nodes) {
      if (node.left != null) {
        queue.offer(node.left);
      }
      if (node.right != null) {
        queue.offer(node.right);
      }
    }
  }

  private Direction getNextDirection(Direction direction) {
    if (direction == Direction.TO_RIGHT) {
      return Direction.TO_LEFT;
    }

    if (direction == Direction.TO_LEFT) {
      return Direction.TO_RIGHT;
    }

    // throw new Exception("unhandled direction");
    return null;
  }
}
