class MinStackWithCustomStack {

  private CustomMinStack stack;

  public MinStackWithCustomStack() {
    this.stack = new CustomMinStack();
  }

  public void push(int value) {
    // IMPORANT: init min
    int min;
    if (this.stack.isEmpty()) {
      min = value;
    } else {
      min = Math.min(this.getMin(), value);
    }
    Pair pair = new Pair(value, min);
    this.stack.push(pair);
  }

  public void pop() {
    this.stack.pop();
  }

  public int top() {
    return this.stack.peek().value;
  }

  public int getMin() {
    return this.stack.peek().min;
  }

  private class Pair {

    private int value;
    private int min;

    public Pair(int value, int min) {
      this.value = value;
      this.min = min;
    }
  }

  private class CustomMinStack {

    private class Node {

      Pair pair;
      Node next;

      public Node(Pair pair, Node next) {
        this.pair = pair;
        this.next = next;
      }
    }

    private Node current;

    public CustomMinStack() {
      this.current = null;
    }

    public void push(Pair pair) {
      Node node = new Node(pair, this.current);
      this.current = node;
    }

    public Pair peek() {
      return this.current.pair;
    }

    public void pop() {
      this.current = this.current.next;
    }

    public boolean isEmpty() {
      return this.current == null;
    }
  }
}
