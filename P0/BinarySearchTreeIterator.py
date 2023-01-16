# Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator
# Facebook 7 Media.net 7 Microsoft 4 Amazon 4 Google 3 Bloomberg 3 Salesforce 2 Twilio 2
# https://leetcode.com/problems/binary-search-tree-iterator/

# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part
# of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        self.push_roots(root)

    def next(self) -> int:
        node = self.stack.pop()
        self.push_roots(node.right)

        return node.val

    def hasNext(self) -> bool:
        return self.stack

    def push_roots(self, root: Optional[TreeNode]):
        while root:
            self.stack.append(root)
            root = root.left
