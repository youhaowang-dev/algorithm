# Depth-First Search, Graph, Biconnected Component
# Facebook 2 Amazon 5 Microsoft 2 Adobe 2 Bloomberg 2 Apple 2 VMware 2 DE Shaw 2
# https://leetcode.com/problems/critical-connections-in-a-network/

# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where
# connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or
# indirectly through the network.

# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

# Return all critical connections in the network in any order.

# Example 1:
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# Example 2:
# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]

# An edge is a critical connection, if and only if it is not in a cycle.
class CriticalConnectionsinaNetwork:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        # Tarjan's algorithm 带人名的算法几乎不考
        return
