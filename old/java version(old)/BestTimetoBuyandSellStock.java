// Array, Dynamic Programming
// Amazon 44 Adobe 14 Apple 13 Bloomberg 10 Microsoft 10 Bolt 8 Facebook 6 Google 6 Cisco 5 Goldman Sachs 4 Uber 3 Oracle 3 PayTM 3 DE Shaw 2 Yahoo 2 Citadel 2 Salesforce 2 Walmart Global Tech 2 Intel 2 tcs 2
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

// Example 1:

// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
// Example 2:

// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transactions are done and the max profit = 0.

class BestTimetoBuyandSellStock {

  // maintain two variables - minprice and maxprofit
  public int maxProfit(int[] prices) {
    int minPrice = Integer.MAX_VALUE;
    int maxProfit = 0;
    for (int i = 0; i < prices.length; i++) {
      if (prices[i] < minPrice) {
        minPrice = prices[i];
      } else if (prices[i] - minPrice > maxProfit) {
        maxProfit = prices[i] - minPrice;
      }
    }

    return maxProfit;
  }

  // space optimized
  // profit and prefixSum can be a variable instead of an array of data
  public int maxProfit(int[] prices) {
    int maxProfitSum = 0;
    int minPrefixProfitSum = 0; // we don't have to trade, so init to 0; if we have to trade at least once, init to a different value probably min int
    int prefixProfitSum = 0;
    for (int i = 1; i < prices.length; i++) {
      int profit = prices[i] - prices[i - 1];
      prefixProfitSum = prefixProfitSum + profit;
      maxProfitSum =
        Math.max(maxProfitSum, prefixProfitSum - minPrefixProfitSum);
      minPrefixProfitSum = Math.min(minPrefixProfitSum, prefixProfitSum);
    }

    return maxProfitSum;
  }

  // build prefix sum and find the max subarray sum in it
  public int maxProfit(int[] prices) {
    int maxProfit = 0;

    int[] profits = new int[prices.length];
    profits[0] = 0; // buy today sell today
    for (int i = 1; i < prices.length; i++) {
      profits[i] = prices[i] - prices[i - 1];
    }

    // now find the max subarray sum(max profit sum)
    int[] prefixSum = new int[prices.length + 1];
    prefixSum[0] = 0;
    for (int i = 1; i < prefixSum.length; i++) {
      prefixSum[i] = prefixSum[i - 1] + profits[i - 1];
    }

    int minPrefixSum = 0;
    for (int i = 1; i < prefixSum.length; i++) {
      maxProfit = Math.max(maxProfit, prefixSum[i] - minPrefixSum);
      minPrefixSum = Math.min(minPrefixSum, prefixSum[i]);
    }

    return maxProfit;
  }

  // brute force: find the max diff
  public int maxProfit(int[] prices) {
    int maxProfit = 0;
    for (int i = 0; i < prices.length - 1; i++) {
      for (int j = i + 1; j < prices.length; j++) {
        int profit = prices[j] - prices[i];
        // if we are forced to bug and sell at least once, use Math.max and take care of init
        if (profit > maxProfit) {
          maxProfit = profit;
        }
      }
    }

    return maxProfit;
  }
}
