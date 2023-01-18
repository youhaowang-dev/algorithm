# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Facebook 10 Amazon 8 Bloomberg 5 Adobe 2 Microsoft 2 Salesforce 2 Uber 3 Oracle 3 Qualtrics 3 Apple 2 DoorDash 2
# ByteDance 12 Goldman Sachs 3 Walmart Global Tech 3 Google 2 VMware 2 tcs 2 FactSet 2 Flipkart 2 Wix
# https://leetcode.com/problems/binary-tree-right-side-view/

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the
# nodes you can see ordered from top to bottom.
from ast import List
from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeRightSideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            current_level_nodes = self.get_current_level_nodes(queue)
            result.append(current_level_nodes[-1].val)
            for node in current_level_nodes:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def get_current_level_nodes(self, queue: Deque[TreeNode]) -> List[TreeNode]:
        nodes = list()
        while queue:
            nodes.append(queue.popleft())

        return nodes
