// https://www.lintcode.com/problem/37/
// Reverse a 3-digit integer.
// Example 1:
// Input:
// number = 123
// Output: 321
// Explanation:
// Reverse the number.
// Example 2:
// Input:
// number = 900
// Output: 9
// Explanation:
// Reverse the number.

class Reverse3digitInteger {

  public int reverseInteger(int number) {
    int digit1 = number % 10;
    number = number / 10;
    int digit2 = number % 10;
    number = number / 10;
    int digit3 = number % 10;
    number = number / 10;

    return 100 * digit1 + 10 * digit2 + 1 * digit3;
  }
}
