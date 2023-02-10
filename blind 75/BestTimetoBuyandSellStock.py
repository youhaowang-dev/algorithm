# Array, Dynamic Programming
# Amazon 44 Adobe 14 Apple 13 Bloomberg 10 Microsoft 10 Bolt 8 Facebook 6 Google 6 Cisco 5 Goldman Sachs 4 Uber 3 Oracle 3 PayTM 3 DE Shaw 2 Yahoo 2 Citadel 2 Salesforce 2 Walmart Global Tech 2 Intel 2 tcs 2
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# buy low sell high, but time only moves forward
# two pointers, right+=1 if can make a profit, otherwise move left to right and right +=1, and continue
# time O(n), space O(1)
class BestTimetoBuyandSellStock:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        left = 0
        right = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:  # unable to buy low sell high because right is lower
                left = right
                right += 1
            else:
                max_profit = max(max_profit, profit)
                right += 1

        return max_profit

# brute force: find the max diff for all possible buy-sell events


class BestTimetoBuyandSellStock2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        length = len(prices)
        max_profit = 0
        for buy in range(0, length):
            for sell in range(buy + 1, length):
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)

        return max_profit
