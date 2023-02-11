# Hash Table, Depth-First Search, Breadth-First Search, Graph
# Facebook 5 Amazon 4 Apple 3 Bloomberg 8 Google 5 Microsoft 3 Adobe 2 Pinterest 2 Salesforce 6 Twitter 3 Uber 3
# Qualtrics 2 Oracle 2 Goldman Sachs 2 ByteDance 2 Pocket Gems Wix
# https://leetcode.com/problems/clone-graph/

# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# bfs, time n space n
class CloneGraph:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        nodes = self.get_all_nodes(node)
        node_to_copy = self.copy_nodes(nodes)
        self.copy_edges(nodes, node_to_copy)

        return node_to_copy[node]

    def get_all_nodes(self, node: 'Node') -> List['Node']:
        visisted = set()
        nodes = list()

        queue = deque()
        queue.append(node)
        visisted.add(node)
        while queue:
            node = queue.popleft()
            nodes.append(node)
            for neighbor in node.neighbors:
                if neighbor in visisted:
                    continue
                queue.append(neighbor)
                visisted.add(neighbor)

        return nodes

    def copy_nodes(self, nodes: List['Node']) -> Dict['Node', 'Node']:
        node_to_copy = dict()
        for node in nodes:
            copy = Node(node.val)
            node_to_copy[node] = copy

        return node_to_copy

    def copy_edges(self, nodes: List['Node'], node_to_copy: Dict['Node', 'Node']) -> None:
        for node in nodes:
            copy = node_to_copy[node]
            for neighbor in node.neighbors:
                neighbor_copy = node_to_copy[neighbor]
                copy.neighbors.append(neighbor_copy)
