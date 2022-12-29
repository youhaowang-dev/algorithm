// String, Dynamic Programming
// Amazon 2 Yahoo 2 Bloomberg 3 Google 2 Facebook 2 Apple 2 Microsoft 2 TikTok 2
// https://leetcode.com/problems/palindrome-partitioning-ii/

// Given a string s, partition s such that every substring  of the partition is a palindrome.
// Return the minimum cuts needed for a palindrome partitioning of s.

// Example 1:
// Input: s = "aab"
// Output: 1
// Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
// Example 2:
// Input: s = "a"
// Output: 0
// Example 3:
// Input: s = "ab"
// Output: 1
class PalindromePartitioningII {

  // time O(n2^n)
  // space O(n) recursion depth
  public int minCut(String s) {
    if (s == null || s.length() == 0) {
      return 0;
    }

    if (this.isPalindrome(s)) {
      return 0;
    }

    int startIndex = 0;
    int endIndex = s.length() - 1;
    return this.minCutHelper(s, startIndex, endIndex);
  }

  private int minCutHelper(String s, int start, int end) {
    // an empty substring or palindrome substring
    if (start == end) {
      return 0;
    }

    int min = end - start;
    for (int i = start; i <= end; i++) {
      String substring = s.substring(start, i + 1);
      if (this.isPalindrome(substring)) {
        min = Math.min(min, 1 + this.minCutHelper(s, i + 1, end));
      }
    }

    return min;
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

  // Expand Around the Center
  // time O(n^2)
  public int minCut(String s) {
    int[] minCuts = new int[s.length()];
    for (int i = 0; i < s.length(); i++) {
      // Initially, the value of cutsDp[i] would be the maximum possible number of cuts till index i, which is equivalent to i.
      int maxCut = i;
      minCuts[i] = maxCut;
    }
    for (int mid = 0; mid < s.length(); mid++) {
      // check for odd length palindrome around mid index
      this.findMinimumCuts(mid, mid, minCuts, s);
      // check for even length palindrome around mid index
      this.findMinimumCuts(mid - 1, mid, minCuts, s);
    }

    return minCuts[s.length() - 1];
  }

  // expand from the middle
  public void findMinimumCuts(
    int leftStart,
    int rightStart,
    int[] minCuts,
    String s
  ) {
    int left = leftStart;
    int right = rightStart;
    while (
      left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)
    ) {
      int newCut = left == 0 ? 0 : minCuts[left - 1] + 1;
      minCuts[right] = Math.min(minCuts[right], newCut);
      left--;
      right++;
    }
  }
}
