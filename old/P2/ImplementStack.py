# https://www.lintcode.com/problem/495/description
# Implement a stack. You can use any data structure inside a stack except stack itself to implement it.


class Node:
    def __init__(self, x: int):
        self.x = x
        self.next = None


class Stack:
    def __init__(self):
        self.peek = None

    def push(self, x: int) -> None:
        node = Node(x)
        node.next = self.peek
        self.peek = node

    def pop(self) -> int:
        self.peek = self.peek.next

    def top(self) -> int:
        return self.peek.x

    def isEmpty(self) -> bool:
        return self.peek is None
