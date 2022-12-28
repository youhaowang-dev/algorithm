// Hash Table, String, Sorting
// Amazon 20 Bloomberg 19 Spotify 3 Google 2 Goldman Sachs 2 Apple 2 Yahoo 2 Microsoft 7 Facebook 6 Affirm 3 Yandex 2 Qualcomm 2 Tesla 2 JPMorgan 5 Oracle 4 Cisco 4 Snapchat 3 Adobe 3 Walmart Global Tech 3 BlackRock 3 American Express 3 Grab 2 IBM 2 Visa 2 Dell 2 Uber Yelp

// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:
// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:
// Input: s = "rat", t = "car"
// Output: false

class ValidAnagram {

  // brute force: sort

  // hash table count
  // one str + one str -
  // finally anagram should have all key with count 0
  public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
      return false;
    }

    HashMap<Character, Integer> charToCount = new HashMap<>();
    for (int i = 0; i < s.length(); i++) {
      charToCount.put(
        s.charAt(i),
        charToCount.getOrDefault(s.charAt(i), 0) + 1
      );
      charToCount.put(
        t.charAt(i),
        charToCount.getOrDefault(t.charAt(i), 0) - 1
      );
    }

    for (char c : charToCount.keySet()) {
      if (charToCount.get(c) != 0) {
        return false;
      }
    }

    return true;
  }
}
