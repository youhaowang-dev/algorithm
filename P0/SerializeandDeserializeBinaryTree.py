# String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
# Amazon 12 Microsoft 4 Apple 4 DoorDash 3 Facebook 2 Google 2 Uber 2 Sprinklr 2 LinkedIn 15 Nvidia 3 C3 IoT 3
# Oracle 2 Nutanix 2 Pinterest 2 TikTok 2 Snapchat 9 Qualtrics 6 ByteDance 6 Adobe 5 Quora 4 Bloomberg 3 VMware 3
# Goldman Sachs 3 Coupang 2 Salesforce 2 Citadel 2 Splunk 2 Qualcomm 2 Yahoo
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:
# Input: root = []
# Output: []

# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# level order traversal
class Codec:
    DELIMITER = "."
    NULL = "null"

    def serialize(self, root):
        if not root:
            return ""

        res = list()
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                res.append(self.NULL + self.DELIMITER)
                continue

            res.append(str(node.val) + self.DELIMITER)
            q.append(node.left)
            q.append(node.right)

        return "".join(res)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(self.DELIMITER)
        root = TreeNode(int(values[0]))

        q = deque()
        q.append(root)

        i = 1
        while i < len(values) and q:
            parent = q.popleft()
            if values[i] != self.NULL:
                left = TreeNode(int(values[i]))
                parent.left = left
                q.append(left)

            if values[i + 1] != self.NULL:
                right = TreeNode(int(values[i + 1]))
                parent.right = right
                q.append(right)

            i += 2

        return root
