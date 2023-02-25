# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Amazon 7 Google 3 Apple 3 Microsoft 2 LinkedIn 9 American Express 6 Facebook 4 Bloomberg 4 Adobe 3 Uber 2 Yandex 2 Oracle 2
# https://leetcode.com/problems/same-tree/

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive
class SameTree:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not q or not p:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# iterative, use tuple as pair
class SameTree:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        queue = deque()
        queue.append((p, q))
        while queue:
            node1, node2 = queue.popleft()
            if not self.same_node(node1, node2):
                return False

            if node1 and node2:
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))

        return True

    def same_node(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        if node1.val != node2.val:
            return False

        return True
