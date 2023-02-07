# https://leetcode.com/problems/minimum-height-trees
# A tree is an undirected graph in which any two vertices are connected by exactly one path.
# In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates
# that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree
# as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees,
# those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


# brute force: build graph, use visited, get depth for each node and saves the nodes with min depth
# time n^2

# bfs like topological sort, 1 indegree, then reduce neighbor indegree by 1, and repeat
class MinimumHeightTrees:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        graph = collections.defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        indegrees = dict()
        for node in graph.keys():
            indegrees[node] = len(graph[node])

        queue = deque()
        visited = set()
        for node, indegree in indegrees.items():
            if indegree == 1:
                queue.append(node)
                visited.add(node)

        prev_nodes = list()
        while queue:
            nodes = self.get_all_nodes(queue)
            prev_nodes = nodes
            for node in nodes:
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] <= 1:
                        queue.append(neighbor)
                        visited.add(neighbor)

        return prev_nodes

    def get_all_nodes(self, queue):
        nodes = list()
        while queue:
            nodes.append(queue.popleft())

        return nodes
