// Linked List Stack Design Doubly-Linked List Ordered Set
// LinkedIn 9 Bloomberg 4 Amazon 3 Lyft 2 Apple 2 VMware 3 Yandex 3 Microsoft 2 Facebook 2 Pure Storage 2 Twitter 2 Goldman Sachs 2
// https://leetcode.com/problems/max-stack/

// Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

// Implement the MaxStack class:

// MaxStack() Initializes the stack object.
// void push(int x) Pushes element x onto the stack.
// int pop() Removes the element on top of the stack and returns it.
// int top() Gets the element on the top of the stack without removing it.
// int peekMax() Retrieves the maximum element in the stack without removing it.
// int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
// You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.

// Example 1:

// Input
// ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
// [[], [5], [1], [5], [], [], [], [], [], []]
// Output
// [null, null, null, null, 5, 5, 1, 5, 1, 5]

// Explanation
// MaxStack stk = new MaxStack();
// stk.push(5);   // [5] the top of the stack and the maximum number is 5.
// stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
// stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
// stk.top();     // return 5, [5, 1, 5] the stack did not change.
// stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
// stk.top();     // return 1, [5, 1] the stack did not change.
// stk.peekMax(); // return 5, [5, 1] the stack did not change.
// stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
// stk.top();     // return 5, [5] the stack did not change.

// Lazy Deletion
// we are not urgent to delete the popped element. Instead, we just memorize the ID of this element.
// Next time, when we are going to peek or pop the top of our heap or stack, we first check whether the top is already removed from the other data structure by checking its ID.
//
// Time Complexity:
// push: O(logN), it costs O(logN) to add an element to heap and O(1) to add an it to stack.
// The amortized time complexity of operations caused by a single pop/popMax call is O(logN).
// For a pop call, we first remove the last element in stack and add its ID to removed in O(1),
// and result in a deletion of the top element in heap in the future (when peekMax or popMax is called),
// which has a time complexity of logN. Similarly, popMax needs O(logN) immediately and O(1) in the operations later.
// Note that because we lazy-update the two data structures, future operations might never happen in some cases.
// But even in the worst cases, the upper bound of the amortized time complexity is still only O(logN).
// top: O(1), excluding the time cost related to popMax calls we discussed above.
// peekMax: O(logN), excluding the time cost related to pop calls we discussed above.
// Space Complexity: O(N), the maximum size of the heap, stack, and removed.

class MaxStack {

  private Stack<int[]> stack;
  private Queue<int[]> maxHeap;
  private Set<Integer> removed;
  private int sequentialID;

  public MaxStack() {
    this.stack = new Stack<>();
    // [value, sequentialID]
    this.maxHeap =
      new PriorityQueue<>((a, b) -> {
        if (b[0] - a[0] == 0) {
          return b[1] - a[1];
        } else {
          return b[0] - a[0];
        }
      });
    this.removed = new HashSet<>();
    this.sequentialID = 0;
  }

  public void push(int x) {
    this.stack.add(new int[] { x, this.sequentialID });
    this.maxHeap.add(new int[] { x, this.sequentialID });
    this.sequentialID++;
  }

  public int pop() {
    while (removed.contains(this.stack.peek()[1])) {
      this.stack.pop();
    }
    int[] top = this.stack.pop();
    this.removed.add(top[1]);
    return top[0];
  }

  public int top() {
    while (removed.contains(this.stack.peek()[1])) {
      this.stack.pop();
    }
    return this.stack.peek()[0];
  }

  public int peekMax() {
    while (this.removed.contains(this.maxHeap.peek()[1])) {
      this.maxHeap.poll();
    }
    return this.maxHeap.peek()[0];
  }

  public int popMax() {
    while (this.removed.contains(this.maxHeap.peek()[1])) {
      this.maxHeap.poll();
    }
    int[] top = this.maxHeap.poll();
    this.removed.add(top[1]);
    return top[0];
  }
}
