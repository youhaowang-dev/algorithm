// Hash Table, String, Dynamic Programming, Trie, Memoization
// Amazon 19 Bloomberg 11 Facebook 7 Wish 5 Apple 4 Adobe 4 Google 2 Microsoft 2 TikTok 2 Qualtrics 4 Oracle 3 Walmart Global Tech 3 Twitter 2 eBay 2 Yahoo 2 Salesforce 2 Cohesity 2 Uber 10 ByteDance 6 Snapchat 3 LinkedIn 2 Nvidia 2 Visa 2 Swiggy 2 Goldman Sachs 2 Pocket Gems Square Coupang

// Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

// Note that the same word in the dictionary may be reused multiple times in the segmentation.

// Example 1:

// Input: s = "leetcode", wordDict = ["leet","code"]
// Output: true
// Explanation: Return true because "leetcode" can be segmented as "leet code".
// Example 2:

// Input: s = "applepenapple", wordDict = ["apple","pen"]
// Output: true
// Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
// Note that you are allowed to reuse a dictionary word.
// Example 3:

// Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
// Output: false

class WordBreak {

  // TLE: TODO: fix it
  //   // BFS
  //   // time n^3 For every starting index, the search can continue till the end of the given string.
  //   // space n Queue of at most nnn size is needed.
  //   public boolean wordBreak(String s, List<String> wordDict) {
  //     Set<String> wordDictSet = new HashSet<>(wordDict);
  //     Queue<Integer> searchStartIndex = new LinkedList<>();
  //     searchStartIndex.offer(0);
  //     boolean[] visited = new boolean[s.length()];

  //     while (!searchStartIndex.isEmpty()) {
  //       int start = searchStartIndex.poll();
  //       if (visited[start]) {
  //         continue;
  //       }
  //       // <= s.length() for substring(inclusive, exclusive)
  //       for (int end = start + 1; end <= s.length(); end++) {
  //         if (wordDictSet.contains(s.substring(start, end))) {
  //           searchStartIndex.offer(end);
  //           if (end == s.length()) {
  //             // able to reach the end of string
  //             return true;
  //           }
  //         }
  //       }
  //     }

  //     return false;
  //   }

  // DFS with memoization
  // time n^3 size of recursion tree can go up to n^2
  // space n the depth of recursion tree can go up to n
  // we check every possible prefix of that string in the dictionary of words,
  // if it is found in the dictionary, then the recursive function is called for the remaining portion of that string.
  // And, if in some function call it is found that the complete string is in dictionary, then it will return true.
  public boolean wordBreak(String s, List<String> wordDict) {
    return this.wordBreakMemoized(
        s,
        new HashSet<>(wordDict),
        0,
        new Boolean[s.length()]
      );
  }

  private boolean wordBreakMemoized(
    String s,
    Set<String> wordDict,
    int start,
    Boolean[] memo
  ) {
    if (start == s.length()) {
      return true;
    }

    if (memo[start] != null) {
      return memo[start];
    }

    for (int end = start + 1; end <= s.length(); end++) {
      if (
        wordDict.contains(s.substring(start, end)) &&
        this.wordBreakMemoized(s, wordDict, end, memo)
      ) {
        return memo[start] = true;
      }
    }

    return memo[start] = false;
  }
}
