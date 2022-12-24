// Stack, Design, Queue
// Amazon 4 Microsoft 2 Bloomberg 2 Google 2 Twilio 3 Paypal 3 Apple 2 Salesforce 2 Goldman Sachs 2
// https://leetcode.com/problems/implement-stack-using-queues/description/

// Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

// Implement the MyStack class:

// void push(int x) Pushes element x to the top of the stack.
// int pop() Removes the element on the top of the stack and returns it.
// int top() Returns the element on the top of the stack.
// boolean empty() Returns true if the stack is empty, false otherwise.
// Notes:

// You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
// Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

// Example 1:

// Input
// ["MyStack", "push", "push", "top", "pop", "empty"]
// [[], [1], [2], [], [], []]
// Output
// [null, null, null, 2, 2, false]

// Explanation
// MyStack myStack = new MyStack();
// myStack.push(1);
// myStack.push(2);
// myStack.top(); // return 2
// myStack.pop(); // return 2
// myStack.empty(); // return False

// either pop or push will be O(n) as queue is FIFO
// assumption: All the calls to pop and top are valid.
class MyStack {

  Queue<Integer> queue;
  Integer peek;

  public MyStack() {
    this.queue = new LinkedList();
    this.peek = null;
  }

  // enqueue and update peek
  public void push(int x) {
    this.peek = x;
    this.queue.offer(x);
  }

  // get the last element in queue and put back the rest
  // update peek
  public int pop() {
    int count = this.queue.size();

    int val = Integer.MIN_VALUE;
    while (count > 0) {
      val = this.queue.poll();
      count--;
      if (count != 0) {
        System.out.println(val);
        // not val put back
        this.queue.offer(val);
      }
      if (count == 1) {
        this.peek = val;
      }
    }

    return val;
  }

  public int top() {
    return this.peek;
  }

  public boolean empty() {
    return this.queue.isEmpty();
  }
}
