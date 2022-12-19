// Math, Dynamic Programming, Memoization
// Amazon 16 Adobe 11 Google 5 Apple 5 Bloomberg 3 Microsoft 3 Uber 2 Visa 2 Nagarro 2 Yahoo 4 Oracle 4 Goldman Sachs 3 Expedia 3 Intel 2 Facebook 4 Walmart Global Tech 3 Morgan Stanley 3 LinkedIn 2 eBay 2 Cisco 2 VMware 2 Twilio 2 Optum 2
// https://leetcode.com/problems/climbing-stairs/

// You are climbing a staircase. It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

// Example 1:
// Input: n = 2
// Output: 2
// Explanation: There are two ways to climb to the top.
// 1. 1 step + 1 step
// 2. 2 steps

// Example 2:
// Input: n = 3
// Output: 3
// Explanation: There are three ways to climb to the top.
// 1. 1 step + 1 step + 1 step
// 2. 1 step + 2 steps
// 3. 2 steps + 1 step

class ClimbingStairs {

  // brute force
  // function(i,n)=function(i+1,n)+climbStairs(i+2,n)
  // O(2^n)
  public int climbStairs(int n) {
    return this.climbStairs(0, n);
  }

  private int climbStairs(int i, int n) {
    if (i > n) {
      return 0;
    }
    if (i == n) {
      return 1;
    }

    return this.climbStairs(i + 1, n) + this.climbStairs(i + 2, n);
  }
}
