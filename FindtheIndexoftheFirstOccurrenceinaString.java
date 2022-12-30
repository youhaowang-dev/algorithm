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
}
