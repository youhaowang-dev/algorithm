# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Amazon 19 Bloomberg 19 Apple 5 Microsoft 4 Yahoo 3 Zillow 3 Facebook 2 Salesforce 2 Uber 2 Yandex 2 Paypal 2
# https://leetcode.com/problems/validate-binary-search-tree/
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left  subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# inorder traverse values should be increasing
class ValidateBinarySearchTree:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = collections.deque()
        self.push_lefts(stack, root)  # smaller and smaller...
        # 0 wont work with if prev_val and ... because 0 is false [0,null,-1] will fail
        prev_val = -math.inf
        while stack:
            node = stack.pop()
            if prev_val >= node.val:
                return False
            prev_val = node.val
            self.push_lefts(stack, node.right)

        return True

    def push_lefts(self, stack, node):
        while node:
            stack.append(node)
            node = node.left


# every node must fullfil min_val < node.val < max_val


class ValidateBinarySearchTree2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        min_val = -math.inf
        max_val = math.inf
        return self.is_valid_bst(root, min_val, max_val)

    def is_valid_bst(
        self,
        root: Optional[TreeNode],
        min_val: float,
        max_val: float,
    ):
        if not root:
            return True  # able to reach leaf means valid

        if not (min_val < root.val < max_val):
            return False

        left_is_valid = self.is_valid_bst(root.left, min_val, root.val)
        right_is_valid = self.is_valid_bst(root.right, root.val, max_val)

        return left_is_valid and right_is_valid
