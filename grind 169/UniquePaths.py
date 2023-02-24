# Math, Dynamic Programming, Combinatorics
# Amazon 16 Google 10 Adobe 6 Apple 5 Bloomberg 4 Yahoo 3 Facebook 2 TikTok 2 Cruise Automation 2 Trilogy 2
# Microsoft 11 Goldman Sachs 2 Expedia 2 Infosys 2 ByteDance 4 Salesforce 3 Zillow 3 Oracle 3 Walmart Global Tech 2
# VMware 2 Uber 2 Wish 2 Morgan Stanley 2 Zoho 2 Intuit 2
# https://leetcode.com/problems/unique-paths/description/

# There is a robot on an m x n grid. The robot is initially located at the top-left corner(i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner(i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down


# brute force with memoization
# time m*n max m*n possible space m*n for memo
class UniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = dict()
        return self.get_unique_paths(m, n, memo)

    def get_unique_paths(self, m, n, memo):
        if (m, n) in memo:
            return memo[(m, n)]

        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1

        path1 = self.get_unique_paths(m - 1, n, memo)
        memo[(m - 1, n)] = path1
        path2 = self.get_unique_paths(m, n - 1, memo)
        memo[(m, n - 1)] = path2

        return path1 + path2


class UniquePaths2:  # brute force 2^(m+n)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
