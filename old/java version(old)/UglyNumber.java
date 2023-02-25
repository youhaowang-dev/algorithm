// Math
// Bloomberg 2 Facebook 2 Adobe 4 Amazon 2
// https://leetcode.com/problems/ugly-number/

// An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

// Given an integer n, return true if n is an ugly number.

// Example 1:

// Input: n = 6
// Output: true
// Explanation: 6 = 2 × 3
// Example 2:

// Input: n = 1
// Output: true
// Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
// Example 3:

// Input: n = 14
// Output: false
// Explanation: 14 is not ugly since it includes the prime factor 7.
class UglyNumber {

  // divide n by 2,3,5 repeatly until cannot( % != 0) to remove 2,3,5 from n, then check if result==1
  // Time complexity: O(log(N)) where N is the input number
  // We are dividing the integer by 2, 3, and 5 and terminating when it is not divisible by any of them.
  // Thus, there can be at most log2(N) divisions by 2, log3(N) divisions by 3 and log5(N) divisions by 5.
  // Thus, total number of divisions will be at most log2(N)+log3(N)+log5(N), which is O(log(N))
  public boolean isUgly(int n) {
    if (n <= 0) {
      return false;
    }

    int[] divisors = new int[] { 2, 3, 5 };

    for (int divisor : divisors) {
      n = this.divideUntilUndivisible(n, divisor);
    }

    // true if n can be reduced to 1
    return n == 1;
  }

  private int divideUntilUndivisible(int dividend, int divisor) {
    while (dividend % divisor == 0) {
      dividend /= divisor;
    }

    return dividend;
  }
}
