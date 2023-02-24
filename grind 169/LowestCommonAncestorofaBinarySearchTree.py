# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Amazon 7 Adobe 3 Facebook 2 LinkedIn 2 Bloomberg 2 Apple 5 Google 2 Microsoft 2 Uber 2 Walmart Global Tech 4 Oracle 2 Reddit 2 Twitter
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# use BST property, if both are bigger than root.val, move to root.right
# if both are smaller than root.val, move to root.left, otherwise return the root
# time: O(n) for unbalanced tree, space: O(1)
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


class LowestCommonAncestorofaBinarySearchTree2:  # use BST property, recursion
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not p:
            return None
        if not q:
            return None

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:  # root.val is between
            return root


# divide and conquer, not using BST property, but can handle p and/or q not in tree case
class LowestCommonAncestorofaBinarySearchTree3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not p:
            return None
        if not q:
            return None

        if not root:
            return None

        if root == p:
            return root

        if root == q:
            return root

        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        if left_lca and right_lca:
            return root
        elif left_lca:
            return left_lca
        elif right_lca:
            return right_lca
        else:
            return None


# class LowestCommonAncestorofaBinarySearchTree {

#     #     6
#     #    / \
#     #   2   8
#     #  / \
#     # 0   4
#     #    / \
#     #   3   5
#     # find LCA for 0 and 5
#     # both are smaller, so go to left,
#     # now 2 is between 0 and 5, we found the LCA

#     # evaluate the root node, if both are in left or right, move root until not
#     # when not, the root is the LCA
#     # can use an example to prove
#     public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
#         int pVal = p.val
#         int qVal = q.val

#         TreeNode current = root  # current parent

#         while (current != null) {
#             int currentVal = current.val

#             if (pVal > currentVal & & qVal > currentVal) {
#                 # both in right subtree, drop left subtree
#                 current = current.right
#                 continue
#             }
#             if (pVal < currentVal & & qVal < currentVal) {
#                 # both in left subtree, drop right subtree
#                 current = current.left
#                 continue
#             }
#             # one in left subtree and one in right subtree, so this is the LCA
#             return current
#         }

#         return null
#     }

#     # recursion uses BST property
#     # binary search an answer
#     # time n space n
#     public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
#         int rootVal = root.val
#         int pVal = p.val
#         int qVal = q.val

#         if (pVal > rootVal & & qVal > rootVal) {
#             # both in right subtree, drop left subtree
#             return lowestCommonAncestor(root.right, p, q)
#         }
#         if (pVal < rootVal & & qVal < rootVal) {
#             # both in left subtree, drop right subtree
#             return lowestCommonAncestor(root.left, p, q)
#         }
#         # one in left subtree and one in right subtree, so this is the LCA
#         return root
#     }
# }
