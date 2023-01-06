// String
// Amazon 9 Microsoft 5 Bloomberg 5 Apple 4 Adobe 4 Facebook 25 Google 7 Goldman Sachs 5 Redfin 3 Uber 2 Qualcomm 2 LinkedIn 3 Splunk 3 Qualtrics 3 eBay 2 VMware 2 Cisco 2 Intel 2
// https://leetcode.com/problems/string-to-integer-atoi/description/
// Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
class StringtoInteger {

  // good question but bad test cases, not all the edge cases will be in an interview, so
  // make sure to ask enough questions and ask for unhandled cases(likely throw)

  // We need to handle the followings.
  // whitespaces, sign, overflow, invalid input
  public int myAtoi(String str) {
    if (str.isEmpty()) {
      return 0;
    }

    int i = 0;
    // whitespaces
    while (i < str.length() && str.charAt(i) == ' ') {
      i++;
    }
    if (i >= str.length()) {
      return 0;
    }

    // sign
    int sign = 1;
    if (str.charAt(i) == '-' || str.charAt(i) == '+') {
      if (str.charAt(i) == '-') {
        sign = -1;
      }
      i++; // still need to skip +
    }

    // build integer and check overflow and bad input
    int number = 0;
    while (i < str.length() && str.charAt(i) >= '0' && str.charAt(i) <= '9') {
      int digit = str.charAt(i) - '0';
      if (
        number > Integer.MAX_VALUE / 10 ||
        (number == Integer.MAX_VALUE / 10 && digit > Integer.MAX_VALUE % 10)
      ) {
        return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
      }
      number = 10 * number + (digit);
      i++;
    }

    return number * sign;
  }
}
