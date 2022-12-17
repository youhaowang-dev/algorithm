// Tree, Binary Search Tree, Binary Tree
// Adobe 3 Amazon 2 Apple 2 Microsoft 5 Oracle 5 Google 3 LinkedIn 2 Bloomberg 2
// https://leetcode.com/problems/delete-node-in-a-bst/

// Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

// Basically, the deletion can be divided into two stages:

// Search for a node to remove.
// If the node is found, delete the node.

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
class DeleteNodeInABST {

  // first we need to find the node
  // Then there are three possible situations here :
  // if node is leaf, just delete it
  // else node has right, the node can be replaced by next inorder node, then we need to delete the inorder node in the subtree.
  //          This replace & delete should be done recursively.
  // else node has left, the node can be replaced by previous inorder node, then we need to delete the inorder node in th
  //          This replace & delete should be done recursively.
  public TreeNode deleteNode(TreeNode root, int key) {
    if (root == null) {
      return null;
    }

    if (key > root.val) {
      root.right = this.deleteNode(root.right, key);
    }

    if (key < root.val) {
      root.left = this.deleteNode(root.left, key);
    }

    if (key == root.val) {
      if (root.left == null && root.right == null) {
        return null;
      } else if (root.left != null) {
        TreeNode leftSubtreeMax = this.getSubtreeMax(root.left);
        root.val = leftSubtreeMax.val;
        root.left = this.deleteNode(root.left, root.val);
      } else if (root.right != null) {
        TreeNode rightSubtreeMin = this.getSubtreeMin(root.right);
        root.val = rightSubtreeMin.val;
        root.right = this.deleteNode(root.right, root.val);
      }
    }

    return root;
  }

  private TreeNode getSubtreeMax(TreeNode node) {
    TreeNode max = node;
    while (max.right != null) {
      max = max.right;
    }

    return max;
  }

  private TreeNode getSubtreeMin(TreeNode node) {
    TreeNode min = node;
    while (min.left != null) {
      min = min.left;
    }

    return min;
  }
}
