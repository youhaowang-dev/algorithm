// Tree, Depth-First Search, Binary Search Tree, Binary Tree
// Microsoft 3 Arista Networks 3 Facebook 5 Google 4 Adobe 3 Apple 2

// Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

// The successor of a node p is the node with the smallest key greater than p.val.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class InorderSuccessorInBST {

  // tree is BST, so we can do binary search for a node where its value is greater than target
  // and it should be as small as possible
  public TreeNode inorderSuccessor(TreeNode root, TreeNode target) {
    TreeNode successor = null;
    TreeNode current = root;
    int targetVal = target.val;
    while (current != null) {
      int currentVal = current.val;
      if (targetVal == currentVal) {
        current = current.right; // depend on tree definition
      }

      if (targetVal > currentVal) {
        current = current.right;
      }

      if (targetVal < currentVal) {
        // current might be the node we are looking for, so record it
        successor = current;
        current = current.left;
      }
    }

    return successor;
  }
}
