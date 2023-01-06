// Hash Table, String, Breadth-First Search
// Amazon 36 Bloomberg 5 Microsoft 3 LinkedIn 3 Adobe 3 Google 2 Uber 2 Apple 2 Qualtrics 2 PayPay 2 Facebook 12 Lyft 6 Snapchat 3 Yahoo 2 Walmart Global Tech 2 Box 2 Intel 2 Twilio 2 Zillow 7 Expedia 5 Citadel 5 Salesforce 4 Hulu 4 VMware 4 Oracle 3 ByteDance 3 Goldman Sachs 3 Nutanix 2 SAP 2 Swiggy 2 Arcesium 2 Yelp
// https://leetcode.com/problems/word-ladder/

// A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

// Every adjacent pair of words differs by a single letter.
// Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
// sk == endWord
// Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

// Example 1:
// Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
// Output: 5
// Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
// Example 2:
// Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
// Output: 0
// Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
class WordLadder {

  // breadth first search in a graph where each char of the beginWord can be replaced by a-z(except self)
  // if next word in set, continue until the end word is reached
  public int ladderLength(
    String beginWord,
    String endWord,
    List<String> wordList
  ) {
    Set<String> words = new HashSet<>(wordList);
    if (!words.contains(endWord)) {
      return 0;
    }

    Queue<String> queue = new LinkedList<>();
    queue.offer(beginWord);

    // track strings that are already added inside our queue
    Set<String> visited = new HashSet<>();
    visited.add(beginWord);

    int changes = 0;
    while (!queue.isEmpty()) {
      changes++;
      List<String> currentWords = this.getCurrentLevelWords(queue);
      for (String currentWord : currentWords) {
        if (currentWord.equals(endWord)) {
          return changes;
        }

        List<String> nextWords = this.getNextWords(currentWord, words);
        for (String nextWord : nextWords) {
          if (visited.contains(nextWord)) {
            continue;
          }

          if (words.contains(nextWord)) {
            queue.offer(nextWord);
            visited.add(nextWord);
          }
        }
      }
    }

    return 0; // unable to reach end word
  }

  private List<String> getCurrentLevelWords(Queue<String> queue) {
    List<String> words = new ArrayList<>();
    while (!queue.isEmpty()) {
      words.add(queue.poll());
    }

    return words;
  }

  private List<String> getNextWords(String word, Set<String> words) {
    List<String> res = new ArrayList<>();
    StringBuilder wordBuilder = new StringBuilder(word);

    for (int i = 0; i < word.length(); i++) {
      char oldCharacter = wordBuilder.charAt(i);
      for (char newCharacter = 'a'; newCharacter <= 'z'; newCharacter++) {
        if (newCharacter != oldCharacter) {
          wordBuilder.setCharAt(i, newCharacter);
          String newWord = wordBuilder.toString();
          res.add(newWord);
        }
      }

      wordBuilder.setCharAt(i, oldCharacter);
    }

    return res;
  }
}
