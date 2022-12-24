// Stack, Design
// Amazon 12 Bloomberg 8 Expedia 4 Microsoft 3 Apple 3 Adobe 4 Facebook 3 Salesforce 3 Walmart Global Tech 2 Oracle 2 Arcesium 2 VMware 5 Goldman Sachs 5 Google 4 Capital One 3 Lyft 2 Cisco 2 Yahoo 2 Paypal 2 Coupang 2 Airtel 2 Uber Snapchat Zenefits

// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// Implement the MinStack class:

// MinStack() initializes the stack object.
// void push(int val) pushes the element val onto the stack.
// void pop() removes the element on the top of the stack.
// int top() gets the top element of the stack.
// int getMin() retrieves the minimum element in the stack.
// You must implement a solution with O(1) time complexity for each function.

// Example 1:

// Input
// ["MinStack","push","push","push","getMin","pop","top","getMin"]
// [[],[-2],[0],[-3],[],[],[],[]]

// Output
// [null,null,null,null,-3,null,0,-2]

// Explanation
// MinStack minStack = new MinStack();
// minStack.push(-2);
// minStack.push(0);
// minStack.push(-3);
// minStack.getMin(); // return -3
// minStack.pop();
// minStack.top();    // return 0
// minStack.getMin(); // return -2

class MinStack {

  // IMPORANT: Make sure that you read the question carefully. The getMin(...) operation only needs to return the value of the minimum, it does not remove items from the MinStack.

  // pair the value and the min value, push and pop them together
  // push 3,2,1,4
  // peak 3, min 3
  // peak 2, min 2
  // peak 1, min 1
  // peak 4, min 1
  private class Pair {

    private int value;
    private int min;

    public Pair(int value, int min) {
      this.value = value;
      this.min = min;
    }
  }

  private Stack<Pair> stack;

  public MinStack() {
    this.stack = new Stack<>();
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
}
