// Tree, Binary Search Tree, Binary Tree
// Microsoft 4 Arista Networks 2 Facebook 2 Google 3 Bloomberg 3 Amazon 2 Akamai 2
// https://leetcode.com/problems/inorder-successor-in-bst-ii/
// Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

// The successor of a node is the node with the smallest key greater than node.val.

// You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

// class Node {
//     public int val;
//     public Node left;
//     public Node right;
//     public Node parent;
// }

// Successor and Predecessor
// Successor = "after node", i.e. the next node in the inorder traversal, or the smallest node after the current one.

// Predecessor = "before node", i.e. the previous node in the inorder traversal, or the largest node before the current one.
class InorderSuccessorInBSTII {

  // There are two possible situations here :
  // Node has a right child, so the min node of the right subtree is the successor.
  // Node has no right child, so the successor is in the upper tree.
  //       find the first parent node where its left is the current pointer, the parent is the successor
  public Node inorderSuccessor(Node node) {
    if (node == null) {
      return null;
    }

    if (node.right != null) {
      Node minNode = node.right;
      while (minNode.left != null) {
        minNode = minNode.left;
      }

      return minNode;
    }

    Node successor = null;
    Node current = node;
    while (current != null) {
      Node parent = current.parent;
      if (parent == null) {
        return null;
      }
      if (parent.left == current) {
        return parent;
      }
      current = parent;
    }

    return successor;
  }
}
