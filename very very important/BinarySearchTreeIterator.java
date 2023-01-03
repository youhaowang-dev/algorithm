// Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator
// Facebook 7 Media.net 7 Microsoft 4 Amazon 4 Google 3 Bloomberg 3 Salesforce 2 Twilio 2

// Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

// BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
// boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
// int next() Moves the pointer to the right, then returns the number at the pointer.
// Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

// You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

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
class BSTIterator {

  private Stack<TreeNode> stack;

  public BSTIterator(TreeNode root) {
    this.current = root;
    this.stack = new Stack<TreeNode>();
    this.pushLefts(root);
  }

  public int next() {
    if (!this.stack.isEmpty()) {
      TreeNode node = this.stack.pop();
      this.pushLefts(node.right);

      return node.val;
    }

    return Integer.MIN_VALUE;
  }

  private void pushLefts(TreeNode node) {
    while (node != null) {
      this.stack.push(node);
      node = node.left;
    }
  }

  public boolean hasNext() {
    return !this.stack.isEmpty();
  }
}
