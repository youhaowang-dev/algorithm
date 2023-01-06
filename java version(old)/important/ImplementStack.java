// https://www.lintcode.com/problem/495/description
// Implement a stack. You can use any data structure inside a stack except stack itself to implement it.
public class Stack {

  Node peek;

  public Stack() {
    this.peek = null;
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

  private class Node {

    public int x;
    public Node next;

    public Node(int x, Node next) {
      this.x = x;
      this.next = next;
    }
  }
}
