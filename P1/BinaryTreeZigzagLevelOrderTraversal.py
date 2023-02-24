# Tree, Breadth-First Search, Binary Tree
# Amazon 17 Bloomberg 8 Microsoft 7 Facebook 3 Adobe 3 Yandex 3 Apple 2 Oracle 2 Walmart Global Tech 2 LinkedIn 4 Google 2 ServiceNow 2 Salesforce 2 VMware 2 SAP 2 Cisco 2 TikTok 2
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# IMPORTANT: do not try to reverse during the traversal because tree left right will not make it work
# only reverse the level value results before adding to the master list


class BinaryTreeZigzagLevelOrderTraversal:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = list()
        if not root:
            return results

        to_right = True
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

            if to_right:
                to_right = False
            else:
                result = reversed(result)
                to_right = True

            results.append(result)

        return results

    def get_all_nodes(self, queue):
        nodes = list()
        while queue:
            nodes.append(queue.popleft())

        return nodes
