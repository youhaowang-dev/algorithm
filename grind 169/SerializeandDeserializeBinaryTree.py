# String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
# Amazon 12 Microsoft 4 Apple 4 DoorDash 3 Facebook 2 Google 2 Uber 2 Sprinklr 2 LinkedIn 15 Nvidia 3 C3 IoT 3
# Oracle 2 Nutanix 2 Pinterest 2 TikTok 2 Snapchat 9 Qualtrics 6 ByteDance 6 Adobe 5 Quora 4 Bloomberg 3 VMware 3
# Goldman Sachs 3 Coupang 2 Salesforce 2 Citadel 2 Splunk 2 Qualcomm 2 Yahoo
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
# stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later
# in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized
# to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily
# need to follow this format, so please be creative and come up with different approaches yourself.

# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:
# Input: root = []
# Output: []


# preorder to serialize and deserialize
class Codec:
    DELIMITER = "."
    NULL = "#"

    def serialize(self, root):
        preorder_vals = list()

        def build_preorder_vals(node):
            if not node:
                preorder_vals.append(self.NULL)
                return

            preorder_vals.append(str(node.val))
            build_preorder_vals(node.left)
            build_preorder_vals(node.right)

        build_preorder_vals(root)
        return self.DELIMITER.join(preorder_vals)

    def deserialize(self, data):
        preorder_vals = deque(data.split(self.DELIMITER))

        def build_from_preorder_vals():
            if preorder_vals[0] == self.NULL:
                preorder_vals.popleft()
                return None

            root = TreeNode(preorder_vals.popleft())
            root.left = build_from_preorder_vals()
            root.right = build_from_preorder_vals()

            return root

        return build_from_preorder_vals()

    # def deserialize(self, data):
    #     preorder_vals = data.split(self.DELIMITER)
    #     self.index = 0
    #     def build_from_preorder_vals():
    #         if preorder_vals[self.index] == self.NULL:
    #             self.index += 1
    #             return None

    #         root = TreeNode(int(preorder_vals[self.index]))
    #         self.index += 1
    #         root.left = build_from_preorder_vals()
    #         root.right = build_from_preorder_vals()

    #         return root

    #     return build_from_preorder_vals()
