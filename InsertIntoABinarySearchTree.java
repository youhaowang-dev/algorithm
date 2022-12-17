// Tree, Binary Search Tree, Binary Tree
// LinkedIn 3 Amazon 3 Google 2 Goldman Sachs 2
// https://leetcode.com/problems/insert-into-a-binary-search-tree/
// You are given the root node of a binary search tree (BST) and a value to insert into the tree.
// Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
// Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

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
class InsertIntoABinarySearchTree {

  public TreeNode insertIntoBST(TreeNode root, int val) {
    if (root == null) {
      return new TreeNode(val);
    }

    if (root.val > val) {
      root.left = this.insertIntoBST(root.left, val);
    } else {
      root.right = this.insertIntoBST(root.right, val);
    }

    return root;
  }
}
