// Hash Table, Linked List
// Amazon 23 Facebook 8 Bloomberg 6 Microsoft 3 Apple 3 Adobe 4 Google 3 ByteDance 2 Qualtrics 8 eBay 7 VMware 4 Nvidia 3 Yahoo 3 Oracle 3 Walmart Global Tech 3 ServiceNow 2 Intel 2 Uber Wix
// https://leetcode.com/problems/copy-list-with-random-pointer/

// A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

// Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

// For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

// Return the head of the copied linked list.

// The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

// val: an integer representing Node.val
// random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
// Your code will only be given the head of the original linked list.

/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class CopyListWithRandomPointer {

  // like doing a list traversal but in two ways
  // regular next and random next
  // connect the next and random during traversal and
  public Node copyRandomList(Node head) {
    if (head == null) {
      return null;
    }

    // init
    Node oldNode = head;
    Node newNode = new Node(oldNode.val);
    HashMap<Node, Node> oldToNew = new HashMap<>(); // helps the random thing
    oldToNew.put(oldNode, newNode);

    while (oldNode != null) {
      // connect
      newNode.next = this.getNewNode(oldToNew, oldNode.next);
      newNode.random = this.getNewNode(oldToNew, oldNode.random);

      newNode = newNode.next;
      oldNode = oldNode.next;
    }
    return oldToNew.get(head);
  }

  // create copy when needed
  private Node getNewNode(HashMap<Node, Node> oldToNew, Node node) {
    if (node == null) {
      return null;
    }

    if (!oldToNew.containsKey(node)) {
      Node copy = new Node(node.val, null, null);
      oldToNew.put(node, copy);
    }

    return oldToNew.get(node);
  }

  // O(1) space but will modify input
  // Inserting the cloned node just next to the original node.
  // If A->B->C is the original linked list,
  // Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
  public Node copyRandomList(Node head) {
    if (head == null) {
      return null;
    }

    this.doubleNodes(head);
    this.linkRandoms(head);

    // separate node and copy
    // aa'bb'cc' => abc and a'b'c'
    Node oldHead = head;
    Node newHead = head.next;
    Node head_old = head.next;
    while (oldHead != null) {
      oldHead.next = oldHead.next.next;
      newHead.next = (newHead.next != null) ? newHead.next.next : null;
      oldHead = oldHead.next;
      newHead = newHead.next;
    }
    return head_old;
  }

  // abc => aa'bb'cc'
  private void doubleNodes(Node current) {
    while (current != null) {
      Node newNode = new Node(current.val);

      newNode.next = current.next;
      current.next = newNode;
      current = newNode.next;
    }
  }

  private void linkRandoms(Node current) {
    while (current != null) {
      if (current.random == null) {
        current.next.random = null;
      } else {
        // connect copy to copy
        current.next.random = current.random.next;
      }
      current = current.next.next;
    }
  }
}
