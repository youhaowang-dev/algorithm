# Given the root of a binary tree, invert the tree, and return its root.
# https://leetcode.com/problems/invert-binary-tree/


# do as the requirement asks for recursively
class InvertBinaryTree:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)

        return root


class InvertBinaryTree2:  # level order traversal
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
