// two stack are more flexible for followup
class MinStackWithTwoStacks {

  // the regular stack
  private Stack<Integer> stack = new Stack<>();
  // track the mins along with the main stack
  private Stack<Integer> minStack = new Stack<>();

  public MinStack() {}

  public void push(int x) {
    stack.push(x);
    if (minStack.isEmpty()) {
      minStack.push(x);
    } else {
      minStack.push(Math.min(x, this.minStack.peek()));
    }
  }

  public void pop() {
    minStack.pop();
    stack.pop();
  }

  public int top() {
    return stack.peek();
  }

  public int getMin() {
    return minStack.peek();
  }
}
