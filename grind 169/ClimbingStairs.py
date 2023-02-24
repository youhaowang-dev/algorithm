# Math, Dynamic Programming, Memoization
# Amazon 16 Adobe 11 Google 5 Apple 5 Bloomberg 3 Microsoft 3 Uber 2 Visa 2 Nagarro 2 Yahoo 4 Oracle 4 Goldman Sachs 3
# Expedia 3 Intel 2 Facebook 4 Walmart Global Tech 3 Morgan Stanley 3 LinkedIn 2 eBay 2 Cisco 2 VMware 2 Twilio 2 Optum 2
# https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# ways[n] = ways[n - 1] + ways[n - 2]
class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        stairs = 3
        prev_prev_ways = 1
        prev_ways = 2
        while stairs <= n:
            ways = prev_prev_ways + prev_ways
            prev_prev_ways = prev_ways
            prev_ways = ways
            stairs += 1

        return ways


# brute force, O(2^n), ways[n] = ways[n - 1] + ways[n - 2]
class ClimbingStairs2:
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1

        return self.get_ways(n)

    def get_ways(self, n: int) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1

        return self.get_ways(n - 2) + self.get_ways(n - 1)
