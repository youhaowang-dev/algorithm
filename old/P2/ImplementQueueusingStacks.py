# Stack, Design, Queue
# Amazon 4 Goldman Sachs 3 eBay 2 Docusign 2 Microsoft 2 Oracle 2 Apple 6 ByteDance 3 VMware 3 Bloomberg 2 Google 2
# Qualcomm 2 Splunk 2 DE Shaw 2
# https://leetcode.com/problems/implement-queue-using-stacks/description/

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support
# all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size,
# and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or
# deque (double-ended queue) as long as you use only a stack's standard operations.

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); # queue is: [1]
# myQueue.push(2); # queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); # return 1
# myQueue.pop(); # return 1, queue is [2]
# myQueue.empty(); # return false

# All the calls to pop and peek are valid.

# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity?
# In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

# only use stack LIFO APIs of deque; append==push, pop==pop, do not use popleft()
# two stacks, one hold the pushes, the other one will be populated when pop is called and when it is empty
# time: O(1) average because we transfer at most N elements from one stack to another
class MyQueue:
    def __init__(self):
        self.in_stack = deque()
        self.out_stack = deque()

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            self._move_in_to_out()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            self._move_in_to_out()
        return self.out_stack[-1]

    def _move_in_to_out(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0
