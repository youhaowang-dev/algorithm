# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Microsoft 3 Arista Networks 3 Facebook 4 Google 4 Adobe 3 Apple 2 Amazon 7 Bloomberg 3 Walmart Global Tech 2 Pocket Gems
# https://leetcode.com/problems/inorder-successor-in-bst/description/

# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
# If the given node has no in-order successor in the tree, return null.

# The successor of a node p is the node with the smallest key greater than p.val.

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# brute force: build inorder iterator for the tree, find target, get next node

# binary search kth
class InorderSuccessorInBST:
    def inorderSuccessor(self, root: TreeNode, target: TreeNode) -> Optional[TreeNode]:
        successor = None
        current = root
        target_val = target.val
        while current:
            current_val = current.val
            if current_val == target_val:
                current = current.right  # bst definition by question
            if current_val > target_val:
                successor = current  # record it as it could be the answer
                current = current.left
            if current_val < target_val:
                current = current.right

        return successor


# binary search iterative
class InorderSuccessorInBST2:
    def inorderSuccessor(self, root: TreeNode, target: TreeNode) -> Optional[TreeNode]:
        if not root or not target:
            return None

        if target.val >= root.val:
            return self.inorderSuccessor(root.right, target)
        else:
            successor = self.inorderSuccessor(root.left, target)
            return successor if successor else root
