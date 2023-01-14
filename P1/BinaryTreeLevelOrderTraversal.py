# Tree, Breadth-First Search, Binary Tree
# Bloomberg 11 Amazon 10 LinkedIn 2 Microsoft 8 Facebook 7 Oracle 4 Google 3 Apple 3 ServiceNow 3 Splunk 2 Adobe 2 Uber 3 Paypal 2 Visa 2 Accolite 2 TikTok 2
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeLevelOrderTraversal:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = list()
        if not root:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            current_level_nodes = self.getCurrent_level_nodes(queue)
            current_level_result = list()
            for node in current_level_nodes:
                current_level_result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(current_level_result)

        return result

    def getCurrent_level_nodes(self, queue) -> List[int]:
        nodes = list()

        while len(queue) > 0:
            nodes.append(queue.popleft())

        return nodes


# dfs
class BinaryTreeLevelOrderTraversal2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = list()
        self.dfs_traverse(results, root, 0)

        return results

    def dfs_traverse(
        self, results: List[List[int]], root: Optional[TreeNode], depth: int
    ):
        if not root:
            return

        if len(results) == depth:
            # init container for next level
            results.append(list())

        results[depth].append(root.val)
        self.dfs_traverse(results, root.left, depth + 1)
        self.dfs_traverse(results, root.right, depth + 1)
