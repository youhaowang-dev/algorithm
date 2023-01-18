# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Amazon 5 Adobe 4 Bloomberg 3 Apple 2 Facebook 2 Google 7 LinkedIn 6 Uber 3 Microsoft 2 Yandex 2 VMware 2 Capital One 4 Arista Networks 3 Yahoo 2 Goldman Sachs 2
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Two trees are a mirror reflection of each other if:

# Their two roots have the same value.
# The right subtree of each tree is a mirror reflection of the left subtree of the other tree.
class SymmetricTree:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isSymmetricHelper(root, root)

    def isSymmetricHelper(self, node1: TreeNode, node2: TreeNode) -> bool:
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        node_val_same = node1.val == node2.val

        return (
            node_val_same
            and self.isSymmetricHelper(node1.right, node2.left)
            and self.isSymmetricHelper(node1.left, node2.right)
        )


class SymmetricTree2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque()
        queue.append((root, root))
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue  # important, donot return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            queue.append((node1.right, node2.left))
            queue.append((node1.left, node2.right))

        return True
