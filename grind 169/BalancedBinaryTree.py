# Tree, Depth-First Search, Binary Tree
# Amazon 4 Facebook 3 Google 3 Spotify 3 Uber 2 Bloomberg 2 Adobe 2 Microsoft 3
# https://leetcode.com/problems/balanced-binary-tree/
# Given a binary tree, determine if it is height-balanced.

# balanced = left_balanced and right_balanced and root_balanced
# root_balanced = abs(left_max_depth - right_max_depth) < 2
# need this because both subtrees can be balanced but depth are different more than 2
# time O(n), space(n) for unbalanced tree
class BalancedBinaryTree:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, _ = self.is_balanced_helper(root)

        return is_balanced

    def is_balanced_helper(self, root) -> Tuple[bool, int]:
        if not root:
            return (True, 0)

        left_is_balanced, left_max_depth = self.is_balanced_helper(root.left)
        right_is_balanced, right_max_depth = self.is_balanced_helper(
            root.right)
        root_is_balanced = abs(left_max_depth - right_max_depth) < 2

        return (
            left_is_balanced and right_is_balanced and root_is_balanced,
            1 + max(left_max_depth, right_max_depth)
        )


# solution2: iterative post order traversal, just know this
class BalancedBinaryTree2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack, node, last, depths = deque(), root, None, dict()
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right = depths.get(
                        node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1:
                        return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
