# Array, Breadth-First Search, Matrix
# Amazon 25 Lyft 6 Uber 4 Apple 3 Salesforce 3 Google 2 Adobe 2 Bloomberg 2 Intuit 2 TikTok 2 Microsoft 13
# LinkedIn 3 VMware 3 Goldman Sachs 2 Walmart Global Tech 5 Samsung 4 Facebook 3 Oracle 3 eBay 2 InMobi 2 Twilio 2
# https://leetcode.com/problems/rotting-oranges/
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# bfs count rounds
class RottingOranges:
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        row_count = len(grid)
        col_count = len(grid[0])

        fresh_count = 0
        queue = deque()
        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == self.ROTTEN:
                    queue.append((row, col))
                elif grid[row][col] == self.FRESH:
                    fresh_count += 1

        minutes_count = 0
        while queue:  # bfs
            locations = self.get_all_locations(queue)
            for row, col in locations:
                for row_delta, col_delta in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    next_row = row + row_delta
                    next_col = col + col_delta
                    if not (0 <= next_row < row_count):
                        continue
                    if not (0 <= next_col < col_count):
                        continue
                    if grid[next_row][next_col] == self.FRESH:
                        grid[next_row][next_col] = self.ROTTEN
                        fresh_count -= 1
                        queue.append((next_row, next_col))

            if queue:
                minutes_count += 1

        if fresh_count == 0:
            return minutes_count

        return -1

    def get_all_locations(self, queue) -> List[Tuple[int, int]]:
        locations = list()
        while queue:
            locations.append(queue.popleft())

        return locations
