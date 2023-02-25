// tag: Array, Binary Search, Interactive
// Facebook 3 Microsoft 2 Adobe 2 Google 3 instacart 3
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

// This is an interactive problem.
// You have a sorted array of unique elements and an unknown size.
// You do not have an access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:
// returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
// returns 2^31 - 1 if the i is out of the boundary of the array.
// You are also given an integer target.

// Return the index k of the hidden array where secret[k] == target or return -1 otherwise.
// You must write an algorithm with O(log n) runtime complexity.

// Example 1:
// Input: secret = [-1,0,3,5,9,12], target = 9
// Output: 4
// Explanation: 9 exists in secret and its index is 4.

// Example 2:
// Input: secret = [-1,0,3,5,9,12], target = 2
// Output: -1
// Explanation: 2 does not exist in secret so return -1.

final class SearchInASortedArrayOfUnknownSize {

  // brute force: call function and length++

  // binary search the [left, right], then search inside
  public int search(ArrayReader reader, int target) {
    int left = 0;
    int right = 1;

    // binary search the range
    while (reader.get(right) < target) {
      left = right;
      right = right * 2; // can also do << 1
    }
    // binary search the target
    while (left + 1 < right) {
      int mid = left - (left - right) / 2;
      int midVal = reader.get(mid);
      if (midVal == target) {
        return mid;
      }
      if (midVal < target) {
        left = mid;
      }
      if (midVal > target) {
        right = mid;
      }
    }
    if (reader.get(left) == target) {
      return left;
    }
    if (reader.get(right) == target) {
      return right;
    }

    return -1;
  }
}
