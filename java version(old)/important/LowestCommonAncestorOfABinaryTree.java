// Tree, Depth-First Search, Binary Tree
// Facebook 24 Amazon 22 Bloomberg 8 Microsoft 4 Karat 4 Google 2 LinkedIn 2 Oracle 2 Yahoo 2 Splunk 2 Qualcomm 2 TikTok 2 Samsung 2
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
// Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

// According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
// two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

// p and q will exist in the tree.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class LowestCommonAncestorOfABinaryTree {

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

  // search LCA in subtrees
  // if found both, return current root
  // if found one, return the one
  // if found none, return null
  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    // exut
    if (root == null) {
      return null;
    }
    if (root == p || root == q) {
      return root;
    }

    // divide
    TreeNode ancestor1 = this.lowestCommonAncestor(root.left, p, q);
    TreeNode ancestor2 = this.lowestCommonAncestor(root.right, p, q);

    // merge subtree results
    if (ancestor1 != null && ancestor2 != null) {
      return root;
    }
    if (ancestor1 != null) {
      return ancestor1;
    }
    if (ancestor2 != null) {
      return ancestor2;
    }

    return null;
  }
}
