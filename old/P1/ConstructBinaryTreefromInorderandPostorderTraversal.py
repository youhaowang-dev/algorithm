#
# Amazon 2 Google 2 Shopee 5 Microsoft 4 Walmart Global Tech 2
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ConstructBinaryTreefromInorderandPostorderTraversal:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildTreeHelper(left, right):
            if left == right:
                return None
            root_val = postorder.pop()
            node = TreeNode(root_val)
            root_index = inorder_val_to_index[root_val]
            node.right = buildTreeHelper(root_index + 1, right)
            node.left = buildTreeHelper(left, root_index)

            return node

        inorder_val_to_index = dict()
        for i, val in enumerate(inorder):
            inorder_val_to_index[val] = i

        return buildTreeHelper(0, len(inorder))
