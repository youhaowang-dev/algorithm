# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Amazon 5 Apple 5 Google 3 Facebook 2 LinkedIn 10 Microsoft 5 Spotify 4 Adobe 3 Bloomberg 2 Intel 3 Visa 2 Yahoo Uber
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along
# the longest path from the root node down to the farthest leaf node.

# can also bfs
class MaximumDepthOfBinaryTree:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left or root.right:  # max for non-left return 0
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        else:  # leaf
            return 1
