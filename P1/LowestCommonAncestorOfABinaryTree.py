# Tree, Depth-First Search, Binary Tree
# Facebook 24 Amazon 22 Bloomberg 8 Microsoft 4 Karat 4 Google 2 LinkedIn 2 Oracle 2 Yahoo 2 Splunk 2 Qualcomm 2 TikTok 2 Samsung 2
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
# two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# p and q will exist in the tree.

from ast import Dict
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# bfs
class LowestCommonAncestorOfABinaryTree:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return None

        child_to_parent = self.get_child_to_parent(root)

        visited = set()
        while p:
            visited.add(p)
            p = child_to_parent.get(p)
        while q:
            if q in visited:
                return q
            else:
                q = child_to_parent.get(q)

        return None

    def get_child_to_parent(self, root) -> Dict["TreeNode", "TreeNode"]:
        child_to_parent = dict()
        queue = deque()
        queue.append(root)
        while queue:
            parent = queue.popleft()
            if parent.left:
                queue.append(parent.left)
                child_to_parent[parent.left] = parent
            if parent.right:
                queue.append(parent.right)
                child_to_parent[parent.right] = parent

        return child_to_parent


# divide and conquer, search LCA in subtrees
# if found both in subtree, return the root
# if found one, return the one
# if found none, return null
class LowestCommonAncestorOfABinaryTree2:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return None

        if root == p or root == q:
            return root

        ancestor_from_left = self.lowestCommonAncestor(root.left, p, q)
        ancestor_from_right = self.lowestCommonAncestor(root.right, p, q)
        # both subtrees have found the target
        if ancestor_from_left and ancestor_from_right:
            return root
        # one subtree found the target
        if ancestor_from_left:
            return ancestor_from_left
        # one subtree found the target
        if ancestor_from_right:
            return ancestor_from_right

        return None
