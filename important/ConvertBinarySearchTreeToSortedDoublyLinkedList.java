// Linked List, Stack, Tree, Depth-First Search, Binary Search Tree, Binary Tree, Doubly-Linked List
// Facebook 2 Microsoft 4 Amazon 3 ByteDance 3 Lyft 2 Google 4 Bloomberg 2 Expedia 2 TikTok 2
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

// Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

// You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

// We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

// Example 1:
// Input: root = [4,2,5,1,3]
// Output: [1,2,3,4,5]
// Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

// Example 2:
// Input: root = [2,1,3]
// Output: [1,2,3]

/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/

class ConvertBinarySearchTreeToSortedDoublyLinkedList {

  private class InorderIterator {

    private Stack<Node> stack;

    public InorderIterator(Node node) {
      this.stack = new Stack<Node>();
      this.pushLefts(node);
    }

    public boolean hasNext() {
      return !this.stack.isEmpty();
    }

    public Node getNext() {
      if (!this.hasNext()) {
        return null;
      }

      Node node = this.stack.pop();
      this.pushLefts(node.right);

      return node;
    }

    private void pushLefts(Node node) {
      while (node != null) {
        this.stack.push(node);
        node = node.left;
      }
    }
  }

  public Node treeToDoublyList(Node root) {
    if (root == null) {
      return null;
    }

    InorderIterator iterator = new InorderIterator(root);
    Node first = iterator.getNext();
    Node current = first;
    while (iterator.hasNext()) {
      Node nextNode = iterator.getNext();
      current.right = nextNode;
      nextNode.left = current;
      current = nextNode;
    }
    // make the doubly linked list circular
    current.right = first;
    first.left = current;

    return first;
  }
}
