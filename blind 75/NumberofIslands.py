# Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
# Amazon 83 Bloomberg 36 Google 19 Apple 10 Facebook 8 Uber 8 Microsoft 6 Adobe 5 Zillow 3 Walmart Global Tech 3
# TikTok 3 Oracle 2 Tesla 2 Cruise Automation 2 Intuit 2 Yandex 2 LinkedIn 15 DoorDash 8 ByteDance 6 eBay 5
# Paypal 5 VMware 4 Twitch 4 Docusign 4 Shopee 4 Snapchat 3 Dropbox 3 JPMorgan 3 Karat 3 Qualtrics 2 Goldman Sachs 2
# SAP 2 Nvidia 2 Salesforce 2 Visa 2 Intel 2 ServiceNow 2 Audible 2 MakeMyTrip 2 Arcesium 2 Reddit 2 Citadel 8
# Expedia 7 Yahoo 5 Palantir Technologies 4 Square 4 Splunk 4 Lyft 3 Lending Club 3 Indeed 3 DE Shaw 3 Nutanix 2
# Samsung 2 Wish 2 Cisco 2 Groupon 2 PayTM 2 Flipkart 2 MindTickle 2 Wayfair 2 HBO 2 Zenefits Wix

# https://leetcode.com/problems/number-of-islands/

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
from collections import deque
from typing import List

# dfs time m*n space m*n


class NumberofIslands:
    LAND = "1"
    WATER = "0"

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row_count = len(grid)
        col_count = len(grid[0])
        island_count = 0
        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == self.LAND:
                    island_count += 1
                    self.dfs(grid, row, col)

        return island_count

    def dfs(self, grid: List[List[str]], row: int, col: int) -> None:
        row_count = len(grid)
        col_count = len(grid[0])

        if (
            row < 0
            or col < 0
            or row >= row_count
            or col >= col_count
            or grid[row][col] == self.WATER
        ):
            return

        grid[row][col] = self.WATER
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)


# bfs
# Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search.
# Put it into a queue and set its value as '0' to mark as visited node. Iteratively search the neighbors of enqueued
# nodes until the queue becomes empty.
class NumberofIslands2:
    LAND = "1"
    WATER = "0"

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row_count = len(grid)
        col_count = len(grid[0])
        num_islands = 0

        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == "1":
                    num_islands += 1
                    grid[row][col] = self.WATER  # mark as visited
                    self.bfs(grid, row, col)  # mark neighbors as visited

        return num_islands

    def bfs(self, grid: List[List[str]], row: int, col: int) -> None:
        row_count = len(grid)
        col_count = len(grid[0])
        neighbors = deque()
        neighbors.append((row, col))
        while neighbors:
            row, col = neighbors.popleft()
            if row - 1 >= 0 and grid[row - 1][col] == self.LAND:
                neighbors.append((row - 1, col))
                grid[row - 1][col] = self.WATER

            if row + 1 < row_count and grid[row + 1][col] == self.LAND:
                neighbors.append((row + 1, col))
                grid[row + 1][col] = self.WATER

            if col - 1 >= 0 and grid[row][col - 1] == self.LAND:
                neighbors.append((row, col - 1))
                grid[row][col - 1] = self.WATER

            if col + 1 < col_count and grid[row][col + 1] == self.LAND:
                neighbors.append((row, col + 1))
                grid[row][col + 1] = self.WATER
