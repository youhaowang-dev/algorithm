# String, Stack, Tree, Binary Tree
# TikTok 3 Google
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

# One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node,
# we record the node's value. If it is a null node, we record using a sentinel value such as '#'.

# Binary tree could be considered as a number of slots to fulfill. At the start there is just one slot available
# for a number or null node. Both number and null node take one slot to be placed. For the null node the story
# ends up here, whereas the number will add into the tree two slots for the child nodes.
# Each child node could be, again, a number or a null.
class VerifyPreorderSerializationofaBinaryTree:
    DELIMITER = ","
    NULL_MARK = "#"

    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1  # root
        nodes = preorder.split(self.DELIMITER)
        for node in nodes:
            # take a slot
            slots -= 1

            # not enough slots
            if slots < 0:
                return False

            # non-null creates two slots for children
            if node != self.NULL_MARK:
                slots += 2

        # all slots should be filled
        return slots == 0
