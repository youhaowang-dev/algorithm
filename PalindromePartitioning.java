// String, Dynamic Programming, Backtracking
// Bloomberg 6 Amazon 4 Adobe 2 Google 4 Apple 3 TikTok 3 Facebook 2 Uber 4 Microsoft 3 ByteDance 3
// https://leetcode.com/problems/palindrome-partitioning/

// Given a string s, partition s such that every substring of the partition is a palindrome.
// Return all possible palindrome partitioning of s.

// Example 1:
// Input: s = "aab"
// Output: [["a","a","b"],["aa","b"]]
// Example 2:
// Input: s = "a"
// Output: [["a"]]
class PalindromePartitioning {

  // time O(n2^n) for substring costs O(n) and every possible split can be picked or not
  // space O(n) for max recursion depth can be n
  public List<List<String>> partition(String s) {
    List<List<String>> result = new ArrayList<>();
    if (s == null || s.length() == 0) {
      return result;
    }

    int startIndex = 0;
    List<String> list = new ArrayList<>();
    this.partitionHelper(s, result, startIndex, list);

    return result;
  }

  private void partitionHelper(
    String s,
    List<List<String>> result,
    int startIndex,
    List<String> list
  ) {
    if (startIndex == s.length()) {
      result.add(new ArrayList<>(list));
      return;
    }

    for (int i = startIndex; i < s.length(); i++) {
      String subStr = s.substring(startIndex, i + 1);
      if (this.isPalindrome(subStr)) {
        list.add(subStr);
        this.partitionHelper(s, result, i + 1, list);
        list.remove(list.size() - 1);
      }
    }
  }

  private boolean isPalindrome(String s) {
    int left = 0;
    int right = s.length() - 1;
    while (left <= right) {
      if (s.charAt(left) != s.charAt(right)) {
        return false;
      }
      left++;
      right--;
    }

    return true;
  }
}
