# https://www.lintcode.com/problem/127/
# Given an directed graph, a topological order of the graph nodes is defined as follow:

# For each directed edge A -> B in graph, A must before B in the order list.
# The first node in the order can be any node in the graph with no nodes direct to it.
# Find any topological order for the given graph.

from collections import deque
from typing import List


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class TopologicalSorting:
    def topSort(self, graph: List[DirectedGraphNode]) -> List[DirectedGraphNode]:
        node_to_indegree = dict()
        # only process neighbors, so the 0 indegree nodes will not be in the dict
        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] = node_to_indegree.get(neighbor, 0) + 1

        queue = deque()
        for node in graph:
            if node not in node_to_indegree:
                queue.append(node)

        result = list()
        while len(queue):
            node = queue.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)

        return result
