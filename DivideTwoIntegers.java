// Math, Bit Manipulation
// Amazon 3 Facebook 2 Google 2 Uber 2 Microsoft 4 Bloomberg 4 Adobe 4 Apple 2 Yahoo 2 Oracle 2
// https://leetcode.com/problems/divide-two-integers/description/
// Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

// The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

// Return the quotient after dividing dividend by divisor.

// Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

// Example 1:
// Input: dividend = 10, divisor = 3
// Output: 3
// Explanation: 10/3 = 3.33333.. which is truncated to 3.
// Example 2:
// Input: dividend = 7, divisor = -3
// Output: -2
// Explanation: 7/-3 = -2.33333.. which is truncated to -2.
class DivideTwoIntegers {

  // NOTE: Math.abs(Integer.MIN_VALUE) = Integer.MIN_VALUE
  // Integer.MIN_VALUE is -2147483648, but the highest value a 32 bit integer can contain is +2147483647. Attempting to represent +2147483648 in a 32 bit int will effectively "roll over" to -2147483648.
  // negative number has a longer range than positive number
  // so convert positive to negative
  public int divide(int dividend, int divisor) {
    if (dividend == Integer.MIN_VALUE && divisor == -1) {
      return Integer.MAX_VALUE;
    }

    int sign = 0;
    if (dividend > 0 && divisor > 0) {
      sign = 1;
    }
    if (dividend > 0 && divisor < 0) {
      sign = -1;
    }
    if (dividend < 0 && divisor > 0) {
      sign = -1;
    }
    if (dividend < 0 && divisor < 0) {
      sign = 1;
    }

    // convert to negative
    dividend = dividend > 0 ? -dividend : dividend;
    divisor = divisor > 0 ? -divisor : divisor;
    int res = this.divideHelper(dividend, divisor);

    return sign * res;
  }

  private int divideHelper(int dividend, int divisor) {
    int result = 0;

    while (dividend <= divisor) {
      int maxShifts = this.getMaxShifts(dividend, divisor);
      dividend -= divisor << maxShifts;
      result += 1 << maxShifts;
    }

    return result;
  }

  // negative num
  // -10 and -3, -6, -12, ...
  private int getMaxShifts(int dividend, int divisor) {
    int shifts = 0;
    while (dividend <= divisor) {
      if (divisor <= Integer.MIN_VALUE / 2) {
        // dont play with possible overflow
        return shifts;
      }
      divisor = divisor << 1;
      shifts++;
    }
    // dividend > divisor; -10 > -12
    return shifts - 1;
  }

  private int divideHelper(int dividend, int divisor) {
    int result = 0;
    while (dividend <= divisor) {
      dividend -= divisor;
      result++;
    }

    return result;
  }
}
