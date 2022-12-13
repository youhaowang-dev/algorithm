// String, String Matching
// Amazon 3 Apple 2 Goldman Sachs 3 Zoom 3 LinkedIn 2 Microsoft 2 Oracle 2 Cisco 2 Bloomberg 3 Adobe 3 Google 2 Yahoo 2 Morgan Stanley 2
// https://leetcode.com/problems/rotate-string/
// Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

// A shift on s consists of moving the leftmost character of s to the rightmost position.

// For example, if s = "abcde", then it will be "bcdea" after one shift.

// Example 1:
// Input: s = "abcde", goal = "cdeab"
// Output: true

// Example 2:
// Input: s = "abcde", goal = "abced"
// Output: false

final class RotateString {

  // https://leetcode.com/problems/rotate-string/solutions/678931/best-solution-for-an-interview-java-thoughts-and-takeaways/?orderBy=most_votes

  // More specifically, say we rotate A by s.
  // Then, instead of A[0], A[1], A[2], ..., we have A[s], A[s+1], A[s+2], ...;
  // and we should check that A[s] == B[0], A[s+1] == B[1], A[s+2] == B[2], etc.
  public boolean rotateString(String A, String B) {
    if (A == null || B == null) {
      // throw?
      return false;
    }
    if (A.length() != B.length()) {
      return false;
    }
    int length = A.length();
    if (length == 0) {
      return true;
    }
    for (int rotation = 0; rotation < length; rotation++) {
      if (isRotated(A, B, rotation)) {
        return true;
      }
    }
    return false;
  }

  private boolean isRotated(String A, String B, int rotation) {
    int length = A.length();
    for (int i = 0; i < length; i++) {
      int bIndex = (i + rotation) % length;
      if (A.charAt(i) != B.charAt(bIndex)) {
        return false;
      }
    }
    return true;
  }

  // All rotations of A are contained in A+A. Thus, we can simply check
  // whether B is a substring of A+A. We also need to check A.length == B.length,
  // otherwise we will fail cases like A = "a", B = "aa".
  public boolean rotateString2(String A, String B) {
    return A.length() == B.length() && (A + A).contains(B);
  }
}
