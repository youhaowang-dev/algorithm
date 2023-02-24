# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Facebook 10 Amazon 8 Bloomberg 5 Adobe 2 Microsoft 2 Salesforce 2 Uber 3 Oracle 3 Qualtrics 3 Apple 2 DoorDash 2
# ByteDance 12 Goldman Sachs 3 Walmart Global Tech 3 Google 2 VMware 2 tcs 2 FactSet 2 Flipkart 2 Wix
# https://leetcode.com/problems/binary-tree-right-side-view/

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the
# nodes you can see ordered from top to bottom.

class BinaryTreeRightSideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return list()

        result = list()
        queue = deque()
        queue.append(root)
        while queue:
            all_nodes = self.get_all_nodes(queue)
            result.append(all_nodes[-1].val)
            for node in all_nodes:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def get_all_nodes(self, queue) -> List[TreeNode]:
        nodes = list()
        while queue:
            nodes.append(queue.popleft())

        return nodes
