// https://www.lintcode.com/problem/492/
// Implement a Queue by linked list. Support the following basic methods:

// enqueue(item). Put a new item in the queue.
// dequeue(). Move the first item out of the queue, return it. If the queue is empty, returned. -1.

public class MyQueue {

  private Node first;
  private Node last;

  public MyQueue() {
    this.first = null;
    this.last = null;
  }

  private class Node {

    int val;
    Node next;

    public Node(int val, Node next) {
      this.val = val;
      this.next = next;
    }
  }

  public void enqueue(int item) {
    Node newNode = new Node(item, null);
    if (this.first == null) {
      this.first = newNode;
      this.last = this.first;
    } else {
      this.last.next = newNode;
      this.last = this.last.next;
    }
  }

  public int dequeue() {
    if (this.first == null) {
      return -1;
    }
    int firstVal = this.first.val;
    this.first = this.first.next;

    return firstVal;
  }
}
