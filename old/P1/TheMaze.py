# Depth-First Search, Breadth-First Search, Graph
# Square 4 TikTok 3 Amazon 2 Citadel 2 Google 3 Facebook 3 ByteDance 3 Microsoft 2 Snapchat 2 Bloomberg 2 Uber 2
# https://leetcode.com/problems/the-maze/description/

# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1).
# The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until
# hitting a wall. When the ball stops, it could choose the next direction.

# Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and
# destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

# You may assume that the borders of the maze are all walls (see examples).

from collections import deque
from typing import List

# bfs time m*n space m*n queue size can grow upto m∗n in worst case.
class TheMaze:
    EMPTY = 0
    WALL = 1
    VISITED = 2

    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        if not maze or not maze[0]:
            return False

        queue = deque()
        queue.append(start)
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while queue:
            row, col = queue.popleft()
            maze[row][col] = self.VISITED

            if row == destination[0] and col == destination[1]:
                return True

            for row_delta, col_delta in directions:
                new_row = row + row_delta
                new_col = col + col_delta
                # walk until hit wall
                while (
                    0 <= new_row < len(maze)
                    and 0 <= new_col < len(maze[0])
                    and maze[new_row][new_col] != self.WALL
                ):
                    new_row += row_delta
                    new_col += col_delta
                new_row -= row_delta
                new_col -= col_delta

                if maze[new_row][new_col] == self.EMPTY:
                    queue.append([new_row, new_col])

        return False


# dfs time m*n space m*n
class TheMaze2:
    EMPTY = 0
    WALL = 1
    DIRECTION_DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        if not maze or not maze[0]:
            return False

        visited = set()
        start_location = tuple(start)
        target_location = tuple(destination)

        def get_stop_location(
            node: Tuple[int, int], direction_delta: Tuple[int, int]
        ) -> tuple[int, int]:
            row, col = node
            row_delta, col_delta = direction_delta
            while (
                row >= 0
                and row < len(maze)
                and col >= 0
                and col < len(maze[0])
                and maze[row][col] == self.EMPTY
            ):
                row += row_delta
                col += col_delta

            return (row - row_delta, col - col_delta)

        def get_target_location(node: tuple[int, int]):
            if node == target_location:
                return True
            visited.add(node)

            for direction_delta in self.DIRECTION_DELTAS:
                stop = get_stop_location(node, direction_delta)
                if stop not in visited:
                    if get_target_location(stop):
                        return True

            return False

        return get_target_location(start_location)
