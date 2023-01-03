// Tree, Depth-First Search, Binary Search Tree, Binary Tree
// Amazon 7 Adobe 3 Facebook 2 LinkedIn 2 Bloomberg 2 Apple 5 Google 2 Microsoft 2 Uber 2 Walmart Global Tech 4 Oracle 2 Reddit 2 Twitter
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

// Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
// According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
// as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

class LowestCommonAncestorofaBinarySearchTree {

  //     6
  //    / \
  //   2   8
  //  / \
  // 0   4
  //    / \
  //   3   5
  // find LCA for 0 and 5
  // both are smaller, so go to left,
  // now 2 is between 0 and 5, we found the LCA

  // evaluate the root node, if both are in left or right, move root until not
  // when not, the root is the LCA
  // can use an example to prove
  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    int pVal = p.val;
    int qVal = q.val;

    TreeNode current = root; // current parent

    while (current != null) {
      int currentVal = current.val;

      if (pVal > currentVal && qVal > currentVal) {
        // both in right subtree, drop left subtree
        current = current.right;
        continue;
      }
      if (pVal < currentVal && qVal < currentVal) {
        // both in left subtree, drop right subtree
        current = current.left;
        continue;
      }
      // one in left subtree and one in right subtree, so this is the LCA
      return current;
    }

    return null;
  }

  // recursion uses BST property
  // binary search an answer
  // time n space n
  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    int rootVal = root.val;
    int pVal = p.val;
    int qVal = q.val;

    if (pVal > rootVal && qVal > rootVal) {
      // both in right subtree, drop left subtree
      return lowestCommonAncestor(root.right, p, q);
    }
    if (pVal < rootVal && qVal < rootVal) {
      // both in left subtree, drop right subtree
      return lowestCommonAncestor(root.left, p, q);
    }
    // one in left subtree and one in right subtree, so this is the LCA
    return root;
  }
}
