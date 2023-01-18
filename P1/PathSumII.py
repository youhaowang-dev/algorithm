# Backtracking, Tree, Depth-First Search, Binary Tree
# Amazon 5 Bloomberg 3 DoorDash 3 Zillow 2
# https://leetcode.com/problems/path-sum-ii/

# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of
# the node values in the path equals targetSum. Each path should be returned as a list of the node values,
# not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs will cost too much space because each node will need to maintain a list
# as a result, dfs is better for this question
class PathSumII:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        result = list()
        if not root:
            return result

        path_state = list()
        self.searchPathSum(root, target, path_state, result)

        return result

    def searchPathSum(
        self,
        root: Optional[TreeNode],
        target_remain: int,
        path_state: List[int],
        result: List[List[int]],
    ) -> None:
        if not root:
            return

        path_state.append(root.val)

        if self.is_leaf(root) and target_remain == root.val:
            result.append(list(path_state))

        if root.left:
            self.searchPathSum(root.left, target_remain - root.val, path_state, result)
        if root.right:
            self.searchPathSum(root.right, target_remain - root.val, path_state, result)

        path_state.pop()

    def is_leaf(self, node: TreeNode) -> bool:
        return not node.left and not node.right
