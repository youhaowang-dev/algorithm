# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Amazon 7 Adobe 3 Facebook 2 LinkedIn 2 Bloomberg 2 Apple 5 Google 2 Microsoft 2 Uber 2 Walmart Global Tech 4 Oracle 2 Reddit 2 Twitter
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# use BST property, if both are bigger than root.val, move to root.right
# if both are smaller than root.val, move to root.left, otherwise return the root
# time: O(n) for unbalanced tree, space: O(1)
class LowestCommonAncestorofaBinarySearchTree2:  # use BST property, recursion
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        root_val = root.val
        if root_val > p.val and root_val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root_val < p.val and root_val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


class LowestCommonAncestorofaBinarySearchTree:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not p:
            return None
        if not q:
            return None

        while root:
            root_val = root.val
            if p.val > root_val and q.val > root_val:
                root = root.right
            elif p.val < root_val and q.val < root_val:
                root = root.left
            else:  # p < root < q or q < root < p
                return root

        return None


# divide and conquer, not using BST property, but can handle p and/or q not in tree case
class LowestCommonAncestorofaBinarySearchTree3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p:
            return root

        if root == q:
            return root

        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)

        if left_result and right_result:
            return root
        elif left_result:
            return left_result
        elif right_result:
            return right_result
        else:
            return None
