// Array, Dynamic Programming, Greedy
// Bloomberg 6 Amazon 5 Adobe 3 Microsoft 2 Goldman Sachs 2 Apple 2 Google 5 Walmart Global Tech 4 Facebook 3 Oracle 3 Uber 3 tcs 7 Morgan Stanley 4 Expedia 4 ByteDance 3 DE Shaw 3 Nutanix 2 Citadel 2 Salesforce 2

// You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

// On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

// Find and return the maximum profit you can achieve.

// Example 1:
// Input: prices = [7,1,5,3,6,4]
// Output: 7
// Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
// Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
// Total profit is 4 + 3 = 7.
// Example 2:
// Input: prices = [1,2,3,4,5]
// Output: 4
// Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
// Total profit is 4.
// Example 3:
// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

// unlimited buy-sell but can only hold one stock
class BestTimetoBuyandSellStockII {

  // sell whenever there is a profit
  // just say this is based on my observation
  public int maxProfit(int[] prices) {
    int profitSum = 0;
    for (int i = 1; i < prices.length; i++) {
      int profit = prices[i] - prices[i - 1];
      if (profit > 0) {
        profitSum = profitSum + profit;
      }
    }

    return profitSum;
  }

  // brute force try all the possible transactions
  // time n^n the function is called n^n times; each n will trigger another n recursively until n is 0, so n^n
  // space n recursion stack
  public int maxProfit(int[] prices) {
    return this.getMaxProfitByDay(prices, 0);
  }

  public int getMaxProfitByDay(int prices[], int day) {
    if (day >= prices.length) {
      return 0;
    }

    int max = 0;
    for (int start = day; start < prices.length; start++) {
      int maxProfit = 0;
      for (int nextDay = start + 1; nextDay < prices.length; nextDay++) {
        if (prices[start] < prices[nextDay]) {
          int profit =
            this.getMaxProfitByDay(prices, nextDay + 1) +
            prices[nextDay] -
            prices[start];
          if (profit > maxProfit) {
            maxProfit = profit;
          }
        }
      }
      if (maxProfit > max) {
        max = maxProfit;
      }
    }

    return max;
  }
}
