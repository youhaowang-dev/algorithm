// Tree, Depth-First Search, Binary Tree
// Facebook 2 Microsoft 2 Amazon 2 LinkedIn
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/
// Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes,
// p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

// According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a
// binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)".
// A descendant of a node x is a node y that is on the path from node x to some leaf node.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// p and q may not be in the tree
class LowestCommonAncestorOfABinaryTreeII {

  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    Map<TreeNode, TreeNode> childToParent = new HashMap<>();
    this.buildChildToParent(root, childToParent);
    Set<TreeNode> visited = new HashSet<>();
    while (p != null) {
      visited.add(p);
      p = childToParent.get(p);
    }
    while (q != null) {
      if (visited.contains(q)) {
        return q;
      }
      visited.add(q);
      q = childToParent.get(q);
    }

    return null;
  }

  private void buildChildToParent(
    TreeNode root,
    Map<TreeNode, TreeNode> childToParent
  ) {
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    while (!queue.isEmpty()) {
      List<TreeNode> nodes = this.getCurrentLevelNode(queue);
      for (TreeNode node : nodes) {
        if (node.left != null) {
          queue.offer(node.left);
          childToParent.put(node.left, node);
        }
        if (node.right != null) {
          queue.offer(node.right);
          childToParent.put(node.right, node);
        }
      }
    }
  }

  private List<TreeNode> getCurrentLevelNode(Queue<TreeNode> queue) {
    List<TreeNode> nodes = new ArrayList<>();
    while (!queue.isEmpty()) {
      nodes.add(queue.poll());
    }

    return nodes;
  }

  private void buildChildToParent(
    TreeNode root,
    Map<TreeNode, TreeNode> childToParent
  ) {
    if (root.left != null) {
      childToParent.put(root.left, root);
      this.buildChildToParent(root.left, childToParent);
    }
    if (root.right != null) {
      childToParent.put(root.right, root);
      this.buildChildToParent(root.right, childToParent);
    }
  }
}
