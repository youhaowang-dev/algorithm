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


# BFS to serialize, BFS to deserialize by processing two nodes each time
class Codec:
    DELIMITER = "."
    NULL = "#"

    def serialize(self, root) -> str:
        if not root:
            return ""
        queue = deque()
        queue.append(root)
        result = list()
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(self.NULL)

        return self.DELIMITER.join(result)

    def deserialize(self, data) -> "TreeNode":
        if not data:
            return None
        vals = data.split(self.DELIMITER)
        if not vals:
            return None

        root = TreeNode(vals[0])
        queue = deque()
        queue.append(root)
        index = 0
        while index < len(vals) and queue:

            node = queue.popleft()
            left_val = vals[index + 1]
            right_val = vals[index + 2]
            if left_val != self.NULL:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            if right_val != self.NULL:
                node.right = TreeNode(right_val)
                queue.append(node.right)
            index += 2

        return root
