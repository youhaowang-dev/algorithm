# Tree, Breadth-First Search, Binary Tree
# Bloomberg 11 Amazon 10 LinkedIn 2 Microsoft 8 Facebook 7 Oracle 4 Google 3 Apple 3 ServiceNow 3 Splunk 2 Adobe 2
# Uber 3 Paypal 2 Visa 2 Accolite 2 TikTok 2
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


class BinaryTreeLevelOrderTraversal:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = list()
        if not root:
            return results

        queue = deque()
        queue.append(root)
        while queue:
            nodes = self.get_all_nodes(queue)
            result = list()
            for node in nodes:
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            results.append(result)

        return results

    def get_all_nodes(self, queue) -> List[TreeNode]:
        nodes = list()
        while queue:
            nodes.append(queue.popleft())

        return nodes


# dfs
class BinaryTreeLevelOrderTraversal2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = list()
        self.dfs_traverse(results, root, 0)

        return results

    def dfs_traverse(
        self, results: List[List[int]], root: Optional[TreeNode], depth: int
    ):
        if not root:
            return

        if len(results) == depth:
            # init container for next level
            results.append(list())

        results[depth].append(root.val)
        self.dfs_traverse(results, root.left, depth + 1)
        self.dfs_traverse(results, root.right, depth + 1)
