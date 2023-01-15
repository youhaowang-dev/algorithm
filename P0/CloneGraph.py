# Hash Table, Depth-First Search, Breadth-First Search, Graph
# Facebook 5 Amazon 4 Apple 3 Bloomberg 8 Google 5 Microsoft 3 Adobe 2 Pinterest 2 Salesforce 6 Twitter 3 Uber 3 Qualtrics 2 Oracle 2 Goldman Sachs 2 ByteDance 2 Pocket Gems Wix
# https://leetcode.com/problems/clone-graph/

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

from collections import deque
from typing import Dict, List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class CloneGraph:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        nodes = self.get_all_nodes(node)
        node_to_copy = self.copy_nodes(nodes)
        self.copy_edges(nodes, node_to_copy)

        return node_to_copy.get(node)

    def get_all_nodes(self, node: "Node") -> List["Node"]:
        nodes = list()
        visited = set()
        queue = deque()
        queue.append(node)

        while queue:
            node = queue.popleft()
            if node in visited:
                continue

            nodes.append(node)
            visited.add(node)

            for neighbor in node.neighbors:
                queue.append(neighbor)

        return nodes

    def copy_nodes(self, nodes: List["Node"]) -> Dict["Node", "Node"]:
        node_to_copy = dict()

        for node in nodes:
            node_to_copy[node] = Node(node.val)

        return node_to_copy

    def copy_edges(
        self, nodes: List["Node"], node_to_copy: Dict["Node", "Node"]
    ) -> None:
        for node in nodes:
            copy = node_to_copy.get(node)
            for neighbor in node.neighbors:
                neighbor_copy = node_to_copy.get(neighbor)
                copy.neighbors.append(neighbor_copy)
