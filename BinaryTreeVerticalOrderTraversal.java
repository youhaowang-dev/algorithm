// Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree
// Facebook 32 Bloomberg 11 Amazon 2 Microsoft 4 Oracle 2 Salesforce 3 Apple 2 VMware 2 Google Snapchat

// Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

// If two nodes are in the same row and column, the order should be from left to right.

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
class BinaryTreeVerticalOrderTraversal {

  private class TreeNodeWithCol {

    TreeNode node;
    int column;

    public TreeNodeWithCol(TreeNode node, int column) {
      this.node = node;
      this.column = column;
    }
  }

  public List<List<Integer>> verticalOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) {
      return result;
    }

    Map<Integer, List<Integer>> colToValues = new HashMap<>();
    Queue<TreeNodeWithCol> queue = new LinkedList<>();
    TreeNodeWithCol rootWithColumn = new TreeNodeWithCol(root, 0);
    queue.offer(rootWithColumn);
    int columnStart = 0;
    int columnEnd = 0;

    while (!queue.isEmpty()) {
      List<TreeNodeWithCol> nodes = this.getCurrentLevelNodes(queue);
      for (TreeNodeWithCol nodeWithCol : nodes) {
        this.addNodeToMapping(nodeWithCol, colToValues);
        int column = nodeWithCol.column;
        int leftCol = column - 1;
        int rightCol = column + 1;
        if (nodeWithCol.node.left != null) {
          queue.offer(new TreeNodeWithCol(nodeWithCol.node.left, leftCol));
          columnStart = Math.min(columnStart, leftCol);
        }
        if (nodeWithCol.node.right != null) {
          queue.offer(new TreeNodeWithCol(nodeWithCol.node.right, rightCol));
          columnEnd = Math.max(columnEnd, rightCol);
        }
      }
    }

    for (int i = columnStart; i <= columnEnd; i++) {
      result.add(colToValues.get(i));
    }

    return result;
  }

  private List<TreeNodeWithCol> getCurrentLevelNodes(
    Queue<TreeNodeWithCol> queue
  ) {
    List<TreeNodeWithCol> nodes = new ArrayList<>();
    while (!queue.isEmpty()) {
      nodes.add(queue.poll());
    }

    return nodes;
  }

  private void addNodeToMapping(
    TreeNodeWithCol nodeWithCol,
    Map<Integer, List<Integer>> colToValues
  ) {
    TreeNode node = nodeWithCol.node;
    int column = nodeWithCol.column;
    if (!colToValues.containsKey(column)) {
      colToValues.put(column, new ArrayList<Integer>());
    }
    colToValues.get(column).add(node.val);
  }
}
