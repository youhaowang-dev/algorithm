# String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Search Tree, Binary Tree
# Amazon 3 LinkedIn 3 Microsoft 3 Nutanix 3 Facebook 4 Splunk 3 Apple 2 Uber 2
# https://leetcode.com/problems/serialize-and-deserialize-bst/

# Serialization is converting a data structure or object into a sequence of bits so that it can be stored
# in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in
# the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be
# serialized to a string, and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Example 1:
# Input: root = [2,1,3]
# Output: [2,1,3]
# Example 2:
# Input: root = []
# Output: []

# preorder to serialize and deserialize, null == val out of bound of min and max
class Codec:
    DELIMITER = "."

    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder_vals = list()

        def build_preorder_vals(node):
            if not node:
                return

            preorder_vals.append(str(node.val))
            build_preorder_vals(node.left)
            build_preorder_vals(node.right)

        build_preorder_vals(root)
        return self.DELIMITER.join(preorder_vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        preorder_vals = deque(map(int, data.split(self.DELIMITER)))
        min_val = min(preorder_vals) - 1
        max_val = max(preorder_vals) + 1

        def build_from_preorder_vals(min_val, max_val):
            if not preorder_vals:
                return None

            if not (min_val < preorder_vals[0] < max_val):
                # val shoud not be the root, so fill this node with null
                return None

            root = TreeNode(preorder_vals.popleft())
            root.left = build_from_preorder_vals(min_val, root.val)
            root.right = build_from_preorder_vals(root.val, max_val)

            return root

        return build_from_preorder_vals(min_val, max_val)
