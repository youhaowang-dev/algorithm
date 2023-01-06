# Stack, Design, Queue
# Amazon 4 Microsoft 2 Bloomberg 2 Google 2 Twilio 3 Paypal 3 Apple 2 Salesforce 2 Goldman Sachs 2
# https://leetcode.com/problems/implement-stack-using-queues/description/

# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(x) Pushes element x to the top of the stack.
# pop() Removes the element on the top of the stack and returns it.
# top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack()
# myStack.push(1)
# myStack.push(2)
# myStack.top() # return 2
# myStack.pop() # return 2
# myStack.empty() # return False

# either pop or push will be O(n) as queue is FIFO
# assumption: All the calls to pop and top are valid.

# Follow-up: Can you implement the stack using only one queue?
from collections import deque


# only use queue FIFO APIs of deque, append and popleft
class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.rotateExceptLast()

    # mimic stack push result by "rotating all elements"
    def rotateExceptLast(self) -> None:
        queue_size = len(self.queue)
        for _ in range(1, queue_size):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


class MyStack2:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        queue_size = len(self.queue)
        val = float("-inf")
        for i in range(0, queue_size):
            val = self.queue.popleft()
            isLastIn = i == queue_size - 1
            if not isLastIn:
                self.queue.append(val)

        return val

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue
