# Tree, Breadth-First Search, Binary Tree
# Amazon 17 Bloomberg 8 Microsoft 7 Facebook 3 Adobe 3 Yandex 3 Apple 2 Oracle 2 Walmart Global Tech 2 LinkedIn 4 Google 2 ServiceNow 2 Salesforce 2 VMware 2 SAP 2 Cisco 2 TikTok 2
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# IMPORTANT: do not try to reverse during the traversal because tree left right will not make it work
# only reverse the level value results before adding to the master list

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeZigzagLevelOrderTraversal:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = list()
        if not root:
            return results

        queue = deque()
        queue.append(root)
        is_reverse_order = False
        while queue:
            temp = list()
            nodes = self.get_current_level_nodes(queue)
            for node in nodes:
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if is_reverse_order:
                temp = reversed(temp)

            is_reverse_order = not is_reverse_order
            results.append(temp)

        return results

    def get_current_level_nodes(self, queue):
        nodes = list()
        while queue:
            nodes.append(queue.popleft())

        return nodes
