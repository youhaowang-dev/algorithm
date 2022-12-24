class Stack {

  private class Node {

    int val;
    Node next;

    public Node(int val, Node next) {
      this.val = val;
      this.next = next;
    }
  }

  private Node current;

  public Stack() {
    this.current = null;
  }

  public void push(int value) {
    Node node = new Node(value, this.current);
    this.current = node;
  }

  public int peek() {
    return this.current.val;
  }

  public void pop() {
    this.current = this.current.next;
  }
}
