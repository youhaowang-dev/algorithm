// Hash Table, String, Dynamic Programming, Backtracking, Trie, Memoization
// Amazon 18 Bloomberg 17 Apple 4 Facebook 2 Microsoft 6 Google 3 Snapchat 3 Adobe 2 Audible 2 ByteDance 8 Uber 5 Walmart Global Tech 2 Twitter Dropbox
// https://leetcode.com/problems/word-break-ii/description/
// Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

// Note that the same word in the dictionary may be reused multiple times in the segmentation.

// Example 1:

// Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
// Output: ["cats and dog","cat sand dog"]
// Example 2:

// Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
// Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
// Explanation: Note that you are allowed to reuse a dictionary word.
// Example 3:

// Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
// Output: []
class WordBreakII {

  // dfs all substrings with memoization
  public List<String> wordBreak(String s, List<String> wordDict) {
    Map<String, ArrayList<String>> substringToResult = new HashMap<>();
    Set<String> wordSet = new HashSet<String>(wordDict);
    return this.wordBreakHelper(s, wordSet, substringToResult);
  }

  private List<String> wordBreakHelper(
    String s,
    Set<String> dict,
    Map<String, ArrayList<String>> substringToResult
  ) {
    // memo return
    if (substringToResult.containsKey(s)) {
      return substringToResult.get(s);
    }

    ArrayList<String> results = new ArrayList<>();
    // recursion exit
    if (s.length() == 0) {
      return results;
    }

    // special case where the entire rest is in the dict
    if (dict.contains(s)) {
      results.add(s);
    }

    for (int len = 1; len < s.length(); len++) {
      String substring = s.substring(0, len);
      if (!dict.contains(substring)) {
        continue;
      }
      // found one match, continue the rest
      String rest = s.substring(len);
      List<String> substringResults =
        this.wordBreakHelper(rest, dict, substringToResult);

      for (String substringResult : substringResults) {
        results.add(substring + " " + substringResult);
      }
    }

    // add to memo
    substringToResult.put(s, results);
    // return result
    return results;
  }
}
