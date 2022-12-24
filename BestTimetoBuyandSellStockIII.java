// Array, Dynamic Programming
// Amazon 7 Bolt 6 Bloomberg 3 Google 2 Citadel 2 Uber 5 Apple 3 Oracle 2 Snapchat 3 Adobe 3 Qualtrics 2
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

class BestTimetoBuyandSellStockIII {

  public int maxProfit(int[] prices) {
    int n = prices.length;
    if (n < 2) {
      return 0;
    }

    int[] left = new int[n]; // highest profit in 0 ... i
    int[] right = new int[n]; // highest profit in i ... n - 1

    // DP from left to right
    int min = prices[0];
    for (int i = 1; i < n; i++) {
      min = Math.min(min, prices[i]);
      left[i] = Math.max(left[i - 1], prices[i] - min);
    }

    // DP from right to left
    int max = prices[n - 1];
    for (int i = n - 2; i >= 0; i--) {
      max = Math.max(max, prices[i]);
      right[i] = Math.max(right[i + 1], max - prices[i]);
    }

    int profit = 0;
    for (int i = 0; i < n; i++) {
      profit = Math.max(profit, left[i] + right[i]);
    }

    return profit;
  }

  // Specifically, given a list of prices, for any two adjacent time points with stock prices p1 and p2, the best strategies can be the following two cases:
  // If later the price augments, i.e. p2 > p1, then a good trader should buy at p1 and then sell at p2, seizing this moment to make profits.
  // If later the price stays the same or even plunges, i.e. p2 <= p1, then a good trader should just hold the money in the pocket, neither to buy nor sell any stock.
  // With the above strategies, as one can see, we would perfectly capitalize at each right moment, meanwhile avoiding any loss. At the end, the accumulative profits that we gain over the time would reach the maximum.

  // keep cost low and keep profit high for both transactions
  // The intuition is that we can consider the problem as a game, and we as agent could make at most two transactions in order to gain the maximum points (profits) from the game.
  // The two transactions be decomposed into 4 actions: "buy of transaction #1", "sell of transaction #1", "buy of transaction #2" and "sell of transaction #2".
  public int maxProfit(int[] prices) {
    // the minimal cost of buying the stock in transaction #1. The minimal cost to acquire a stock would be the minimal price value that we have seen so far at each step.
    int firstTransactionCost = Integer.MAX_VALUE;
    // the maximal profit of selling the stock in transaction #1.
    int firstTransactionProfit = 0;
    // the minimal cost of buying the stock in transaction #2, while taking into account the profit gained from the previous transaction #1. One can consider this as the cost of reinvestment.
    // Similar with firstTransactionCost, we try to find the lowest price so far, which in addition would be partially compensated by the profits gained from the first transaction.
    int secondTransactionCost = Integer.MAX_VALUE;
    // the maximal profit of selling the stock in transaction #2. With the help of secondTransactionCost as we prepared so far, we would find out the maximal profits with at most two transactions at each step.
    int secondTransactionProfit = 0;

    for (int price : prices) {
      // the maximum profit if only one transaction is allowed
      firstTransactionCost = Math.min(firstTransactionCost, price);
      firstTransactionProfit =
        Math.max(firstTransactionProfit, price - firstTransactionCost);
      // reinvest the gained profit in the second transaction
      secondTransactionCost =
        Math.min(secondTransactionCost, price - firstTransactionProfit);
      secondTransactionProfit =
        Math.max(secondTransactionProfit, price - secondTransactionCost);
    }

    return secondTransactionProfit;
  }
  // brute force try all possible choices
}
