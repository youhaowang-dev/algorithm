# https://www.lintcode.com/problem/492/
# Implement a Queue by linked list. Support the following basic methods:

# enqueue(item). Put a new item in the queue.
# dequeue(). Move the first item out of the queue, return it. If the queue is empty, returned. -1.


class Node:
    def __init__(self, val: int):  #  -> Node not work in python 3
        self.val = val
        self.next = None


class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item: int) -> None:
        newNode = Node(item)
        if self.first == None:
            self.first = newNode
            self.last = self.first
        else:
            self.last.next = newNode
            self.last = self.last.next

    def dequeue(self) -> int:
        if self.first == None:
            return -1

        firstVal = self.first.val
        self.first = self.first.next

        return firstVal
