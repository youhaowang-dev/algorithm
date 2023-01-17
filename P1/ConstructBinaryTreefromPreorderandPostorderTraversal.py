# Array, Hash Table, Divide and Conquer, Tree, Binary Tree
# Amazon 2 Google 3 Bloomberg 2 Uber 2 Adobe 2
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# global variable, can wrap them
class ConstructBinaryTreefromPreorderandPostorderTraversal:

    preIndex, posIndex = 0, 0

    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        root = TreeNode(preorder[self.preIndex])
        self.preIndex += 1
        if root.val != postorder[self.posIndex]:
            root.left = self.constructFromPrePost(preorder, postorder)
        if root.val != postorder[self.posIndex]:
            root.right = self.constructFromPrePost(preorder, postorder)
        self.posIndex += 1
        return root
