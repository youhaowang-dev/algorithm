# Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# diameter = max node to node distance = max(1 + left_max_depth + right_max_depth, left_max, right_max)
class DiameterofBinaryTree:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_node_to_node, _ = self.get_max_diameter(root)
        return max_node_to_node

    # Tuple[max_node_to_node, max_root_to_leaf]
    def get_max_diameter(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if not root:
            return (0, 0)

        left_max_node_to_node, left_max_root_to_leaf = self.get_max_diameter(
            root.left)
        right_max_node_to_node, right_max_root_to_leaf = self.get_max_diameter(
            root.right)
        root_max_node_to_node = left_max_root_to_leaf + right_max_root_to_leaf
        max_node_to_node = max(left_max_node_to_node, right_max_node_to_node,
                               root_max_node_to_node)
        max_root_to_leaf = 1 + \
            max(left_max_root_to_leaf, right_max_root_to_leaf)

        return (
            max_node_to_node,
            max_root_to_leaf
        )
