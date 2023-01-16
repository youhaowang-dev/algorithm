# Array, Hash Table, Divide and Conquer, Tree, Binary Tree
# Bloomberg 7 Amazon 7 Microsoft 8 Adobe 4 Google 3 Apple 3 Yahoo 2 Uber 2 ByteDance 5 Facebook 4 Splunk 3 LinkedIn 2 TikTok 2
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
# inorder is the inorder traversal of the same tree, construct and return the binary tree.


# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Preorder traversal follows Root -> Left -> Right, therefore, given the preorder array preorder,
# we have easy access to the root which is preorder[0].
# Inorder traversal follows Left -> Root -> Right, therefore if we know the position of Root,
# we can recursively split the entire array into two subtrees.
class ConstructBinaryTreefromPreorderandInorderTraversal:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root_val = preorder[0]
        if len(inorder) == 1:
            return TreeNode(root_val)

        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        left_preorder = preorder[1 : root_index + 1]
        left_inorder = inorder[:root_index]
        root.left = self.buildTree(left_preorder, left_inorder)

        right_preorder = preorder[root_index + 1 :]
        right_inorder = inorder[root_index + 1 :]
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
