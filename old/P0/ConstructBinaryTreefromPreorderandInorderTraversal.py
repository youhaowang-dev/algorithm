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

# time n space n, partition to exclude the root
class ConstructBinaryTreefromPreorderandInorderTraversal:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        preorder_queue = collections.deque(preorder)
        inorder_val_to_index = dict()
        for i, val in enumerate(inorder):
            inorder_val_to_index[val] = i

        return self.build_tree(preorder_queue, inorder_val_to_index, 0, len(inorder)-1)

    def build_tree(self, preorder_queue, inorder_val_to_index, left, right):
        if left > right:
            return None

        root_val = preorder_queue.popleft()
        root = TreeNode(root_val)
        root_index = inorder_val_to_index[root_val]
        root.left = self.build_tree(
            preorder_queue, inorder_val_to_index, left, root_index - 1)
        root.right = self.build_tree(
            preorder_queue, inorder_val_to_index, root_index + 1, right)

        return root


# time n^2 space n^2, partition to exclude the root
# preorder[1:inorder_root_index+1], preorder[inorder_root_index+1:]
class ConstructBinaryTreefromPreorderandInorderTraversal2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        inorder_root_index = inorder.index(root_val)  # assume unique

        root.left = self.buildTree(
            preorder[1:inorder_root_index + 1], inorder[:inorder_root_index])
        root.right = self.buildTree(
            preorder[inorder_root_index + 1:], inorder[inorder_root_index + 1:])

        return root
