# String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Search Tree, Binary Tree
# Amazon 3 LinkedIn 3 Microsoft 3 Nutanix 3 Facebook 4 Splunk 3 Apple 2 Uber 2
# https://leetcode.com/problems/serialize-and-deserialize-bst/

# Serialization is converting a data structure or object into a sequence of bits so that it can be stored
# in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in
# the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be
# serialized to a string, and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Example 1:
# Input: root = [2,1,3]
# Output: [2,1,3]
# Example 2:
# Input: root = []
# Output: []


from ast import List
from collections import deque
import collections
from typing import Deque, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# O( N ) since each val run build once
class Codec:
    DELIMITER = ","
    MIN = -(2**31)
    MAX = 2**31 - 1

    def serialize(self, root: Optional[TreeNode]) -> str:
        node_vals = list()

        self.get_node_vals(root, node_vals)
        node_val_strs = map(str, node_vals)

        return self.DELIMITER.join(node_val_strs)

    def get_node_vals(self, node: Optional[TreeNode], node_vals: List[int]) -> None:
        if not node:
            return

        node_vals.append(node.val)
        self.get_node_vals(node.left, node_vals)
        self.get_node_vals(node.right, node_vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = deque(map(int, data.split(self.DELIMITER)))
        return self.build_tree(nodes, self.MIN, self.MAX)

    def build_tree(self, nodes: Deque[int], min: int, max: int) -> Optional[TreeNode]:
        if not nodes:
            return None

        # dont pop it now because some branches are invalid and should return None
        node_val = nodes[0]
        if node_val > max:
            return None
        # pop now
        nodes.popleft()

        root = TreeNode(node_val)
        root.left = self.build_tree(nodes, min, node_val)
        root.right = self.build_tree(nodes, node_val, max)

        return root


# O( N ) since each val run build once
class Codec2:
    DELIMITER = ","
    MIN = -(2**31)
    MAX = 2**31 - 1

    def serialize(self, root):
        vals = list()

        def preorder(node):
            if node:
                vals.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)

        return self.DELIMITER.join(map(str, vals))

    def deserialize(self, data):
        if not data:
            return None
        val_strs = data.split(self.DELIMITER)
        if not val_strs:
            return None

        vals = deque(map(int, val_strs))

        def build(min, max):
            if vals and min < vals[0] < max:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(min, val)
                node.right = build(val, max)
                return node

        return build(self.MIN, self.MAX)
