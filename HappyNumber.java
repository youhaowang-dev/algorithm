// Hash Table, Math, Two Pointers
// Amazon 9 Google 5 Apple 4 Bloomberg 3 Facebook 3 Adobe 2 Yahoo 2 Paypal 6 Uber 2 Microsoft 2 TikTok 2 ByteDance 4 VMware 2 Intuit 2 Airbnb Twitter
// https://leetcode.com/problems/happy-number/description/

// Write an algorithm to determine if a number n is happy.

// A happy number is a number defined by the following process:

// Starting with any positive integer, replace the number by the sum of the squares of its digits.
// Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
// Those numbers for which this process ends in 1 are happy.
// Return true if n is a happy number, and false if not.

// Example 1:
// Input: n = 19
// Output: true
// Explanation:
// 12 + 92 = 82
// 82 + 22 = 68
// 62 + 82 = 100
// 12 + 02 + 02 = 1
// Example 2:
// Input: n = 2
// Output: false

class HappyNumber {

  // based on observation, the number wont be larger and larger
  // for example, 9999999999999 will be 1053 for the max 13 digits
  // so we need to detect 2 things
  // 1. it becomes 1
  // 2. it stucks in a cycle => set
  // time O(logn) because a million digit number will be reduced to 3 digits in a few steps, so the while loop is O(1)
  // space O(logn) to save all nexts
  public boolean isHappy(int n) {
    Set<Integer> seen = new HashSet<>();
    while (n != 1 && !seen.contains(n)) {
      seen.add(n);
      n = this.getNext(n);
    }
    // n == 1 or has cycle
    return n == 1;
  }

  // log(n) for /10
  private int getNext(int n) {
    int totalSum = 0;
    while (n > 0) {
      int digit = n % 10;
      n = n / 10;
      totalSum += digit * digit;
    }

    return totalSum;
  }
}
