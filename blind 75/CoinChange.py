# Array, Dynamic Programming, Breadth-First Search
# https://leetcode.com/problems/coin-change/
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

# brute force: branching factor=len(coins), max recursion depth=amount/min_coin, so O(len(coins)^(amount/min_coin))
# brute force with memoization: time O(len(coins) * amount), space O(amount) where coin=1, so recursion goes amount depth
class CoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1

        amount_to_min_count = dict()  # memo
        min_count = self.search_min_count(coins, amount, amount_to_min_count)

        if min_count == math.inf:
            return -1

        return min_count

    def search_min_count(self, coins, amount, amount_to_min_count):
        if amount in amount_to_min_count:
            return amount_to_min_count[amount]

        if amount == 0:
            return 0

        if amount < 0:
            return math.inf

        min_count = math.inf
        for coin in coins:
            count = self.search_min_count(
                coins, amount - coin, amount_to_min_count)
            min_count = min(min_count, 1 + count)

        amount_to_min_count[amount] = min_count

        return min_count


class CoinChange2:  # dp
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for am in range(1, amount + 1):
            for coin in coins:
                if am - coin >= 0:
                    dp[am] = min(dp[am], dp[am - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1
