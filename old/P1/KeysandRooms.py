# Depth-First Search, Breadth-First Search, Graph
# Amazon 2 Google 2 Microsoft 2 Hotstar 5 Twitch 2 Bloomberg 2
# https://leetcode.com/problems/keys-and-rooms/

# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
# Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it,
# denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
# return true if you can visit all the rooms, or false otherwise.

# Example 1:
# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation:
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.

# Example 2:
# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

from collections import deque, dequeueue
from typing import List

# The problem can be seen as a graph problem, where the rooms are the nodes and the keys in each room are its
# neighbors (i.e., there is a directed edge connecting this room and the key's room). Starting from node 0,
# we want to see if we can traverse the entire graph or not. BFS and DFS are the two algorithms that can help,
# and since this problem has nothing to do with distance, shortest path, etc. DFS is a very good candidate.


# dfs
class KeysandRooms:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False

        room_0_key = 0
        stack = deque()
        stack.append(room_0_key)
        visited = set()
        visited.add(room_0_key)
        while stack:
            node = stack.pop()
            for key in rooms[node]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)

        return len(visited) == len(rooms)


# bfs
class KeysandRooms2:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False

        first_room_key = 0
        queue = deque()
        queue.append(first_room_key)
        visited = set()
        visited.add(first_room_key)
        while queue:
            node = queue.popleft()
            for k in rooms[node]:
                if k not in visited:
                    visited.add(k)
                    queue.append(k)

        return len(visited) == len(rooms)
