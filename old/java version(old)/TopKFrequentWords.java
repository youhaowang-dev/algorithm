// Hash Table, String, Trie, Sorting, Heap (Priority Queue), Bucket Sort, Counting
// Amazon 7 Uber 7 Bloomberg 6 Google 4 Yahoo 4 Microsoft 3 Apple 3 Atlassian 3 IBM 3 Adobe 2 Facebook 5 Two Sigma 3 Goldman Sachs 2 Oracle 7 Salesforce 3 Visa 3 Nvidia 2 Yelp 2 ByteDance 2 Zillow 2 Twitch 2 Wish 2 Indeed 2 Pocket Gems
// https://leetcode.com/problems/top-k-frequent-words/description/

// Given an array of strings words and an integer k, return the k most frequent strings.

// Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

// Example 1:
// Input: words = ["i","love","leetcode","i","love","coding"], k = 2
// Output: ["i","love"]
// Explanation: "i" and "love" are the two most frequent words.
// Note that "i" comes before "love" due to a lower alphabetical order.
// Example 2:
// Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
// Output: ["the","is","sunny","day"]
// Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

class TopKFrequentWords {

  // min heap
  public List<String> topKFrequent(String[] words, int k) {
    Map<String, Integer> wordToCount = new HashMap<>();
    for (String word : words) {
      wordToCount.putIfAbsent(word, 0);
      wordToCount.put(word, wordToCount.get(word) + 1);
    }

    // low count at top; low dictionary order at top
    PriorityQueue<String> minHeap = new PriorityQueue<>((w1, w2) ->
      wordToCount.get(w1) == wordToCount.get(w2)
        ? w2.compareTo(w1)
        : wordToCount.get(w1) - wordToCount.get(w2)
    );

    for (String word : wordToCount.keySet()) {
      minHeap.offer(word);
      if (minHeap.size() > k) minHeap.poll();
    }

    List<String> res = new ArrayList<>();
    while (!minHeap.isEmpty()) res.add(minHeap.poll());
    Collections.reverse(res);
    return res;
  }

  // brute force time O(nlogn)
  // we just need to sort all words by their frequencies and return the first k words. Notice that the sorting order is first by frequencies then lexicographically.
  public List<String> topKFrequent(String[] words, int k) {
    Map<String, Integer> wordToCount = new HashMap<>();
    for (String word : words) {
      wordToCount.putIfAbsent(word, 0);
      wordToCount.put(word, wordToCount.get(word) + 1);
    }

    List<String> candidates = new ArrayList<>(wordToCount.keySet());
    Collections.sort(
      candidates,
      (word1, word2) -> {
        if (wordToCount.get(word1) == wordToCount.get(word2)) {
          return word1.compareTo(word2);
        }

        return wordToCount.get(word2) - wordToCount.get(word1);
      }
    );

    return candidates.subList(0, k);
  }

  // trie
  private int k;
  private List<String> res;

  public List<String> topKFrequent(String[] words, int k) {
    this.k = k;
    res = new ArrayList<>();
    int n = words.length;
    TrieNode[] bucket = new TrieNode[n + 1];
    Map<String, Integer> cnt = new HashMap<>();

    for (String word : words) {
      cnt.put(word, cnt.getOrDefault(word, 0) + 1);
    }

    for (var entry : cnt.entrySet()) {
      if (bucket[entry.getValue()] == null) bucket[entry.getValue()] =
        new TrieNode();
      this.addWord(bucket[entry.getValue()], entry.getKey());
    }

    for (int i = n; i > 0; i--) {
      if (bucket[i] != null) {
        this.getWords(bucket[i], "");
      }
      if (this.k == 0) {
        break;
      }
    }
    return res;
  }

  class TrieNode {

    TrieNode[] children;
    boolean isWord;

    public TrieNode() {
      children = new TrieNode[26];
      isWord = false;
    }
  }

  private void addWord(TrieNode root, String word) {
    TrieNode cur = root;
    for (char c : word.toCharArray()) {
      if (cur.children[c - 'a'] == null) {
        cur.children[c - 'a'] = new TrieNode();
      }
      cur = cur.children[c - 'a'];
    }
    cur.isWord = true;
  }

  private void getWords(TrieNode root, String prefix) {
    if (this.k == 0) {
      return;
    }
    if (root.isWord) {
      this.k--;
      res.add(prefix);
    }
    for (int i = 0; i < 26; i++) {
      if (root.children[i] != null) {
        getWords(root.children[i], prefix + (char) (i + 'a'));
      }
    }
  }
}
