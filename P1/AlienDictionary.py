# Array, String, Depth-First Search, Breadth-First Search, Graph, Topological Sort
# Airbnb 15 Amazon 2 Facebook 2 Bloomberg 2 Google 6 Microsoft 6 Uber 5 Snapchat 3 Rubrik 12 Pinterest 6 Apple 4 Twitter 3 eBay 3 ByteDance 3 Coupang 2 Pocket Gems Wix
# https://leetcode.com/problems/alien-dictionary/description/
# https://www.lintcode.com/problem/892/
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

class AlienDictionary:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""

        order_pairs = self.get_order_pairs(words)
        if order_pairs == None:
            return ""
        node_to_indegree, node_to_nodes = self.build_graph(words, order_pairs)

        queue = deque()
        for letter, indegree in node_to_indegree.items():
            if indegree == 0:
                queue.append(letter)

        result = list()
        while queue:
            all_nodes = self.get_all_nodes(queue)
            result.extend(all_nodes)
            for node in all_nodes:
                for child in node_to_nodes[node]:
                    node_to_indegree[child] -= 1
                    if node_to_indegree[child] == 0:
                        queue.append(child)

        for letter, indegree in node_to_indegree.items():
            if indegree != 0:
                return ""

        return "".join(result)

    def get_order_pairs(self, words):
        pairs = list()
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            has_same_prefix = False
            for letter1, letter2 in zip(word1, word2):
                if letter1 != letter2:
                    pairs.append((letter1, letter2))
                    has_same_prefix = False
                    break
                else:
                    has_same_prefix = True

            if has_same_prefix and len(word1) > len(word2):
                return None

        return pairs

    def build_graph(self, words, order_pairs):
        node_to_indegree = dict()
        node_to_nodes = dict()
        # all chars are needed otherwise "xy","xz" will output "yz" instead of "xyz"
        for word in words:
            for letter in word:
                node_to_indegree[letter] = 0
                node_to_nodes[letter] = list()

        for from_letter, to_letter in order_pairs:
            node_to_indegree[to_letter] += 1
            node_to_nodes[from_letter].append(to_letter)

        return node_to_indegree, node_to_nodes

    def get_all_nodes(self, queue):
        nodes = list()
        while queue:
            nodes.append(queue.popleft())

        return nodes
