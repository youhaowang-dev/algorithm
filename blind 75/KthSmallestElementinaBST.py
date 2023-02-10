# Tree，Depth-First Search，Binary Search Tree，Binary Tree
# Uber 7 Amazon 4 Facebook 3 Expedia 3 Microsoft 2 eBay 2 Google 2 Adobe 2 Apple 3 LinkedIn 2 Oracle 2 VMware 2 Citadel 2 Bloomberg
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

class KthSmallestElementinaBST:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        iterator = BSTIterator(root)
        while k > 1:
            if not iterator.hasNext():
                return float("inf")

            iterator.getNext()
            k -= 1

        return iterator.getNext()


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = deque()
        self.push_roots(root)

    def hasNext(self) -> bool:
        return self.stack

    def getNext(self) -> int:
        node = self.stack.pop()
        self.push_roots(node.right)

        return node.val

    def push_roots(self, root: TreeNode) -> None:
        while root:
            self.stack.append(root)
            root = root.left
