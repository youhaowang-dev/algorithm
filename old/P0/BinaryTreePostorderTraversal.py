# Stack, Tree, Depth-First Search, Binary Tree
# Facebook 2 Amazon 2 Apple 2 TuSimple 2 Bloomberg 2
# https://leetcode.com/problems/binary-tree-postorder-traversal/


from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreePostorderTraversal:
    def postorderTraversal(self, root):
        result = list()
        stack = deque()
        stack.append((root, False))  # (node, visited)
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    result.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return result


# recursion
class BinaryTreePostorderTraversal2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result

        self.postorderTraversalHelper(root, result)

        return result

    def postorderTraversalHelper(
        self, root: Optional[TreeNode], result: List[int]
    ) -> None:
        if not root:
            return

        self.postorderTraversalHelper(root.left, result)
        self.postorderTraversalHelper(root.right, result)
        result.append(root.val)


# divide and conquer
class BinaryTreePostorderTraversal3:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result

        left_result = self.postorderTraversal(root.left)
        right_result = self.postorderTraversal(root.right)
        result.extend(left_result)
        result.extend(right_result)
        result.append(root.val)

        return result
