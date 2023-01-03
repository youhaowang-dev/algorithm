// Two Pointers, String, String Matching
// Bloomberg 4 Amazon 4 Google 3 Apple 3 Microsoft 2 Yahoo 2 Facebook 4 Adobe 2 Zynga 2 Uber 5 Goldman Sachs 2 Pocket Gems
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

// Example 1:
// Input: haystack = "sadbutsad", needle = "sad"
// Output: 0
// Explanation: "sad" occurs at index 0 and 6.
// The first occurrence is at index 0, so we return 0.
// Example 2:
// Input: haystack = "leetcode", needle = "leeto"
// Output: -1
// Explanation: "leeto" did not occur in "leetcode", so we return -1.
class FindtheIndexoftheFirstOccurrenceinaString {

  public int strStr(String string, String substring) {
    for (int i = 0; i < string.length(); i++) {
      int stringIndex = i;
      int substringIndex = 0;
      while (
        stringIndex < string.length() && substringIndex < substring.length()
      ) {
        if (string.charAt(stringIndex) != substring.charAt(substringIndex)) {
          break;
        }
        stringIndex++;
        substringIndex++;
        if (substringIndex == substring.length()) {
          return i;
        }
      }
    }

    return -1;
  }

  public int strStr(String string, String substring) {
    for (int i = 0; i < string.length(); i++) {
      for (
        int substringIndex = 0;
        substringIndex < substring.length();
        substringIndex++
      ) {
        int stringIndex = i + substringIndex;
        if (stringIndex >= string.length()) {
          break;
        }
        char stringChar = string.charAt(stringIndex);
        char substringChar = substring.charAt(substringIndex);
        if (stringChar != substringChar) {
          break;
        }
        if (substringIndex == substring.length() - 1) {
          return i;
        }
      }
    }

    return -1;
  }

  // rolling hash O(m + n)
  private static final Integer BASE = 100007;

  public int strStr(String source, String target) {
    if (source == null || target == null) {
      return -1;
    }

    if (
      target.length() <= source.length() &&
      source.substring(0, target.length()).equals(target)
    ) {
      return 0;
    }

    int m = target.length();

    if (m == 0) {
      return 0;
    }

    int power = 1;

    for (int i = 0; i < m; i++) {
      power = (power * 31) % BASE;
    }

    int targetCode = 0;

    for (int i = 0; i < m; i++) {
      targetCode = (targetCode * 31 + target.charAt(i)) % BASE;
    }

    int sourceCode = 0;

    for (int i = 0; i < source.length(); i++) {
      sourceCode = (sourceCode * 31 + source.charAt(i)) % BASE;

      if (i <= m - 1) {
        continue;
      }

      sourceCode = (sourceCode - power * source.charAt(i - m)) % BASE;

      if (sourceCode < 0) {
        sourceCode += BASE;
      }

      if (sourceCode == targetCode) {
        return i - m + 1;
      }
    }

    return -1;
  }
}
