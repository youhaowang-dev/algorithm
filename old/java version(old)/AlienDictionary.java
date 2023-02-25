// Array, String, Depth-First Search, Breadth-First Search, Graph, Topological Sort
// Airbnb 15 Amazon 2 Facebook 2 Bloomberg 2 Google 6 Microsoft 6 Uber 5 Snapchat 3 Rubrik 12 Pinterest 6 Apple 4 Twitter 3 eBay 3 ByteDance 3 Coupang 2 Pocket Gems Wix
// https://leetcode.com/problems/alien-dictionary/description/
// There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

// You are given a list of strings words from the alien language's dictionary, where the strings in words are
// sorted lexicographically
//  by the rules of this new language.

// Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

// Example 1:
// Input: words = ["wrt","wrf","er","ett","rftt"]
// Output: "wertf"
// Example 2:
// Input: words = ["z","x"]
// Output: "zx"
// Example 3:
// Input: words = ["z","x","z"]
// Output: ""
// Explanation: The order is invalid, so return "".
class AlienDictionary {

  // the first different char of two words can form an edge
  // for example, "wrt","wrf" => t > f => t -> f
  // there could be more chars between t and f, so we need to get all edges and do topological sort
  public String alienOrder(String[] words) {
    Map<Character, Set<Character>> charToChars = this.buildGraph(words);
    if (charToChars == null) {
      return "";
    }

    return this.getTopologicalOrder(charToChars);
  }

  private Map<Character, Set<Character>> buildGraph(String[] words) {
    Map<Character, Set<Character>> graph = new HashMap<>();
    // build nodes
    for (String word : words) {
      for (char character : word.toCharArray()) {
        if (!graph.containsKey(character)) {
          graph.put(character, new HashSet<Character>());
        }
      }
    }
    // build edges
    for (int i = 0; i < words.length - 1; i++) {
      int index = 0;
      while (index < words[i].length() && index < words[i + 1].length()) {
        Character currentChar = words[i].charAt(index);
        Character nextChar = words[i + 1].charAt(index);
        if (currentChar != nextChar) {
          graph.get(currentChar).add(nextChar);
          break; // only need the first diff chars
        }
        index++;
      }
      // check invalid input
      if (index == Math.min(words[i].length(), words[i + 1].length())) {
        if (words[i].length() > words[i + 1].length()) {
          return null;
        }
      }
    }

    return graph;
  }

  private String getTopologicalOrder(Map<Character, Set<Character>> graph) {
    Map<Character, Integer> indegree = this.getIndegree(graph);
    Queue<Character> queue = new LinkedList<>();
    for (Character c : indegree.keySet()) {
      if (indegree.get(c) == 0) {
        queue.offer(c);
      }
    }

    StringBuilder resultBuilder = new StringBuilder();
    while (!queue.isEmpty()) {
      Character head = queue.poll();
      resultBuilder.append(head);
      for (Character neighbor : graph.get(head)) {
        indegree.put(neighbor, indegree.get(neighbor) - 1);
        if (indegree.get(neighbor) == 0) {
          queue.offer(neighbor);
        }
      }
    }

    if (resultBuilder.length() != indegree.size()) {
      return "";
    }

    return resultBuilder.toString();
  }

  private Map<Character, Integer> getIndegree(
    Map<Character, Set<Character>> graph
  ) {
    Map<Character, Integer> indegree = new HashMap<>();
    for (Character from : graph.keySet()) {
      indegree.put(from, 0);
    }

    for (Character from : graph.keySet()) {
      for (Character to : graph.get(from)) {
        indegree.putIfAbsent(to, 0);
        indegree.put(to, indegree.get(to) + 1);
      }
    }

    return indegree;
  }
}
