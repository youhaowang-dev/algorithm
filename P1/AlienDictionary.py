# Array, String, Depth-First Search, Breadth-First Search, Graph, Topological Sort
# Airbnb 15 Amazon 2 Facebook 2 Bloomberg 2 Google 6 Microsoft 6 Uber 5 Snapchat 3 Rubrik 12 Pinterest 6 Apple 4 Twitter 3 eBay 3 ByteDance 3 Coupang 2 Pocket Gems Wix
# https://leetcode.com/problems/alien-dictionary/description/
# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary, where the strings in words are
# sorted lexicographically
#  by the rules of this new language.

# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

# Example 1:
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:
# Input: words = ["z","x"]
# Output: "zx"
# Example 3:
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
from collections import deque
from typing import Dict, List, Set


class AlienDictionary:

    # the first different char of two words can form an edge
    # for example, "wrt","wrf" => t > f => t -> f
    # there could be more chars between t and f, so we need to get all edges and do topological sort
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""

        charToChars: Dict[str, Set[str]] = self.build_graph(words)
        if not charToChars:
            return ""

        return self.get_topological_order(charToChars)

    def build_graph(self, words: List[str]) -> Dict[str, Set[str]]:
        graph = dict()
        # build nodes
        for word in words:
            for character in word:
                if character not in graph:
                    graph[character] = set()

        # build edges
        for i in range(0, len(words) - 1):
            index = 0
            while index < len(words[i]) and index < len(words[i + 1]):
                currentChar = words[i][index]
                nextChar = words[i + 1][index]
                if currentChar != nextChar:
                    graph.get(currentChar).add(nextChar)
                    break  # only need the first diff chars
                index += 1

            # check invalid input
            if index == min(len(words[i]), len(words[i + 1])):
                if len(words[i]) > len(words[i + 1]):
                    return None

        return graph

    def get_topological_order(self, graph) -> str:
        indegree: Dict[str, int] = self.get_indegree(graph)
        queue = deque()
        for char in indegree.keys():
            if indegree.get(char) == 0:
                queue.append(char)

        result = list()
        while queue:
            head = queue.popleft()
            result.append(head)
            for neighbor in graph.get(head):
                indegree[neighbor] = -1 + indegree.get(neighbor)
                if indegree.get(neighbor) == 0:
                    queue.append(neighbor)

        if len(result) == len(indegree):
            return "".join(result)

        return ""

    def get_indegree(self, graph) -> Dict[str, int]:
        indegree: Dict[str, int] = dict()
        for from_char in graph.keys():
            indegree[from_char] = 0

        for from_char in graph.keys():
            for to_char in graph.get(from_char):
                indegree[to_char] = 1 + indegree.get(to_char, 0)

        return indegree
