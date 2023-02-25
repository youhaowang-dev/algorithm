# Depth-First Search, Breadth-First Search, Graph, Heap (Priority Queue), Shortest Path
# ByteDance 3 Microsoft 2 Google 4 Amazon 3
# https://leetcode.com/problems/the-maze-ii/
# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1).
# The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until
# hitting a wall. When the ball stops, it could choose the next direction.

# Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol]
# and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at
# the destination. If the ball cannot stop at destination, return -1.

# The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

# You may assume that the borders of the maze are all walls (see examples).
from collections import deque
from typing import List


class TheMazeII:
    DIRECTION_DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def shortestDistance(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        if maze[start[0]][start[1]] == 1:
            return -1

        n, m = len(maze), len(maze[0])
        default_dist = float("inf")
        dist = [[default_dist for _ in range(m)] for _ in range(n)]
        dist[start[0]][start[1]] = 0

        queue = deque()
        queue.append((start[0], start[1]))
        while queue:
            row, col = queue.popleft()

            for dx, dy in self.DIRECTION_DELTAS:
                d = dist[row][col]
                x = row
                y = col
                while 0 <= x + dx < n and 0 <= y + dy < m and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    d += 1

                if d < dist[x][y]:
                    dist[x][y] = d
                    queue.append((x, y))

        if dist[destination[0]][destination[1]] == default_dist:
            return -1

        return dist[destination[0]][destination[1]]
