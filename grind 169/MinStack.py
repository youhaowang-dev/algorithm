# Stack, Design
# Amazon 12 Bloomberg 8 Expedia 4 Microsoft 3 Apple 3 Adobe 4 Facebook 3 Salesforce 3 Walmart Global Tech 2 Oracle 2
# Arcesium 2 VMware 5 Goldman Sachs 5 Google 4 Capital One 3 Lyft 2 Cisco 2 Yahoo 2 Paypal 2 Coupang 2 Airtel 2 Uber
# Snapchat Zenefits

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); # return -3
# minStack.pop();
# minStack.top();    # return 0
# minStack.getMin(); # return -2

# IMPORANT getMin only needs to return the min, it does not remove items from the MinStack.
class MinStack:

    def __init__(self):
        self.stack = deque()  # Tuple[val, min_val] min can only decreasing

    def push(self, val: int) -> None:
        if self.stack:
            min_val = min(val, self.getMin())
            self.stack.append((val, min_val))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
