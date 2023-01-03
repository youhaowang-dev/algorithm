// Math
// Amazon 11 Apple 9 Adobe 7 Bloomberg 5 Microsoft 3 tcs 3 Oracle 2 Google 2 Uber 2 Intel 2 Facebook 6 Yahoo 3 Infosys 3 Visa 2 IBM 2 American Express 6 eBay 4 Samsung 2 Accenture 2
// https://leetcode.com/problems/reverse-integer/
// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

// Example 1:
// Input: x = 123
// Output: 321
// Example 2:
// Input: x = -123
// Output: -321
// Example 3:
// Input: x = 120
// Output: 21
class ReverseInteger {

  // time: O(log(number)) total digits bounded by log10(number)
  // space: O(1)
  public int reverse(int number) {
    int reversedNumber = 0;
    while (number != 0) {
      int digit = number % 10;
      number = number / 10;
      if (this.shiftLeftWillOverflow(reversedNumber, digit)) {
        return 0;
      }
      reversedNumber = reversedNumber * 10 + digit;
    }

    return reversedNumber;
  }

  // 2147483647 and -2147483648
  private boolean shiftLeftWillOverflow(int number, int digit) {
    boolean prevDigitsWillExceedMax = number > Integer.MAX_VALUE / 10;
    boolean lastDigitWillExceedMax =
      number == Integer.MAX_VALUE / 10 && digit > 7;
    boolean prevDigitsWillExceedMin = number < Integer.MIN_VALUE / 10;
    boolean lastDigitWillExceedMin =
      number == Integer.MIN_VALUE / 10 && digit < -8;

    return (
      prevDigitsWillExceedMax ||
      lastDigitWillExceedMax ||
      prevDigitsWillExceedMin ||
      lastDigitWillExceedMin
    );
  }
}
