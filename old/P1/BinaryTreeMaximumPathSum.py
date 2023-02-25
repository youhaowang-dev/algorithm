# Dynamic Programming, Tree, Depth-First Search, Binary Tree
# DoorDash 23 Microsoft 5 Amazon 4 Facebook 3 Bloomberg 2 Adobe 2 Apple 2 Samsung 2 TikTok 2 Akuna Capital 2
# Google 8 ByteDance 6 Snapchat 3 Oracle 2 Twitter 2 Twilio 2 Yandex 2 Sprinklr 2 TuSimple 2
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has
# an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

from ast import Tuple
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# divide and conquer: time O(n)
# two types of paths: rootToAny and anyToAny
# max(rootToAny) = root.val + max(left rootToAny, right rootToAny)
# max(anyToAny) = max(left anyToAny, right anyToAny, current anyToAny)
#      current anyToAny passes the root = root.val + max(0, left anyToAny) + max(0, right anyToAny)
# rootToAny/anyToAny can be negative, so max(0, rootToAny/anyToAny) is needed because we don't have to take subtree paths
class BinaryTreeMaximumPathSum:
    MIN_SUM = -(2**31)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _, any_to_any = self.get_path_sums(root)

        return any_to_any

    # (root_to_any, any_to_any)
    def get_path_sums(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if not root:
            return (self.MIN_SUM, self.MIN_SUM)

        left_root_to_any, left_any_to_any = self.get_path_sums(root.left)
        right_root_to_any, right_any_to_any = self.get_path_sums(root.right)

        max_root_to_any = root.val + max(0, left_root_to_any, right_root_to_any)

        any_to_any_pass_root = (
            root.val + max(0, left_root_to_any) + max(0, right_root_to_any)
        )
        max_any_to_any = max(any_to_any_pass_root, left_any_to_any, right_any_to_any)

        return (max_root_to_any, max_any_to_any)
