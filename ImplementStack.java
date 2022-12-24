// https://www.lintcode.com/problem/495/description
// Implement a stack. You can use any data structure inside a stack except stack itself to implement it.
public class Stack {

  Node peek; // IMPORTANT: put it here; not in the node class

  public Stack() {
    this.peek = null;
  }

  private class Node {

    int x;
    Node next;

    public Node(int x, Node next) {
      this.x = x;
      this.next = next;
    }
  }

  public void push(int x) {
    Node node = new Node(x, this.peek);
    this.peek = node;
  }

  public void pop() {
    this.peek = this.peek.next;
  }

  public int top() {
    return this.peek.x;
  }

  public boolean isEmpty() {
    return this.peek == null;
  }
}
