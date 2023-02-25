# Depth-First Search, Breadth-First Search, Union Find, Graph
# Google 2 Bloomberg 2 TikTok 2 LinkedIn 10 Amazon 3 Microsoft 3 Coupang 3 Qualtrics 2 TuSimple 2 Facebook Zenefits
# https://leetcode.com/problems/graph-valid-tree/
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where
# edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.
from collections import deque
from typing import List

# tree = graph that all nodes connected and no cycle

# bfs, n=4,edges=[[0,1],[0,2],[0,3]] => graph=[[1, 2, 3], [0], [0], [0]]
class GraphValidTree:
    def validTree(self, max_node: int, edges: List[List[int]]) -> bool:
        if edges is None:
            # empty list need additional check
            return False

        if max_node - 1 != len(edges):
            return False

        graph = self.build_graph(max_node, edges)
        visited = set()
        queue = deque()
        queue.append(0)
        parent = [-1 for _ in range(max_node)]

        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    parent[neighbor] = node
                    queue.append(neighbor)
                elif neighbor == parent[node]:
                    # visited but it is parent; parent is fine for undirected graph
                    continue
                else:
                    return False

        return len(visited) == max_node

    def build_graph(self, n, edges):
        graph = [[] for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        return graph


# dfs, n=4,edges=[[0,1],[0,2],[0,3]] => graph=[[1, 2, 3], [0], [0], [0]]
class GraphValidTree2:
    def validTree(self, max_node: int, edges: List[List[int]]) -> bool:
        if edges is None:
            # empty list need additional check
            return False

        if max_node - 1 != len(edges):
            return False

        graph = self.build_graph(max_node, edges)
        visited = set()

        start_node = 0
        start_parent = -1  # less than min node
        if self.hasCycle(start_node, start_parent, visited, graph):
            return False

        return True if len(visited) == max_node else False

    # build_adjacency_list
    def build_graph(self, n, edges):
        graph = [[] for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        return graph

    def hasCycle(self, node, parent, visited, graph):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if self.hasCycle(neighbor, node, visited, graph):
                    return True
            elif neighbor != parent:
                return True

        return False
