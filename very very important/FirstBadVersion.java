// tag: Binary Search, Interactive
// Google 10 Amazon 8 Adobe 7 Apple 6 Facebook 3 Microsoft 3 Uber 2

// You are a product manager and currently leading a team to develop a new product.
// Unfortunately, the latest version of your product fails the quality check.
// Since each version is developed based on the previous version, all the versions after a bad version are also bad.

// Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
// which causes all the following ones to be bad.

// You are given an API bool isBadVersion(version) which returns whether version is bad.
// Implement a function to find the first bad version. You should minimize the number of calls to the API.

// Example 1:
// Input: n = 5, bad = 4
// Output: 4
// Explanation:
// call isBadVersion(3) -> false
// call isBadVersion(5) -> true
// call isBadVersion(4) -> true
// Then 4 is the first bad version.

// Example 2:
// Input: n = 1, bad = 1
// Output: 1

final class FirstBadVersion {

  // TLE on leetcode but same complexity
  public int firstBadVersion(int n) {
    int start = 1;
    int end = n;
    while (start + 1 < end) {
      int mid = start - (start - end) / 2;
      if (isBadVersion(mid)) {
        end = mid;
      } else {
        start = mid + 1;
      }
    }
    if (isBadVersion(start)) {
      return start;
    }

    return end;
  }

  public int firstBadVersionV2(int n) {
    int start = 1;
    int end = n;
    while (start < end) {
      int mid = start - (start - end) / 2;
      if (isBadVersion(mid)) {
        end = mid;
      } else {
        start = mid + 1;
      }
    }

    // start == end
    return start;
  }
}
